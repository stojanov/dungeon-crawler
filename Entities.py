import enum

from SpriteAnimation import sprite_animation
from SpriteRenderer import sprite_renderer

class entity_type(enum.IntEnum):
    none = -1
    player = 0
    skeleton1 = 1
    hpflask = 2
    manaflask = 3
    
class entity(object):
    def __init__(self, type, sprites, duration):
        self.type = type
        self.sprite = sprite_renderer(sprite_animation(duration, sprites))
        self.pos = (0, 0)
        self.gridpos = (0, 0)
        
    def spawn(self, pos):
        self.pos = pos
        self.sprite.reset_sprites()
        
    def set_pos(self, pos):
        self.pos = pos
        
    def should_die(self):
        return False
    
    def update(self, dt):
        self.sprite.update(dt)
    
    def render(self, display, offset):
        newpos = (self.pos[0] + offset[0], self.pos[1] + offset[1])
        self.sprite.render(display, newpos)