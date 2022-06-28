import enum

class collision_dir(enum.Enum):
    top = 0,
    bott = 1,
    left = 2,
    right = 3
    
def collides(posa, posb, blocksize = (64, 64)):
    right = posa[0] + blocksize[0] > posb[0]
    left = posa[0] < posb[0] + blocksize[0]
    bott = posa[1] + blocksize[1] > posb[1]
    top = posa[1] < posb[1] + blocksize[1]
    
    return right and left and bott and top

def collides_size(posa, sizea, posb, sizeb):
    right = posa[0] + sizea[0] > posb[0]
    left = posa[0] < posb[0] + sizeb[0]
    bott = posa[1] + posa[1] > posb[1]
    top = posa[1] < posb[1] + sizea[1]
    
    return right and left and bott and top

def collides_point(pos, posb, size):
    right = pos[0] < posb[0] + size[0]
    left = pos[0] > posb[0]
    top = pos[1] > posb[1]
    bottom = pos[1] < posb[1] + size[1]
    
    return right and left and top and bottom