from os import listdir

from Logger import Logger
from Enum import Enum
from TreeNode import TreeNode
from JsonLoader import JsonLoader


class ModLoader:
    def __init__(self, mod_directory_path: str) -> None:
        self.logger: Logger = Logger(
            "ModLoader",
            [Enum.ConsoleColor.Purple],
            [Enum.ConsoleColor.Blue, Enum.ConsoleColor.NotBold, Enum.ConsoleColor.NotItalic, Enum.ConsoleColor.NotUnderline]
        )

        self.jsonLoader: JsonLoader = JsonLoader()

        self.logger.log("Mod Loader Started!")

        for mod in listdir(mod_directory_path):
            mod_path: str = f"{mod_directory_path}\\{mod}"

            data: dict = self.jsonLoader.load(f"{mod_path}\\info.json")

            print(data)

            self.load_mod(mod_path)

    def generate_dependency_tree(self, mods: list[tuple[str, list[str]]]) -> TreeNode:
        pass

    def load_mod(self, mod_path: str) -> None:
        print(listdir(mod_path))
