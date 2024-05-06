import pygame
from typing import Any

from JsonLoader import JsonLoader
from Enum import PointRatio2d, Point2d


class TextBox(pygame.sprite.Sprite):
    def __init__(self, size: PointRatio2d | Point2d, position: PointRatio2d | Point2d,  color: pygame.color.Color, text: str) -> None:
        super().__init__()

        config: dict[str, Any] = JsonLoader.load("config.json")

        jetbrains_mono: pygame.font.Font = pygame.font.Font(pygame.font.match_font(pygame.font.get_fonts()[-1]), 12)

        self.image: pygame.Surface = jetbrains_mono.render("text", True, (255, 0, 0))

        if type(size[0]) == float:
            pass
            # self.image = pygame.transform.scale(self.image, (int(size[0] * config["size"][0]), int(size[1] * config["size"][1])))
            # self.image = pygame.Surface((int(size[0] * config["size"][0]), int(size[1] * config["size"][1])))
        elif type(size[0]) == int:
            pass
            # self.image = pygame.Surface(size)
            # self.image = pygame.transform.scale(self.image, size)
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

