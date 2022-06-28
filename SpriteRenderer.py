

class sprite_renderer(object):
    def __init__(self, animation):
        self.animation = animation
        self.facing_left = False
        
    def face_left(self):
        self.facing_left = True
        
    def face_right(self):
        self.facing_left = False
        
    def reset_sprites(self):
        self.animation.reset()
        
    def facing_left(self):
        return self.facing_left
        
    def update(self, dt):
        self.animation.update(dt)
    
    def render(self, display, pos):
        sprite = self.animation.get_active_frame()
        if self.facing_left and not sprite.flipped_horizontal:
            sprite.flip_horizontally()
        if not self.facing_left and sprite.flipped_horizontal:
            sprite.flip_horizontally()
        sprite.render(display, pos)