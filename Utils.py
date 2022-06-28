import math
from os.path import exists
import json

from GameConsts import BlockSize

def check_keys(d, keys):
    for key in keys:
        if key not in d:
            return False
        
    return True

def read_json(filepath):
    if not exists(filepath):
        return False
    
    f = open(filepath, "r")
    
    data = json.loads(f.read())
    f.close()
    
    return data

def write_json(filepath, data):
    f = open(filepath, "w")
    
    f.write(json.dumps(data))
    
    f.close()

def pixel_to_grid(pos):
    x = math.floor(pos[0] / BlockSize[0])
    y = math.floor(pos[1] / BlockSize[1])
    
    return (x, y)

def dist(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    
    return math.sqrt(x * x + y * y)