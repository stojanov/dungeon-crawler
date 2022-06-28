import pygame

class sprite(object):
    def __init__(self, image, size):
        self.image = pygame.transform.scale(image, size)
        self.flipped_vertical = False
        self.flipped_horizontal = False
    
    def flip_vertically(self):
        self.flipped_vertical = not self.flipped_vertical
        self.image = pygame.transform.flip(self.image, False, True)
        
    def flip_horizontally(self):
        self.flipped_horizontal = not self.flipped_horizontal
        self.image = pygame.transform.flip(self.image, True, False)
        
    def render(self, display, pos):
        display.blit(self.image, pos)