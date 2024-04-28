import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from typing import Any

from Logger import Logger
from Enum import Enum
from ModLoader import ModLoader
from JsonLoader import JsonLoader


def main() -> None:
    logger: Logger = Logger("main.py",
                            [Enum.ConsoleColor.Green],
                            [Enum.ConsoleColor.Blue, Enum.ConsoleColor.NotBold, Enum.ConsoleColor.NotItalic, Enum.ConsoleColor.NotUnderline])

    logger.log("Started!")

    pygame.init()

    logger.log("Pygame Initialized!")

    config: dict[str, Any] = JsonLoader.load("config.json")

    modLoader: ModLoader = ModLoader(config["mod_directory"])

    logger.log("Started Creating Window!")

    from Window import Window

    window: Window = Window(config["size"], config["title"])

    logger.log("Application Ended!")


if __name__ == '__main__':
    main()
