import pygame
from typing import Any

from Menu import Menu
from Renderer import Renderer
from Layer import Layer
from JsonLoader import JsonLoader
from Sprite.Background import Background
from Sprite.SpriteBox import SpriteBox
from Sprite.TextBox import TextBox


class MainMenu(Menu):
    def __init__(self, renderer: Renderer, window: pygame.Surface) -> None:
        super().__init__(renderer, window)

        self.backgroundLayer: Layer = Layer(0, window)
        self.menuBackLayer: Layer = Layer(1, window)
        self.menuFrontLayer: Layer = Layer(2, window)

        config: dict[str, Any] = JsonLoader.load("config.json")

        backgroundGroup: pygame.sprite.Group = pygame.sprite.Group()

        background: Background = Background("resources\\background.bmp", config["size"])

        backgroundGroup.add(background)  # noqa

        self.backgroundLayer.add_group(backgroundGroup)

        menuBackLayerGroup: pygame.sprite.Group = pygame.sprite.Group()

        menuBack: SpriteBox = SpriteBox((.3, .75), (.5, .5), pygame.color.Color(0, 0, 0))

        menuBackLayerGroup.add(menuBack) # noqa

        self.menuBackLayer.add_group(menuBackLayerGroup)

        menFrontLayerGroup: pygame.sprite.Group = pygame.sprite.Group()

        title: TextBox = TextBox((.3, .05), (.5, .15), pygame.color.Color(255, 255, 255), "SomeGame[Test]")

        menFrontLayerGroup.add(title)  # noqa

        self.menuFrontLayer.add_group(menFrontLayerGroup)

        renderer.add_layers([self.backgroundLayer, self.menuBackLayer, self.menuFrontLayer])

    def tick(self, events: list[pygame.event.Event]) -> None:
        pass
