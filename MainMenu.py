import pygame
from Collision import collides_point
from GameConsts import *

class button(object):
    def __init__(self, sNormal, sSelected, pos):
        self.normal = sNormal
        self.selected = sSelected
        self.pos = pos
        self.is_selected = False
        
        
    def update(self, dt, mouse_pos):
        if collides_point(mouse_pos, self.pos, MainMenuButtonSize):
            self.is_selected = True
        else:
            self.is_selected = False
    
    def render(self, display):
        if self.is_selected:
            self.selected.render(display, self.pos)
        else:
            self.normal.render(display, self.pos)


class main_menu(object):
    def __init__(self, gameState):
        from GameSprites import StartingScreen
        self.bg = StartingScreen["bg"]
        self.buttons = []
        self.gameState = gameState
        
        btn_x = (DisplaySize[0] / 2) - (MainMenuButtonSize[0] / 2)
        btn_y = (DisplaySize[1] / 2) - (MainMenuButtonSize[1] / 2)
        btn_y_offset = 50
        
        play = button(StartingScreen["play_normal"], StartingScreen["play_selected"], (btn_x, btn_y + btn_y_offset))   
        tutorial = button(StartingScreen["tutorial_normal"], StartingScreen["tutorial_selected"], (btn_x, btn_y + btn_y_offset + MainMenuButtonSize[1]))
        
        self.buttons.append(play)
        self.buttons.append(tutorial)
    
    def onevent(self, evt):
        if evt.type == MOUSEBUTTONDOWN:
                if self.buttons[0].is_selected:
                    self.gameState.switch_game()
    
    def update(self, dt, pressed_keys):
        for button in self.buttons:
            button.update(dt, pygame.mouse.get_pos())
    
    def render(self, display):
        self.bg.render(display, (0, 0))
        for button in self.buttons:
            button.render(display)
    