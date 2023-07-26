from __future__ import annotations

import logging
from typing import Dict, List, Optional

from chik_rs import ENABLE_ASSERT_BEFORE, LIMIT_STACK, MEMPOOL_MODE, NO_RELATIVE_CONDITIONS_ON_EPHEMERAL
from chik_rs import get_puzzle_and_solution_for_coin as get_puzzle_and_solution_for_coin_rust
from chik_rs import run_block_generator, run_chik_program
from klvm.casts import int_from_bytes

from chik.consensus.constants import ConsensusConstants
from chik.consensus.cost_calculator import NPCResult
from chik.consensus.default_constants import DEFAULT_CONSTANTS
from chik.types.blockchain_format.coin import Coin
from chik.types.blockchain_format.program import Program
from chik.types.blockchain_format.serialized_program import SerializedProgram
from chik.types.blockchain_format.sized_bytes import bytes32
from chik.types.coin_record import CoinRecord
from chik.types.coin_spend import CoinSpend, SpendInfo
from chik.types.generator_types import BlockGenerator
from chik.types.spend_bundle_conditions import SpendBundleConditions
from chik.util.errors import Err
from chik.util.ints import uint16, uint32, uint64
from chik.wallet.puzzles.load_klvm import load_serialized_klvm_maybe_recompile

DESERIALIZE_MOD = load_serialized_klvm_maybe_recompile(
    "chiklisp_deserialisation.clsp", package_or_requirement="chik.wallet.puzzles"
)

log = logging.getLogger(__name__)


def get_name_puzzle_conditions(
    generator: BlockGenerator,
    max_cost: int,
    *,
    mempool_mode: bool,
    height: uint32,
    constants: ConsensusConstants = DEFAULT_CONSTANTS,
) -> NPCResult:
    if mempool_mode:
        flags = MEMPOOL_MODE
    else:
        flags = LIMIT_STACK

    if height >= constants.SOFT_FORK2_HEIGHT:
        flags = flags | ENABLE_ASSERT_BEFORE | NO_RELATIVE_CONDITIONS_ON_EPHEMERAL

    try:
        block_args = [bytes(gen) for gen in generator.generator_refs]
        err, result = run_block_generator(bytes(generator.program), block_args, max_cost, flags)
        assert (err is None) != (result is None)
        if err is not None:
            return NPCResult(uint16(err), None, uint64(0))
        else:
            assert result is not None
            return NPCResult(None, result, uint64(result.cost))
    except BaseException:
        log.exception("get_name_puzzle_condition failed")
        return NPCResult(uint16(Err.GENERATOR_RUNTIME_ERROR.value), None, uint64(0))


def get_puzzle_and_solution_for_coin(generator: BlockGenerator, coin: Coin) -> SpendInfo:
    try:
        args = bytearray(b"\xff")
        args += bytes(DESERIALIZE_MOD)
        args += b"\xff"
        args += bytes(Program.to([bytes(a) for a in generator.generator_refs]))
        args += b"\x80\x80"

        puzzle, solution = get_puzzle_and_solution_for_coin_rust(
            bytes(generator.program),
            bytes(args),
            DEFAULT_CONSTANTS.MAX_BLOCK_COST_KLVM,
            coin.parent_coin_info,
            coin.amount,
            coin.puzzle_hash,
        )
        return SpendInfo(SerializedProgram.from_bytes(puzzle), SerializedProgram.from_bytes(solution))
    except Exception as e:
        raise ValueError(f"Failed to get puzzle and solution for coin {coin}, error: {e}") from e


def get_spends_for_block(generator: BlockGenerator) -> List[CoinSpend]:
    args = bytearray(b"\xff")
    args += bytes(DESERIALIZE_MOD)
    args += b"\xff"
    args += bytes(Program.to([bytes(a) for a in generator.generator_refs]))
    args += b"\x80\x80"

    _, ret = run_chik_program(
        bytes(generator.program),
        bytes(args),
        DEFAULT_CONSTANTS.MAX_BLOCK_COST_KLVM,
        0,
    )

    spends: List[CoinSpend] = []

    for spend in Program.to(ret).first().as_iter():
        parent, puzzle, amount, solution = spend.as_iter()
        puzzle_hash = puzzle.get_tree_hash()
        coin = Coin(parent.atom, puzzle_hash, int_from_bytes(amount.atom))
        spends.append(CoinSpend(coin, puzzle, solution))

    return spends


def mempool_check_time_locks(
    removal_coin_records: Dict[bytes32, CoinRecord],
    bundle_conds: SpendBundleConditions,
    prev_transaction_block_height: uint32,
    timestamp: uint64,
) -> Optional[Err]:
    """
    Check all time and height conditions against current state.
    """

    if prev_transaction_block_height < bundle_conds.height_absolute:
        return Err.ASSERT_HEIGHT_ABSOLUTE_FAILED
    if timestamp < bundle_conds.seconds_absolute:
        return Err.ASSERT_SECONDS_ABSOLUTE_FAILED
    if bundle_conds.before_height_absolute is not None:
        if prev_transaction_block_height >= bundle_conds.before_height_absolute:
            return Err.ASSERT_BEFORE_HEIGHT_ABSOLUTE_FAILED
    if bundle_conds.before_seconds_absolute is not None:
        if timestamp >= bundle_conds.before_seconds_absolute:
            return Err.ASSERT_BEFORE_SECONDS_ABSOLUTE_FAILED

    for spend in bundle_conds.spends:
        unspent = removal_coin_records[bytes32(spend.coin_id)]
        if spend.birth_height is not None:
            if spend.birth_height != unspent.confirmed_block_index:
                return Err.ASSERT_MY_BIRTH_HEIGHT_FAILED
        if spend.birth_seconds is not None:
            if spend.birth_seconds != unspent.timestamp:
                return Err.ASSERT_MY_BIRTH_SECONDS_FAILED
        if spend.height_relative is not None:
            if prev_transaction_block_height < unspent.confirmed_block_index + spend.height_relative:
                return Err.ASSERT_HEIGHT_RELATIVE_FAILED
        if spend.seconds_relative is not None:
            if timestamp < unspent.timestamp + spend.seconds_relative:
                return Err.ASSERT_SECONDS_RELATIVE_FAILED
        if spend.before_height_relative is not None:
            if prev_transaction_block_height >= unspent.confirmed_block_index + spend.before_height_relative:
                return Err.ASSERT_BEFORE_HEIGHT_RELATIVE_FAILED
        if spend.before_seconds_relative is not None:
            if timestamp >= unspent.timestamp + spend.before_seconds_relative:
                return Err.ASSERT_BEFORE_SECONDS_RELATIVE_FAILED

    return None
