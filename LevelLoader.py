import json
from tabnanny import check

from EntitiesContainer import entity_container

from GameConsts import LEVEL_DIR, BlockSize 
from Utils import read_json, check_keys, write_json
from Entities import entity_type
from Block import block_type
from Level import level, mapblock_data

def load_level(name):
    newmap = level(BlockSize)
    
    mapdata = read_json(LEVEL_DIR + name + ".json")
    
    if not mapdata:
        return None
    
    if not check_keys(mapdata, ["playerspawn", "blocks", "entities"]):
        return None
    
    playerspawn = (mapdata["playerspawn"]["x"], mapdata["playerspawn"]["y"])
    
    for block in mapdata["blocks"]:
        if not check_keys(block, ["x", "y", "block_type", "ent_type"]):
            continue
        
        pos = (block["x"], block["y"])
        bType = block_type(block["block_type"])
        eType = entity_type(block["ent_type"])
        
        newmap.put_generator_block(pos, bType, eType)
        
    entities = []
    for ent in mapdata["entities"]:
        if not check_keys(ent, ["x", "y", "block_type", "ent_type"]):
            continue
        
        pos = (ent["x"], ent["y"])
        bType = block_type(ent["block_type"])
        eType = entity_type(ent["ent_type"])
        
        entities.append(mapblock_data(None, pos, bType, eType))
        
    newmap.generate(playerspawn)
    return [playerspawn, newmap, entities]

def save_level(lvl, name):
    base = {
            "playerspawn": {
                "x": lvl.player_spawn[0],
                "y": lvl.player_spawn[1],
            }
        }

    blocks = []
    for key, val in lvl.map.items():
        block = {
            "x": key[0],
            "y": key[1],
            "block_type": int(val.type),
            "ent_type": int(val.ent_type)
        }
        
        blocks.append(block)
        
    entities = []
    for key, val in lvl.entities.items():
        entity = {
            "x": key[0],
            "y": key[1],
            "block_type": int(val.type),
            "ent_type": int(val.ent_type)
        }
        
        entities.append(entity)
        
    base["blocks"] = blocks
    base["entities"] = entities
    
    return write_json(LEVEL_DIR + name + ".json", base)