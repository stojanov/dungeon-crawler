from Entities import entity
from SpriteAnimation import sprite_animation
from SpriteRenderer import sprite_renderer

import enum

class spell_type(enum.Enum):
    player = 0
    enemy = 1

class spell(entity):
    def __init__(self, sprites, animation_dur, type, pos = (0, 0)):
        super().__init__(type, sprites , animation_dur)

    def should_die(self):
        return self.sprite.animation.has_looped()