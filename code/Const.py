
import pygame as pg

# C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_YELLOW = (255, 255, 0),
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
ENTITY_DAMAGE = {
    'Level1Bg': 0,
    'Level2Bg': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 25,
    'HealthPill': 0,
    'DoubleShot': 0,
}

ENTITY_SCORE = {
    'Level1Bg': 0,
    'Level2Bg': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 150,
    'Enemy2Shot': 0,
    'HealthPill': 0,
    'DoubleShot': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
    'Enemy1': 100,
    'Enemy2': 90
}

EVENT_ENEMY = pg.USEREVENT + 1

EVENT_TIMEOUT = pg.USEREVENT + 2

ENTITY_HEALTH = {
    'Level1Bg': 999,
    'Level2Bg': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
    'HealthPill': 999,
    'DoubleShot': 999,
}

ENTITY_SPEED = {

    'Level1Bg': 1,
    'Level2Bg': 1,
    'Player1': 3,
    'Player1Shot': 4,
    'Player2': 3,
    'Player2Shot': 4,
    'Enemy1': 1,
    'Enemy1Shot': 4,
    'Enemy2': 2,
    'Enemy2Shot': 4,
    'HealthPill': 1,
    'DoubleShot': 1,
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

PLAYER_MAX_LIFE = {
    'Player1': 320,
    'Player2': 320,
}

# S
SPAWN_TIME = 2000


# T

TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 80000

# w
WIN_WIDTH = 560
WIN_HEIGHT = 960

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50 ),
             'EnterName': (WIN_WIDTH / 2, 80 ),
             'Label': (WIN_WIDTH / 2, 90 ),
             'Name': (WIN_WIDTH / 2, 110 ),
             0: (WIN_WIDTH / 2, 110 ),
             1: (WIN_WIDTH / 2, 130 ),
             2: (WIN_WIDTH / 2, 150 ),
             3: (WIN_WIDTH / 2, 170 ),
             4: (WIN_WIDTH / 2, 190 ),
             5: (WIN_WIDTH / 2, 210 ),
             6: (WIN_WIDTH / 2, 230 ),
             7: (WIN_WIDTH / 2, 250 ),
             8: (WIN_WIDTH / 2, 270 ),
             9: (WIN_WIDTH / 2, 290 ),
}
