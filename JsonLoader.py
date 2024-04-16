from typing import Any
import json
from Logger import Logger
from Enum import Enum


class _JsonLoader:
    def __init__(self) -> None:
        self.logger: Logger = Logger(
            "JsonLoader",
            [Enum.ConsoleColor.Cyan],
            [Enum.ConsoleColor.Blue, Enum.ConsoleColor.NotBold, Enum.ConsoleColor.NotItalic,
             Enum.ConsoleColor.NotUnderline]
        )

    def load(self, path: str) -> Any:
        self.log(f"Loaded: '{path}'!")
        with open(path, 'r') as file:
            out: Any = json.load(file)

        return out

    def log(self, msg: str) -> None:
        self.logger.log(msg)


JsonLoader: _JsonLoader = _JsonLoader()
