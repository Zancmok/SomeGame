from typing import Any, Self


class TreeNode:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.left: Self | None = None
        self.right: Self | None = None
        self.parent: Self | None = None

    def __str__(self) -> str:
        return f"TreeNode<{self.value}>"

    def __repr__(self) -> str:
        return f"TreeNode<{self.value}:[{self.left}|{self.right}]>"
