import pygame
from pygame import sprite


class Layer:
    def __init__(self, index: int, surface: pygame.Surface) -> None:
        self.index: int = index
        self.surface: pygame.Surface = surface
        self.groups: list[sprite.Group] = []

    def add_group(self, group: sprite.Group) -> None:
        self.groups.append(group)

    def get_groups(self) -> list[sprite.Group]:
        return self.groups

    def render(self) -> None:
        for group in self.groups:
            group.draw(self.surface)
