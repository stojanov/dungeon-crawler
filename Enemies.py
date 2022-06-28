from Block import block_type
from Entities import entity, entity_type
from Pathfinding import path_dijkstra_nodes, path_find_best_point
from Utils import dist, pixel_to_grid

SKELETON_ANIM_DUR = 1
SKELETON_MOVEMENT_VEL = 100
SKELETON_1_HP = 100
SKELETON_1_DMG = 50

class skeleton_1(entity):
    def __init__(self):
        from GameSprites import Sprites
        super().__init__(entity_type.skeleton1, Sprites["skeleton_1"], SKELETON_ANIM_DUR)
        self.dir = (0, 0)
        self.gridpos = (0, 0)
        self.vel = (0, 0)
        self.grid = None
        self.hp = SKELETON_1_HP
    
    def do_dmg(self, dmg):
        self.hp -= dmg
    
    def attack(self):
        return SKELETON_1_DMG
    
    def should_die(self):
        return False

    def move(self, dir):
        self.dir = dir

    def update(self, dt):
        super().update(dt)
        self.gridpos = pixel_to_grid(self.pos)
        
        velX = self.dir[0] * SKELETON_MOVEMENT_VEL * dt
        velY = self.dir[1] * SKELETON_MOVEMENT_VEL * dt
        
        self.pos = (self.pos[0] + velX, self.pos[1] + velY)
        self.dir = (0, 0)
        