import pygame

from Enum import Point2d


class Window:
    def __init__(self, size: Point2d, title: str) -> None:
        self.size: Point2d = size
        self.title: str = title

        self.screen: pygame.surface.Surface = pygame.display.set_mode(self.size)
        self.clock: pygame.time.Clock = pygame.time.Clock()

        pygame.display.set_caption(title)

        self.running: bool = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

            self.clock.tick(60)
