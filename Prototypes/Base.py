from typing import Optional

from _types import *


class Base:
    id: str  # The unique prototype id of an object
    type: str  # Specifies the prototype it is
    order: Optional[str]  # The order in User Interfaces
