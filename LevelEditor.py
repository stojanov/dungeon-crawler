import random, sys, time, pygame, json, math, uuid, copy
import pygame
from pygame.locals import *
from Entities import entity, entity_type
from Level import level, block_type
from GameConsts import *
from LevelLoader import load_level, save_level
from Enemies import skeleton_1
from Utils import pixel_to_grid

TextColor = Color(247, 227, 50)

class current_state(object):
    def __init__(self):
        self.sprite = None
        self.type = block_type.none
        self.entity_type = entity_type.none

class edcamera(object):
    def __init__(self):
        self.offset = (0, 0)
    
    def move(self, pos):
        self.offset = (self.offset[0] + pos[0], self.offset[1] + pos[1])

class mouse_state(object):
    def __init__(self):
        self.m1drag = False
        self.m2drag = False
        self.m3drag = False

def get_sprite_state(newblock, entt = entity_type.none):
    from GameSprites import MapBlocks, Sprites
    
    if newblock == block_type.player:
        return Sprites["player"][0]
    
    if newblock == block_type.wall:
        return MapBlocks["blank_wall"][0]
        
    if newblock == block_type.floor:
        return MapBlocks["floor"][0]
        
    if newblock == block_type.entity:
        if entt == entity_type.skeleton1:
            return Sprites["skeleton_1"][0]
        if entt == entity_type.hpflask:
            return Sprites["hpflask"][0]
        if entt == entity_type.manaflask:
            return Sprites["manaflask"][0]
        
    return MapBlocks["blank_wall"][0]

def update_state(state, newblock, entt = entity_type.none):
    state.sprite = get_sprite_state(newblock, entt)
    state.type = newblock
    state.entity_type = entt

def place_object(lvl, state, gridpos):
    if state.type == block_type.entity and state.entity_type == entity_type.player:
        lvl.playerspawn = gridpos
        
    lvl.put_block(state.sprite, gridpos, state.type, state.entity_type)

def draw_text(display, pos, text, font):
    display.blit(font.render(text, True, TextColor), pos)

def draw_active_item(display, font, state):
    draw_text(display, (7, 7), "Active Item", font)
    state.sprite.render(display, (32, 32))

def main_editor(levelName):
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font("assets/Pixeboy.ttf", 32)
    display = pygame.display.set_mode(DisplaySize)
    
    state = current_state()
    mstate = mouse_state()
    cam = edcamera()
    window_clear = pygame.Rect(0, 0, DisplaySize[0], DisplaySize[1])
    
    fpsClock = pygame.time.Clock()
    dt = 0.016

    loadedLevel = load_level(levelName)
    
    lvl = None
    if not loadedLevel:
        lvl = level(BlockSize)
    else:
        lvl = loadedLevel[1]
        for entt in loadedLevel[2]:
            sprite = get_sprite_state(entt.type, entt.ent_type)
            lvl.put_block(sprite, entt.pos, entt.type, entt.ent_type)
    
    prevmousepos = (0, 0)
    mousepos = (0, 0)
    
    update_state(state, block_type.floor)
    
    gridworldpos = (0, 0)
    dragedBlocks = {}
    
    removingBlocks = False
    removingEnt = False
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mstate.m1drag = True
                    
                if event.button == 2:
                    mstate.m2drag = True
                    
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    mstate.m1drag = False
                    
                    if len(dragedBlocks) > 0:
                        dragedBlocks.clear()
                    else:
                        place_object(lvl, state, gridworldpos)
                    
                    #lvl.update_sprites()
                    
                if event.button == 2:
                    mstate.m2drag = False

            if event.type == MOUSEMOTION:
                prevmousepos = mousepos
                mousepos = pygame.mouse.get_pos()
                
                if mstate.m2drag:                    
                    mdiff = (mousepos[0] - prevmousepos[0], mousepos[1] - prevmousepos[1])
                    cam.move(mdiff)

                gridworldpos = pixel_to_grid((mousepos[0] - cam.offset[0], mousepos[1] - cam.offset[1]))

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                if event.key == K_0:
                    update_state(state, block_type.entity, entity_type.player)
                    
                if event.key == K_SPACE:
                    lvl.update_map_sprites()    
                
                if event.key == K_F1:
                    save_level(lvl, levelName)
                    print("Level Saved " + levelName)
                    
                if event.key == K_1:
                    update_state(state, block_type.floor)
                
                if event.key == K_2:
                    update_state(state, block_type.wall)
                    
                if event.key == K_3:
                    update_state(state, block_type.entity, entity_type.skeleton1)
                    
                if event.key == K_9:
                    update_state(state, block_type.entity, entity_type.hpflask)
                    
                if event.key == K_8:
                    update_state(state, block_type.entity, entity_type.manaflask)
                    
                if event.key == K_c:
                    removingBlocks = True
                
                if event.key == K_x:
                    removingEnt = True
                    
            if event.type == KEYUP:
                if event.key == K_c:
                    removingBlocks = False
                    
                if event.key == K_x:
                    removingEnt = False
        
        
        pygame.draw.rect(display, ClearColor, window_clear)

        if dt > 0.1:
            dt = 0.02
        
        lvl.render(display, cam.offset, True)
        
        if mstate.m1drag:
            if gridworldpos not in dragedBlocks:
                place_object(lvl, state, gridworldpos)
                dragedBlocks[gridworldpos] = True
                
        if removingBlocks:
            lvl.remove_block(gridworldpos)
            
        if removingEnt:
            lvl.remove_entity(gridworldpos)

        draw_active_item(display, font, state)
        
        if lvl.player_spawn != None:
            from GameSprites import Sprites
            pos = (lvl.player_spawn[0] * BlockSize[0] + cam.offset[0], lvl.player_spawn[1] * BlockSize[1] + cam.offset[1])
            Sprites["player"][0].render(display, pos)
        
        pygame.display.flip()
        dt = fpsClock.tick(Fps) / 1000