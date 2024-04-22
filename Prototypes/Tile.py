from Base import Base
from TileGroup import TileGroup


class Tile(Base):
    image_path: str  # the path of the tiles image
    tile_group: TileGroup  # the group of the tile
