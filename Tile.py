from pygame import sprite
from typing import Any
from random import randint

from JsonLoader import JsonLoader
from data import init
init()
from data import data


class Tile(sprite.Sprite):
    def __init__(self, ID: str) -> None:  # TODO: make a Tile
        super().__init__()

        data_path: dict[str, Any] = data["Tile"][ID]

        images: list[str] = data_path["image_path"]

        self.image_path: str = images[randint(0, len(images) - 1)]


Tile("grass")
