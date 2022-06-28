import sys
import pygame
from pygame.locals import *
from Block import block_type
from Collision import collides_size
from Entities import entity_type
from EntitiesContainer import entity_container
from GameConsts import BlockSize
from LevelLoader import load_level

from FireSpell import firespell
from Enemies import skeleton_1
from Overlay import overlay
from Pathfinding import path_dijkstra_nodes, path_find_best_point
from Pickables import hpflask, manaflask, pickable
from Utils import dist, pixel_to_grid

def get_entity(type):
    if type == entity_type.skeleton1:
        return skeleton_1()
    
    if type == entity_type.hpflask:
        return hpflask()
    
    if type == entity_type.manaflask:
        return manaflask()

def drawblock(display, pos, offset):
    pos = (pos[0] * BlockSize[0] + offset[0], pos[1] * BlockSize[1] + offset[1])
    rect = pygame.Rect(pos[0], pos[1], BlockSize[0], BlockSize[1])
    pygame.draw.rect(display, (255, 0, 0), rect)

class game(object):
    def __init__(self, blocksize):
        self.map = None
        self.spawnable = entity_container()
        self.attacks = entity_container()
        self.overlay = overlay()
        self.ent_map = {}
        self.blocksize = blocksize
        self.player = None
        self.camera = None
        self.last_player_pos = None
        self.path = []
    
    def init_camera(self, camera):
        self.camera = camera
    
    def init_player(self, player):
        self.player = player
        self.overlay.attach_player(player)
    
    def spawn_player(self, mappos):
        pos = (mappos[0] * self.blocksize[0], mappos[1] * self.blocksize[1])
        self.player.set_pos(pos)
        self.last_player_pos = pixel_to_grid(pos)
    
    def load_level(self, name):
        lvl = load_level(name)
        
        if lvl == None:
            print("Error loading level: " + name)
            pygame.quit()
            sys.exit()
        
        self.map = lvl[1]
        self.spawn_player(lvl[0])
        self.generate_entities(lvl[2])
    
    def generate_entities(self, entities):
        for ent in entities:
            if ent.type != block_type.entity:
                continue
            inst = get_entity(ent.ent_type)
            worldpos = (ent.pos[0] * BlockSize[0], ent.pos[1] * BlockSize[1])
            inst.spawn(worldpos)
            self.spawnable.add(inst)
            self.ent_map[ent.pos] = inst
    
    def onevent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.key == K_SPACE:
                spell = firespell(True)
            
                if self.player.mana < spell.cost:
                    return
            
                if self.player.facing_left():
                    pos = (self.player.pos[0] - BlockSize[0], self.player.pos[1])
                    spell.sprite.face_left()
                else:
                    pos = (self.player.pos[0] + BlockSize[0], self.player.pos[1])
                    spell.sprite.face_right()

                spell.spawn(pos)
                self.spawnable.add(spell)
                
                self.player.mana = self.player.mana - spell.cost
    
    def update(self, dt, pressed_keys):
        pMoveX = 0
        pMoveY = 0

        if pressed_keys[K_w]:
            pMoveY = -1
        if pressed_keys[K_a]:
            pMoveX = -1
            self.player.flipleft()
        if pressed_keys[K_s]:
            pMoveY = 1
        if pressed_keys[K_d]:
            pMoveX = 1
            self.player.flipright()
        
        if self.map.collides(self.player.pos, block_type.wall):
            self.player.return_pos()
            
        if pMoveX != 0 or pMoveY != 0:
            self.player.move((pMoveX, pMoveY))
        
        self.camera.update((self.player.pos[0] + 32, self.player.pos[1] + 32), dt)

        ent = self.spawnable.entities()
        removedents = []
        
        p_gridpos = pixel_to_grid(self.player.pos)
        
        nodes = {}
        
        if p_gridpos != self.last_player_pos:
            nodes = path_dijkstra_nodes(p_gridpos, self.map.map, lambda block: block.type == block_type.wall, 5)
        
        for i in range(self.spawnable.count()):
            e = ent[i]
            e.update(dt)
            
            if e.type == entity_type.skeleton1:
                skeleton_dist = dist(self.player.pos, e.pos)
                if skeleton_dist > BlockSize[0] and e.gridpos in nodes:
                    bestpoint = path_find_best_point(nodes, e.gridpos)
                    dir = (bestpoint[0] - e.gridpos[0], bestpoint[1] - e.gridpos[1])
                    e.move(dir)
                elif skeleton_dist < (BlockSize[0] + BlockSize[0] / 3):
                    self.player.do_dmg(e.attack() * dt)
                    

            if isinstance(e, pickable):
                if dist(self.player.pos, e.pos) <= BlockSize[0]:        
                    if e.type == entity_type.hpflask:
                        if not self.player.max_health():
                            self.player.add_hp(e.hp)
                            e.destroy()
                    
                    if e.type == entity_type.manaflask:
                        if not self.player.max_mana():
                            self.player.add_mana(e.mana)
                            e.destroy()


            if e.should_die():
                removedents.append(i)

        for idx in removedents:
            self.spawnable.remove(idx)

        self.player.store_pos()
        self.player.update(dt)
        self.map.update(dt)
    
    def render(self, display):
        offset = self.camera.getoffset()
        self.map.render(display, offset, False)
        ent = self.spawnable.entities() 
        
        for i in range(self.spawnable.count()):
            ent[i].render(display, offset)
        
        for pos in self.path:
            drawblock(display, pos, offset)
        
        self.player.render(display, offset)
        self.overlay.render(display)
        