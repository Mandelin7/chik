from __future__ import annotations

from typing import Generator, KeysView

SERVICES_FOR_GROUP = {
    "all": [
        "chik_harvester",
        "chik_timelord_launcher",
        "chik_timelord",
        "chik_farmer",
        "chik_full_node",
        "chik_wallet",
        "chik_data_layer",
        "chik_data_layer_http",
    ],
    # TODO: should this be `data_layer`?
    "data": ["chik_wallet", "chik_data_layer"],
    "data_layer_http": ["chik_data_layer_http"],
    "node": ["chik_full_node"],
    "harvester": ["chik_harvester"],
    "farmer": ["chik_harvester", "chik_farmer", "chik_full_node", "chik_wallet"],
    "farmer-no-wallet": ["chik_harvester", "chik_farmer", "chik_full_node"],
    "farmer-only": ["chik_farmer"],
    "timelord": ["chik_timelord_launcher", "chik_timelord", "chik_full_node"],
    "timelord-only": ["chik_timelord"],
    "timelord-launcher-only": ["chik_timelord_launcher"],
    "wallet": ["chik_wallet"],
    "introducer": ["chik_introducer"],
    "simulator": ["chik_full_node_simulator"],
    "crawler": ["chik_crawler"],
    "seeder": ["chik_crawler", "chik_seeder"],
    "seeder-only": ["chik_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
