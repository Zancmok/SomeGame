import pygame

from Enum import Point2d, Enum
from Logger import Logger
from Renderer import Renderer
from Game import Game


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

        self.game: Game = Game(self.renderer, self.screen)

        self.running: bool = True

        while self.running:
            events: list[pygame.event.Event] = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.game.tick(events)

            self.renderer.render()

            pygame.display.flip()

            self.clock.tick(60)
