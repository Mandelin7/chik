from __future__ import annotations

import random
from pathlib import Path
from typing import Tuple

from chik.consensus.blockchain import Blockchain
from chik.consensus.constants import ConsensusConstants
from chik.full_node.block_store import BlockStore
from chik.full_node.coin_store import CoinStore
from chik.util.db_wrapper import DBWrapper2


async def create_ram_blockchain(consensus_constants: ConsensusConstants) -> Tuple[DBWrapper2, Blockchain]:
    uri = f"file:db_{random.randint(0, 99999999)}?mode=memory&cache=shared"
    db_wrapper = await DBWrapper2.create(database=uri, uri=True, reader_count=1, db_version=2)
    block_store = await BlockStore.create(db_wrapper)
    coin_store = await CoinStore.create(db_wrapper)
    blockchain = await Blockchain.create(coin_store, block_store, consensus_constants, Path("."), 2)
    return db_wrapper, blockchain
