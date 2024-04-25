from typing import Any
from JsonLoader import JsonLoader

data: dict[str, Any] = {}


def init() -> None:
    global data
    data = JsonLoader.load("data.json")
