import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import json
from typing import Any

from Window import Window
from Logger import Logger
from Enum import Enum
from ModLoader import ModLoader


def main() -> None:
    logger: Logger = Logger("main.py",
                            [Enum.ConsoleColor.Green],
                            [Enum.ConsoleColor.Blue, Enum.ConsoleColor.NotBold, Enum.ConsoleColor.NotItalic, Enum.ConsoleColor.NotUnderline])

    logger.log("Started!")

    pygame.init()

    logger.log("Pygame Initialized!")

    config_file: Any = open("config.json")

    config: dict[str, Any] = json.load(config_file)

    config_file.close()

    modLoader: ModLoader = ModLoader(config["mod_directory"])

    logger.log("Started Creating Window!")

    window: Window = Window(config["size"], config["title"])

    logger.log("Application Ended!")


if __name__ == '__main__':
    main()
