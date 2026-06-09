# C
import pygame as pg

COLOR_ORANGE = (255,128,0)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_YELLOW = (255,255,0)
# E
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
    'Player2'   : 3,
    'Enemy1'    : 1,
    'Enemy2'    : 2
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
