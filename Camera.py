
from Collision import collides_point, collides_size

class camera(object):
    def __init__(self, display_size, bounds):
        self.display_size = display_size
        self.screenpoint = (display_size[0] / 2, display_size[1] / 2)
        self.bounds = bounds
        self.bhalf = (bounds[0] / 2, bounds[1] / 2)
        self.offset = (0, 0)

    def update(self, pos, dt):
        camerapos = (self.screenpoint[0] + self.offset[0], self.screenpoint[1] + self.offset[1])
        bound_point = (camerapos[0] - self.bhalf[0], camerapos[1] - self.bhalf[1])
        
        if not collides_size(pos, (0,0), bound_point, self.bounds):
            ends = (bound_point[0] + self.bounds[0], bound_point[1] + self.bounds[1])
            
            offsetX = 0
            offsetY = 0
            
            if pos[0] > ends[0]:
                offsetX = pos[0] - ends[0]
            elif pos[0] < bound_point[0]:
                offsetX = pos[0] - bound_point[0]
            if pos[1] > ends[1]:
                offsetY = pos[1] - ends[1]
            elif pos[1] < bound_point[1]:
                offsetY = pos[1] - bound_point[1]
            
            self.offset = (self.offset[0] + offsetX, self.offset[1] + offsetY)

    def getoffset(self):
        return (-1 * self.offset[0], -1 * self.offset[1])
