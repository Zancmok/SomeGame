from _types import *

from Base import Base


class TileGroup(Base):
    walkable: bool  # if you can walk on tiles
    swimable: bool  # if you can swim on tiles
    passable: bool  # if you can fly over tiles
