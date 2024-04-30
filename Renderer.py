from Layer import Layer
from Logger import Logger
from Enum import Enum


class Renderer:
    def __init__(self) -> None:
        self.layers: list[Layer] = []
        self.logger: Logger = Logger("Renderer",
                                     [Enum.ConsoleColor.Red],
                                     [Enum.ConsoleColor.Blue, Enum.ConsoleColor.NotBold, Enum.ConsoleColor.NotItalic, Enum.ConsoleColor.NotUnderline])
        self.logger.log("Started!")

    def render(self) -> None:
        self.layers.sort(key=lambda x: x.index)

        for layer in self.layers:
            layer.render()

    def add_layer(self, layer: Layer) -> None:
        self.layers.append(layer)

    def add_layers(self, layers: list[Layer]) -> None:
        for layer in layers:
            self.add_layer(layer)
