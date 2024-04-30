import pygame
from typing import Any

from Menu import Menu
from Renderer import Renderer
from Layer import Layer
from JsonLoader import JsonLoader
from Sprite.Background import Background


class MainMenu(Menu):
    def __init__(self, renderer: Renderer, window: pygame.Surface) -> None:
        super().__init__(renderer, window)

        self.backgroundLayer: Layer = Layer(0, window)
        self.mainLayer: Layer = Layer(1, window)

        backgroundGroup: pygame.sprite.Group = pygame.sprite.Group()

        config: dict[str, Any] = JsonLoader.load("config.json")

        background: Background = Background("resources\\background.bmp", config["size"])

        backgroundGroup.add(background)  # noqa

        self.backgroundLayer.add_group(backgroundGroup)

        renderer.add_layers([self.backgroundLayer, self.mainLayer])

    def tick(self, events: list[pygame.event.Event]) -> None:
        pass
