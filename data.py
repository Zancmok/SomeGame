from typing import Any
from JsonLoader import JsonLoader

_data: dict[str, Any] = {}


def init() -> None:
    global _data
    _data = JsonLoader.load("data.json")


def get_data() -> dict[str, Any]:
    return _data
