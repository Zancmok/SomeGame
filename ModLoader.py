from os import listdir
from copy import deepcopy
from typing import Any

from Logger import Logger
from Enum import Enum, ModId
from JsonLoader import JsonLoader


class ModLoader:
    def __init__(self, mod_directory_path: str) -> None:
        self.mod_directory_path: str = mod_directory_path

        self.logger: Logger = Logger(
            "ModLoader",
            [Enum.ConsoleColor.Purple],
            [Enum.ConsoleColor.Blue, Enum.ConsoleColor.NotBold, Enum.ConsoleColor.NotItalic,
             Enum.ConsoleColor.NotUnderline]
        )

        self.logger.log("Mod Loader Started!")

        dependencies: list[tuple[str, list[str]]] = []
        for mod in listdir(mod_directory_path):
            mod_path: str = f"{mod_directory_path}\\{mod}"

            data: dict = JsonLoader.load(f"{mod_path}\\info.json")

            dependencies.append((data["mod_id"], data["dependencies"]))

            self.load_mod(mod_path)

        self.logger.log("Generating Mod Loading Queue!")
        mod_queue: list[ModId] = self.generate_dependency_tree(dependencies)
        self.logger.log("Mod Queue Generated!")

        for mod in mod_queue:
            self.load_mod(f"{self.mod_directory_path}\\{mod}")

    def generate_dependency_tree(self, mods: list[tuple[ModId, list[ModId]]]) -> list[ModId]:  # TODO: Fix the generation itself, see log for info
        out: list[str] = []

        def inner(_mods: list[tuple[ModId, list[ModId]]], _out: list[ModId]) -> None:
            if not _mods:
                return

            popables: list[int] = []

            for i, mod in enumerate(_mods):
                if len(mod[1]) == 0:
                    popables.append(i)

                for inner_mod in _mods:
                    for j, dependency in enumerate(inner_mod[1]):
                        if dependency == mod[0]:
                            inner_mod[1].pop(j)

            for i in popables[::-1]:
                out.append(_mods[i][0])
                _mods.pop(i)

            inner(_mods, out)

        inner(deepcopy(mods), out)

        return out

    def load_mod(self, mod_path: str) -> None:
        self.logger.log(f"Loading Mod: {mod_path}!")

        data: dict[str, Any] = JsonLoader.load(f"{mod_path}\\info.json")
