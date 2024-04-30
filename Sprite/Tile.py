from pygame import sprite
import pygame
from typing import Any
from random import randint
from Enum import Point2d

from JsonLoader import JsonLoader
from data import get_data


class Tile(sprite.Sprite):
    def __init__(self, ID: str, position: Point2d) -> None:  # TODO: make a Tile
        super().__init__()

        data_path: dict[str, Any] = get_data()["Tile"][ID]

        images: list[str] = data_path["image_path"]

        image_path: str = images[randint(0, len(images) - 1)]

        self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(image_path), (128, 128))
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = position

    def update(self) -> None:
        pass  # on tick
