import pygame

from Enum import Point2d, Enum
from Logger import Logger
from Renderer import Renderer
from Layer import Layer
from Tile import Tile


class Window:
    def __init__(self, size: Point2d, title: str) -> None:
        self.logger: Logger = Logger(
            "Window",
            [Enum.ConsoleColor.Yellow],
            [Enum.ConsoleColor.Blue, Enum.ConsoleColor.NotUnderline, Enum.ConsoleColor.NotBold, Enum.ConsoleColor.NotItalic]
        )

        self.logger.log("Started!")

        self.size: Point2d = size
        self.title: str = title

        self.screen: pygame.surface.Surface = pygame.display.set_mode(self.size)
        self.clock: pygame.time.Clock = pygame.time.Clock()

        pygame.display.set_caption(title)

        self.renderer: Renderer = Renderer()

        tileLayer: Layer = Layer(0, self.screen)

        tileGroup: pygame.sprite.Group = pygame.sprite.Group()

        tileLayer.add_group(tileGroup)

        tileGroup.add(
            Tile("grass", (0, 0))
        )

        self.renderer.add_layer(tileLayer)

        self.running: bool = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.renderer.render()

            pygame.display.flip()

            self.clock.tick(60)
