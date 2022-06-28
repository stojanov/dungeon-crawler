import enum
import pygame
    
# blocks from level
class block_type(enum.IntEnum):
    any = -2
    none = -1
    player = 0
    wall = 1
    floor = 2
    entity = 3
