type Point2d = tuple[int, int]  # a set of 2 scalars, representing sizes, positions...
type PointRatio2d = tuple[float, float]  # a set of 2 floats, both having value from 0 to 1
type ModId = str  # the identity/name of a mod


class ConsoleColor:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value


class Enum:
    class ConsoleColor:
        Black: ConsoleColor = ConsoleColor("\033[30m")
        Red: ConsoleColor = ConsoleColor("\033[31m")
        Green: ConsoleColor = ConsoleColor("\033[32m")
        Yellow: ConsoleColor = ConsoleColor("\033[33m")
        Blue: ConsoleColor = ConsoleColor("\033[34m")
        Purple: ConsoleColor = ConsoleColor("\033[35m")
        Cyan: ConsoleColor = ConsoleColor("\033[36m")
        White: ConsoleColor = ConsoleColor("\033[37m")
        Bold: ConsoleColor = ConsoleColor("\033[1m")
        NotBold: ConsoleColor = ConsoleColor("\033[22m")
        Italic: ConsoleColor = ConsoleColor("\033[3m")
        NotItalic: ConsoleColor = ConsoleColor("\033[23m")
        Underline: ConsoleColor = ConsoleColor("\033[4m")
        NotUnderline: ConsoleColor = ConsoleColor("\033[24m")
