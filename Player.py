import enum
from pygame import math

from SpriteRenderer import sprite_renderer
from SpriteAnimation import sprite_animation
from Utils import pixel_to_grid

PLAYER_VEL = 130
PLAYER_FRICTION = 128
PLAYER_ANIMATION_SPEED = 0.8
PLAYER_HEALTH = 100
PLAYER_MANA = 100
PLAYER_MANA_REC = 10

class player(object):
    def __init__(self, sprites, pos = (0, 0)):
        self.pos = pos
        self.velX = 0
        self.velY = 0
        self.move_direction = (0, 0)
        self.last_pos = pos
        self.sprite = sprite_renderer(sprite_animation(PLAYER_ANIMATION_SPEED, sprites))
        self.ismoving = False
        self.health = PLAYER_HEALTH
        self.mana = PLAYER_MANA
        
    def facing_left(self):
        return self.sprite.facing_left
        
    def do_dmg(self, dmg):
        self.health -= dmg
    
    def max_health(self):
        return self.health == PLAYER_HEALTH
    
    def max_mana(self):
        return self.mana == PLAYER_MANA
    
    def add_mana(self, mana):
        if self.mana + mana > PLAYER_MANA:
            limit = self.mana + mana - PLAYER_MANA
            self.mana += mana - limit
        else:
            self.mana += mana
    
    def add_hp(self, hp):
        if self.health + hp > PLAYER_HEALTH:
            limit = self.health + hp - PLAYER_HEALTH
            self.health += hp - limit
        else:
            self.health += hp
        
    def flipleft(self):
        self.sprite.face_left()
        
    def flipright(self):
        self.sprite.face_right()
        
    def set_pos(self, pos):
        self.pos = pos
        
    def store_pos(self):
        self.last_pos = self.pos
        
    def return_pos(self):
        self.pos = self.last_pos
        
    def move(self, dir):
        self.velX = PLAYER_VEL
        self.velY = PLAYER_VEL
        self.move_direction = dir
        
    def stop(self):
        self.velX = 0
        self.velY = 0

    def update(self, dt):
        if self.velX < 0:
            self.velX = 0
        if self.velY < 0:
            self.velY = 0
        
        moveVelX = self.velX * self.move_direction[0] * dt
        moveVelY = self.velY * self.move_direction[1] * dt
        
        self.pos = (self.pos[0] + moveVelX, self.pos[1] + moveVelY)
        
        self.velX -= PLAYER_FRICTION * dt
        self.velY -= PLAYER_FRICTION * dt
        
        if self.pos != self.last_pos:
            self.ismoving = True
            self.sprite.update(dt)
        else:
            self.ismoving = False
            
        if self.mana < 100:
            self.mana = self.mana + PLAYER_MANA_REC * dt
        
    def render(self, display, offset):
        newpos = (self.pos[0] + offset[0], self.pos[1] + offset[1])
        self.sprite.render(display, newpos)