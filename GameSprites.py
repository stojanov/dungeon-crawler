from tkinter import Image
from GameConsts import *
from Spritesheet import spritesheet
from Sprite import sprite
import pygame

dungeonsheet = spritesheet('assets/Dungeon_Tileset.png', ImageBlockSize)
playersheet = spritesheet('assets/Player.png', ImageBlockSize)
firespell_sheet = spritesheet('assets/Fire_Spell.png', ImageBlockSize)
skeleton_sheet = spritesheet('assets/Skeleton.png', ImageBlockSize)
hpflask = spritesheet('assets/flask_1.png', ImageBlockSize)
manaflask = spritesheet('assets/flask_2.png', ImageBlockSize)
main_bg = spritesheet('assets/Bg.png', (1920, 1080))
main_buttons = spritesheet('assets/Buttons.png', (200, 80))

StartingScreen = {
    "bg": sprite(main_bg.image_at_block((0, 0)), (1280, 720)),
    "play_normal": sprite(main_buttons.image_at_block((0, 0)), MainMenuButtonSize),
    "play_selected": sprite(main_buttons.image_at_block((0, 1)), MainMenuButtonSize),
    "tutorial_normal": sprite(main_buttons.image_at_block((0, 2)), MainMenuButtonSize),
    "tutorial_selected": sprite(main_buttons.image_at_block((0, 3)), MainMenuButtonSize)
}

Fonts = {
    "mainfont": pygame.font.Font("assets/Pixeboy.ttf", 32)
}

Sprites = {
    "player": [
        sprite(playersheet.image_at_block((0, 0)), BlockSize),
        sprite(playersheet.image_at_block((1, 0)), BlockSize),
        sprite(playersheet.image_at_block((2, 0)), BlockSize),
        sprite(playersheet.image_at_block((3, 0)), BlockSize)
    ],
    "firespell": [
        sprite(firespell_sheet.image_at((0, 0, 16, 16)), BlockSize),
        sprite(firespell_sheet.image_at((16, 0, 21, 16)), BlockSize),
        sprite(firespell_sheet.image_at((31, 0, 16, 16)), BlockSize),
        sprite(firespell_sheet.image_at((52, 0, 16, 16)), BlockSize)  
    ],
    "skeleton_1": [
        sprite(skeleton_sheet.image_at_block((0, 0)), BlockSize),
        sprite(skeleton_sheet.image_at_block((1, 0)), BlockSize),
        sprite(skeleton_sheet.image_at_block((2, 0)), BlockSize),
        sprite(skeleton_sheet.image_at_block((3, 0)), BlockSize)
    ],
    "hpflask": [
        sprite(hpflask.image_at_block((0, 0)), BlockSize),
        sprite(hpflask.image_at_block((1, 0)), BlockSize),
        sprite(hpflask.image_at_block((2, 0)), BlockSize),
        sprite(hpflask.image_at_block((3, 0)), BlockSize)
    ],
    "manaflask": [
        sprite(manaflask.image_at_block((0, 0)), BlockSize),
        sprite(manaflask.image_at_block((1, 0)), BlockSize),
        sprite(manaflask.image_at_block((2, 0)), BlockSize),
        sprite(manaflask.image_at_block((3, 0)), BlockSize)
    ]
}

MapBlocks = {
    "blank_wall": [
        sprite(dungeonsheet.image_at_block((8, 7)), BlockSize),  
    ],
    "top_wall": [
        sprite(dungeonsheet.image_at_block((1, 0)), BlockSize),
        sprite(dungeonsheet.image_at_block((2, 0)), BlockSize),
        sprite(dungeonsheet.image_at_block((3, 0)), BlockSize),
        sprite(dungeonsheet.image_at_block((4, 0)), BlockSize),
    ],
    "bott_wall": [
        sprite(dungeonsheet.image_at_block((1, 4)), BlockSize),
        sprite(dungeonsheet.image_at_block((2, 4)), BlockSize),
        sprite(dungeonsheet.image_at_block((3, 4)), BlockSize),
        sprite(dungeonsheet.image_at_block((4, 4)), BlockSize),
    ],
    "left_wall": [
        sprite(dungeonsheet.image_at_block((0, 0)), BlockSize),
        sprite(dungeonsheet.image_at_block((0, 1)), BlockSize),
        sprite(dungeonsheet.image_at_block((0, 2)), BlockSize),
        sprite(dungeonsheet.image_at_block((0, 3)), BlockSize),
    ],
    "right_wall": [
        sprite(dungeonsheet.image_at_block((5, 0)), BlockSize),
        sprite(dungeonsheet.image_at_block((5, 1)), BlockSize),
        sprite(dungeonsheet.image_at_block((5, 2)), BlockSize),
        sprite(dungeonsheet.image_at_block((5, 3)), BlockSize),
    ],
    
    "floor": [
        sprite(dungeonsheet.image_at_block((7, 0)), BlockSize),
        sprite(dungeonsheet.image_at_block((8, 0)), BlockSize),
        sprite(dungeonsheet.image_at_block((6, 0)), BlockSize),
        sprite(dungeonsheet.image_at_block((9, 0)), BlockSize),
    ],
    "corners": {
        "bott_left": [
            sprite(dungeonsheet.image_at_block((0, 4)), BlockSize),
        ],
        "bott_right": [
            sprite(dungeonsheet.image_at_block((5, 4)), BlockSize),
        ],
    }
}