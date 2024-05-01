import pygame
from typing import Any

from JsonLoader import JsonLoader
from Enum import PointRatio2d, Point2d


class SpriteBox(pygame.sprite.Sprite):
    def __init__(self, size: PointRatio2d | Point2d, position: PointRatio2d | Point2d,  color: pygame.color.Color) -> None:
        super().__init__()

        config: dict[str, Any] = JsonLoader.load("config.json")

        self.image: pygame.Surface

        if type(size[0]) == float:
            self.image = pygame.Surface((int(size[0] * config["size"][0]), int(size[1] * config["size"][1])))
        elif type(size[0]) == int:
            self.image = pygame.Surface(size)
        else:
            raise TypeError

        self.rect: pygame.Rect = self.image.get_rect()

        if type(size[0]) == float:
            self.rect.center = (position[0] * config["size"][0], position[1] * config["size"][1])
        elif type(size[0]) == int:
            self.rect.center = position
        else:
            raise TypeError

        self.image.fill(color)


