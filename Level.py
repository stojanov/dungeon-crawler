import enum
import json
import math
import random

from Block import block_type
from Collision import collides
from Entities import entity_type
from Utils import pixel_to_grid

class mapblock_data(object):
    def __init__(self, sprite, pos, type, eType = entity_type.none):
        self.sprite = sprite
        self.pos = pos
        self.type = type
        self.ent_type = eType

# Main grid and world
class level(object):
    def __init__(self, blocksize):
        self.blocksize = blocksize
        self.map = {}
        self.entities = {}
        self.player_spawn = None
        self.generated = False
    
    def remove_block(self, mappos):
        if mappos in self.map:
            self.map.pop(mappos)
    
    def remove_entity(self, mappos):
        if mappos in self.entities:
            self.entities.pop(mappos)
    
    def put_generator_block(self, mappos, type, eType = entity_type.none):
        pos = (mappos[0] * self.blocksize[0], mappos[1] * self.blocksize[1])
        
        if type == block_type.entity:
            self.entities[mappos] = mapblock_data(None, mappos, type, eType)
        else:
            self.map[mappos] = mapblock_data(None, pos, type, eType)
    
    def update_map_sprites(self):
        from GameSprites import MapBlocks
        
        for key, val in self.map.items():
            if val.type == block_type.floor:
                val.sprite = random.choice(MapBlocks["floor"])
                continue
            
            neighbours = [
                (key[0] - 1, key[1]),     # 0 LEFT
                (key[0] + 1, key[1]),     # 1 RIGHT
                (key[0], key[1] - 1),     # 2 UP
                (key[0], key[1] + 1),     # 3 DOWN
                (key[0] - 1, key[1] - 1),  # 4 TOP LEFT CORNER
                (key[0] + 1, key[1] - 1),  # 5 TOP RIGHT CORNER
                (key[0] - 1, key[1] + 1),  # 6 BOTT LEFT CORNER
                (key[0] + 1, key[1] + 1),  # 7 BOTT RIGHT CORNER
            ]
            
            for i in range(len(neighbours)):
                point = neighbours[i]

                if point not in self.map:
                    neighbours[i] = None
                    continue
                
                neighbours[i] = self.map[point].type
                
            if neighbours[1] == block_type.wall and neighbours[0] == block_type.wall:
                val.sprite = random.choice(MapBlocks["blank_wall"])
            
            if neighbours[0] == block_type.floor:
                val.sprite = random.choice(MapBlocks["right_wall"])
            if neighbours[1] == block_type.floor:
                val.sprite = random.choice(MapBlocks["left_wall"])
            if neighbours[2] == block_type.floor:
                val.sprite = random.choice(MapBlocks["bott_wall"])
            if neighbours[3] == block_type.floor:
                val.sprite = random.choice(MapBlocks["top_wall"])
  
            if neighbours[0] == block_type.wall and neighbours[3] == block_type.wall and neighbours[6] == block_type.floor:
                 val.sprite = random.choice(MapBlocks["right_wall"])
                
            if neighbours[0] == block_type.wall and neighbours[2] == block_type.wall and neighbours[4] == block_type.floor:
                val.sprite = random.choice(MapBlocks["corners"]["bott_right"])
                
            if neighbours[1] == block_type.wall and neighbours[3] == block_type.wall and neighbours[7] == block_type.floor:
                val.sprite = random.choice(MapBlocks["left_wall"])
                
            if neighbours[1] == block_type.wall and neighbours[2] == block_type.wall and neighbours[5] == block_type.floor:
                val.sprite = random.choice(MapBlocks["corners"]["bott_left"])
    
    def generate(self, playerspawn):
        self.generated = True
        self.player_spawn = playerspawn
        self.update_map_sprites()
    
    def put_block_at_pos(self, block, pos, type, eType = entity_type.none):
        self.put_block(block, pixel_to_grid(pos), type, eType)
    
    def put_block(self, block, mappos, type, eType = entity_type.none):
        pos = (mappos[0] * self.blocksize[0], mappos[1] * self.blocksize[1])
        
        if type == block_type.entity:
            if eType == entity_type.player:
                self.player_spawn = mappos
                
            else:
                self.entities[mappos] = mapblock_data(block, pos, type, eType)
        else:
            self.map[mappos] = mapblock_data(block, pos, type, eType)
    
    def block_at(self, mappos):
        if not self.exists(mappos):
            return None
        return self.map[mappos]
    
    def block_at_pos(self, pos):
        return self.block_at(pixel_to_grid(pos))
    
    def exists(self, mappos):
        return mappos in self.map
    
    def block_count(self):
        return len(self.map)
    
    def collides(self, pos, bType):
        # Checks all the neighboring blocks to see if they collide with a given position
        collarr = [
            self.block_at_pos(pos), # check the current block
            self.block_at_pos((pos[0] + self.blocksize[0], pos[1])), # left block
            self.block_at_pos((pos[0] - self.blocksize[0], pos[1])), # right
            self.block_at_pos((pos[0], pos[1] + self.blocksize[0])), # bottom
            self.block_at_pos((pos[0], pos[1] - self.blocksize[0])), # top
            self.block_at_pos((pos[0] - self.blocksize[0], pos[1] - self.blocksize[0])), # top left
            self.block_at_pos((pos[0] + self.blocksize[0], pos[1] - self.blocksize[0])), # top right
            self.block_at_pos((pos[0] - self.blocksize[0], pos[1] + self.blocksize[0])), # bott left
            self.block_at_pos((pos[0] + self.blocksize[0], pos[1] + self.blocksize[0]))  # bott right
        ]
        
        for col_block in collarr:
            if col_block != None and col_block.type == bType and collides(pos, col_block.pos):
                return True
        
        return False
    
    def update(self, dt):
        return 0
    
    def render(self, display, offset, isEditor = False):
        for key, val in self.map.items():
            if val.sprite:
                val.sprite.render(display, (val.pos[0] + offset[0], val.pos[1] + offset[1]))
                
        if isEditor:
            for key, val in self.entities.items():
                if val.sprite:
                    val.sprite.render(display, (val.pos[0] + offset[0], val.pos[1] + offset[1]))