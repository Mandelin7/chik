from __future__ import annotations

from chik.wallet.puzzles.load_klvm import load_klvm_maybe_recompile

CAT_MOD = load_klvm_maybe_recompile("cat_v2.clsp", package_or_requirement=__name__)

CAT_MOD_HASH = CAT_MOD.get_tree_hash()
