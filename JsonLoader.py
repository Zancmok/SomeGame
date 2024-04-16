from typing import Any
import json


class JsonLoader:
    def __init__(self) -> None:
        pass

    def load(self, path: str) -> Any:
        file: Any = open(path)

        out: Any = json.load(file)

        file.close()

        self.log(f"Loaded: {path}")

        return out

    def log(self, msg: str) -> None:
        pass

