from __future__ import annotations

from chik.types.blockchain_format.serialized_program import SerializedProgram

from .load_klvm import load_serialized_klvm_maybe_recompile

GENERATOR_MOD: SerializedProgram = load_serialized_klvm_maybe_recompile("rom_bootstrap_generator.clsp")
