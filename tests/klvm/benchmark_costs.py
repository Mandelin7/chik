from __future__ import annotations

from chik.consensus.cost_calculator import NPCResult
from chik.consensus.default_constants import DEFAULT_CONSTANTS
from chik.full_node.bundle_tools import simple_solution_generator
from chik.full_node.mempool_check_conditions import get_name_puzzle_conditions
from chik.types.blockchain_format.program import INFINITE_COST
from chik.types.generator_types import BlockGenerator
from chik.types.spend_bundle import SpendBundle


def cost_of_spend_bundle(spend_bundle: SpendBundle) -> int:
    program: BlockGenerator = simple_solution_generator(spend_bundle)
    # always use the post soft-fork2 semantics
    npc_result: NPCResult = get_name_puzzle_conditions(
        program,
        INFINITE_COST,
        mempool_mode=True,
        height=DEFAULT_CONSTANTS.SOFT_FORK3_HEIGHT,
        constants=DEFAULT_CONSTANTS,
    )
    return npc_result.cost
