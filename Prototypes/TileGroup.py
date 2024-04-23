from _types import *

from Base import Base
from TileType import TileType


class TileGroup(Base):
    tile_type: pID[TileType]  # the type of the tile, the tile group is(land, water...)
