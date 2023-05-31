from __future__ import annotations

from chik.types.blockchain_format.program import Program
from chik.types.blockchain_format.sized_bytes import bytes32
from chik.util.ints import uint64
from chik.wallet.puzzles.load_clvm import load_clvm_maybe_recompile

NOTIFICATION_MOD = load_clvm_maybe_recompile("notification.clsp")


def construct_notification(target: bytes32, amount: uint64) -> Program:
    return NOTIFICATION_MOD.curry(target, amount)
