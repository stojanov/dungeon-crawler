import random, sys, time, pygame, json, math, uuid

from pygame.locals import *
from Block import block_type
from Camera import camera
from Game import game
from GameStatesController import game_states_controller, game_states
from LevelLoader import load_level
from Player import player
from Spell import spell
from Sprite import sprite
from Spritesheet import spritesheet
from FireSpell import firespell
from GameConsts import *
from LevelEditor import main_editor
from MainMenu import main_menu
import enum

def main_game(level):
    pygame.init()
    display = pygame.display.set_mode(DisplaySize)
    
    from GameSprites import Sprites
    
    window_clear = pygame.Rect(0, 0, DisplaySize[0], DisplaySize[1])
    
    c = camera(DisplaySize, (300, 300))

    p = player(Sprites["player"])

    dungeon_crawler = game(BlockSize)
    gameState = game_states_controller()

    menu = main_menu(gameState)
    dungeon_crawler.init_player(p)
    dungeon_crawler.init_camera(c)
    dungeon_crawler.load_level(level)

    fpsClock = pygame.time.Clock()
    dt = 0.016
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if gameState.state == game_states.main_menu:
                menu.onevent(event)
                
            if gameState.state == game_states.game:
                dungeon_crawler.onevent(event)
        
        pygame.draw.rect(display, ClearColor, window_clear)
        
        if dt > 0.1:
            dt = 0.02
        
        if gameState.state == game_states.game:
            dungeon_crawler.update(dt, pygame.key.get_pressed())
            dungeon_crawler.render(display)
        
        if gameState.state == game_states.main_menu:
            menu.update(dt, pygame.key.get_pressed())
            menu.render(display)
       
        pygame.display.flip()
        dt = fpsClock.tick(Fps) / 1000

if __name__ == '__main__':
    args = sys.argv[1:] 
    
    editorLaunch = False
    level = ""
    
    for arg in args:
        if arg == "editor":
            editorLaunch = True
        else:
            level = arg
            
            
            
    if editorLaunch:
        main_editor(level)
    else:
        main_game(level if len(level) > 0 else "test")