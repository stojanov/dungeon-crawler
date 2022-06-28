HEALTH_CLR = (200, 0, 0)

class overlay(object):
    def __init__(self):
        from GameSprites import Fonts
        self.player = None
        self.font = Fonts["mainfont"]
        self.padding = 12
        self.font_size = 32
        
    def attach_player(self, player):
        self.player = player
        
    def draw_hp(self, display):
        s = "HP:   " + str(int(self.player.health))
        display.blit(self.font.render(s, True, HEALTH_CLR), (self.padding, self.padding))

    def draw_mana(self, display):
        s = "MANA: " + str(int(self.player.mana))
        display.blit(self.font.render(s, True, HEALTH_CLR), (self.padding, self.padding + self.font_size))
        
    def render(self, display):
        self.draw_hp(display)
        self.draw_mana(display)
