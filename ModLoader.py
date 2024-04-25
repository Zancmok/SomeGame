from os import listdir, system
from copy import deepcopy
from typing import Any

from Logger import Logger
from Enum import Enum, ModId
from JsonLoader import JsonLoader
import data as _data


class ModLoader:
    def __init__(self, mod_directory_path: str) -> None:
        self.mod_directory_path: str = mod_directory_path

        self.logger: Logger = Logger(
            "ModLoader",
            [Enum.ConsoleColor.Purple],
            [Enum.ConsoleColor.Blue, Enum.ConsoleColor.NotBold, Enum.ConsoleColor.NotItalic,
             Enum.ConsoleColor.NotUnderline]
        )

        self.logger.log("Started!")

        dependencies: list[tuple[str, list[str]]] = []
        for mod in listdir(mod_directory_path):
            mod_path: str = f"{mod_directory_path}\\{mod}"

            data: dict = JsonLoader.load(f"{mod_path}\\info.json")

            dependencies.append((data["mod_id"], data["dependencies"]))

        self.logger.log("Generating Mod Loading Queue!")
        mod_queue: list[ModId] = self.generate_dependency_tree(dependencies)
        self.logger.log("Mod Queue Generated!")

        luaBridgeInput: str = f"lua .\\LuaBridge.lua {mod_directory_path}"

        for i in mod_queue:
            luaBridgeInput += f" {i}"

        self.logger.log("Starting LuaBridge!")
        system(luaBridgeInput)
        self.logger.log("Finished LuaBridge!")

        self.logger.log("Initializing data.py!")
        _data.init()
        self.logger.log("Finished mod phase!")

    @staticmethod
    def generate_dependency_tree(mods: list[tuple[ModId, list[ModId]]]) -> list[ModId]:
        out: list[str] = []

        def inner(_mods: list[tuple[ModId, list[ModId]]], _out: list[ModId]) -> None:
            while _mods:

                popables: list[int] = []

                for i, mod in enumerate(_mods):
                    if not mod[1]:
                        _out.append(mod[0])
                        popables.append(i)
                        for _mod in _mods:
                            for j, inner_mod in enumerate(_mod[1]):
                                if inner_mod == mod[0]:
                                    _mod[1].pop(j)

                for i in popables[::-1]:
                    _mods.pop(i)

        inner(deepcopy(mods), out)

        return out
