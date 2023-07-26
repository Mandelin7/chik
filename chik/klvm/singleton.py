from __future__ import annotations

from chik.wallet.puzzles.load_klvm import load_klvm_maybe_recompile

P2_SINGLETON_MOD = load_klvm_maybe_recompile("p2_singleton.clsp")
SINGLETON_TOP_LAYER_MOD = load_klvm_maybe_recompile("singleton_top_layer.clsp")
SINGLETON_LAUNCHER = load_klvm_maybe_recompile("singleton_launcher.clsp")
