from typing import Optional
import pygame

from Renderer import Renderer
from Menu import Menu
from MainMenu import MainMenu


class Game:
    def __init__(self, renderer: Renderer, window: pygame.Surface) -> None:
        self.renderer: Renderer = renderer
        self.current_menu: Optional[Menu] = MainMenu(renderer, window)

    def tick(self, events: list[pygame.event.Event]) -> None:
        if self.current_menu:
            self.current_menu.tick(events)
