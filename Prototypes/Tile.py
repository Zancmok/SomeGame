from _types import *

from Base import Base
from TileGroup import TileGroup


class Tile(Base):
    image_path: str  # the path of the tiles image
    tile_group: pID[TileGroup]  # the group of the tile(grass_1 and grass_2 are both grass, so their group is grass)
