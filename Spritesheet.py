import pygame

class spritesheet(object):
    def __init__(self, filename, blocksize):
        self.sheet = pygame.image.load(filename)#.convert_alpha()
        self.blocksize = blocksize
        
    def image_at_block(self, pos, colorkey = None):
        xStart = pos[0] * self.blocksize[0]
        yStart = pos[1] * self.blocksize[1]

        return self.image_at((xStart, yStart, self.blocksize[0], self.blocksize[1]), colorkey)
    
    def image_at_custom(self, pos, size, colorkey = None):
        xStart = pos[0] * self.blocksize[0]
        yStart = pos[1] * self.blocksize[1]
        
        return self.image_at((xStart, yStart, size[0], size[1]), colorkey)
    
    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey != None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image