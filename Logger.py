from Enum import ConsoleColor


class Logger:
    def __init__(self, serviceName: str, prefix: list[ConsoleColor], suffix: list[ConsoleColor]) -> None:
        self.serviceName: str = serviceName

        self.prefix: str = ""
        for color in prefix:
            self.prefix += str(color)

        self.suffix: str = ""
        for color in suffix:
            self.suffix += str(color)

    def log(self, *args):
        print(self.prefix, end="")
        print(f"[{self.serviceName}]: ", end="")

        for i in args:
            print(i, end="")

        print(self.suffix)
