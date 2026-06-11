# C
import pygame as pg

C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0),
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
# E

ENTITY_DAMAGE = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Level1Bg4' : 0,
    'Level1Bg5' : 0,
    'Level1Bg6' : 0,
    'Level2Bg0' : 0,
    'Level2Bg1' : 0,
    'Level2Bg2' : 0,
    'Level2Bg3' : 0,
    'Level2Bg4' : 0,
    'Player1' : 1,
    'Player1Shot' : 25,
    'Player2' : 1,
    'Player2Shot' : 25,
    'Enemy1' : 1,
    'Enemy1Shot' : 20,
    'Enemy2' : 1,
    'Enemy2Shot' : 25
}

ENTITY_SCORE = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Level1Bg4' : 0,
    'Level1Bg5' : 0,
    'Level1Bg6' : 0,
    'Player1' : 0,
    'Player1Shot' : 0,
    'Player2' : 0,
    'Player2Shot' : 0,
    'Enemy1' : 100,
    'Enemy1Shot' : 0,
    'Enemy2' : 150,
    'Enemy2Shot' : 0
}

ENTITY_SHOT_DELAY = {
    'Player1' : 20,
    'Player2' : 20,
    'Enemy1'  : 100,
    'Enemy2'  : 90
}

EVENT_ENEMY = pg.USEREVENT +1

ENTITY_HEALTH = {
    'Level1Bg0' : 999,
    'Level1Bg1' : 999,
    'Level1Bg2' : 999,
    'Level1Bg3' : 999,
    'Level1Bg4' : 999,
    'Level1Bg5' : 999,
    'Level1Bg6' : 999,
    'Player1' : 300,
    'Player1Shot' : 1,
    'Player2' : 300,
    'Player2Shot' : 1,
    'Enemy1' : 50,
    'Enemy1Shot' : 1,
    'Enemy2' : 60,
    'Enemy2Shot' : 1,
}

ENTITY_SPEED = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 1,
    'Level1Bg2' : 2,
    'Level1Bg3' : 3,
    'Level1Bg4' : 4,
    'Level1Bg5' : 5,
    'Level1Bg6' : 6,
    'Player1'   : 3,
    'Player1Shot' : 4,
    'Player2'   : 3,
    'Player2Shot' : 4,
    'Enemy1'    : 1,
    'Enemy1Shot': 4,
    'Enemy2'    : 2,
    'Enemy2Shot': 4
}


# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT'
               )

# P
PLAYER_KEY_UP = {'Player1': pg.K_w,
                 'Player2': pg.K_UP}
PLAYER_KEY_DOWN = {'Player1': pg.K_s,
                 'Player2': pg.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pg.K_a,
                   'Player2': pg.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pg.K_d,
                    'Player2': pg.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pg.K_t,
                    'Player2': pg.K_KP0}

# S
SPAWN_TIME = 4000


# w
WIN_WIDTH = 576
WIN_HEIGHT = 324
