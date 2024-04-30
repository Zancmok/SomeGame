import pygame
from Enum import Point2d


class Background(pygame.sprite.Sprite):
    def __init__(self, path: str, size: Point2d):
        super().__init__()

        self.image: pygame.Surface = pygame.transform.scale(pygame.image.load(path), size)
        self.rect: pygame.Rect = self.image.get_rect()
