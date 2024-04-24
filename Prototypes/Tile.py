from _types import *

from Base import Base
from TileGroup import TileGroup


class Tile(Base):
    image_path: list[str]  # the path of the tiles image
    tile_group: ID[TileGroup]  # the group of the tile (examples: ground, water, void)
