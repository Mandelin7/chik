from __future__ import annotations

from typing import Any

from chik.types.blockchain_format.program import Program


def json_to_chiklisp(json_data: Any) -> Any:
    list_for_chiklisp = []
    if isinstance(json_data, list):
        for value in json_data:
            list_for_chiklisp.append(json_to_chiklisp(value))
    else:
        if isinstance(json_data, dict):
            for key, value in json_data:
                list_for_chiklisp.append((key, json_to_chiklisp(value)))
        else:
            list_for_chiklisp = json_data
    return Program.to(list_for_chiklisp)
