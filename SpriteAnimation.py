
class sprite_animation(object):
    def __init__(self, duration, frames):
        self.duration = duration
        self.idx = 0
        self.timestep = 0
        self.frames = frames
        self.frameduration = self.duration / len(frames)
        self.looped = False
        
    def reset(self):
        self.looped = False
        self.timestep = 0
        self.idx = 0
        
    def has_looped(self):
        return self.looped
        
    def update(self, dt):
        if self.timestep > self.frameduration:
            self.timestep = self.timestep - self.frameduration
            if self.idx >= len(self.frames) - 1:
                self.idx = 0
                self.looped = True
            else:
                self.idx += 1
        else:
            self.timestep += dt
            self.looped = False
            
            
    def get_active_frame(self):
        return self.frames[self.idx]