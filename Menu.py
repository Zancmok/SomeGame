import pygame

from Renderer import Renderer


class Menu:
    def __init__(self, renderer: Renderer, window: pygame.Surface) -> None:
        self.renderer: Renderer = renderer
        self.window = window

    def tick(self, events: list[pygame.event.Event]) -> None:
        pass

