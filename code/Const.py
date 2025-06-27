# constantes
import pygame
from pygame.examples.grid import WINDOW_WIDTH

# C
C_BLUE = (17, 40, 237)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 254, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)
C_RED = (237, 28, 36)

# E
ENTITY_DAMAGE = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Level2Bg0' : 0,
    'Level2Bg1' : 0,
    'Level2Bg2' : 0,
    'Level2Bg3' : 0,
    'Level2Bg4' : 0,
    'Level3Bg0' : 0,
    'Level3Bg1' : 0,
    'Level3Bg2' : 0,
    'Level3Bg3' : 0,
    'Player1' : 1,
    'Player1Shoot' : 25,
    'Player2' : 1,
    'Player2Shoot' : 25,
    'Enemy1' : 1/2,
    'Enemy1Shoot' : 20,
    'Enemy2' : 1/2,
    'Enemy2Shoot' : 15,
    'Enemy3' : 1/2,
    'Enemy3Shoot' : 15}

ENTITY_HEALTH = {
    'Level1Bg0' : 999,
    'Level1Bg1' : 999,
    'Level1Bg2' : 999,
    'Level1Bg3' : 999,
    'Level2Bg0' : 999,
    'Level2Bg1' : 999,
    'Level2Bg2' : 999,
    'Level2Bg3' : 999,
    'Level2Bg4' : 999,
    'Level3Bg0' : 999,
    'Level3Bg1' : 999,
    'Level3Bg2' : 999,
    'Level3Bg3' : 999,
    'Player1' : 200,
    'Player1Shoot' : 1,
    'Player2' : 200,
    'Player2Shoot' : 1,
    'Enemy1' : 50,
    'Enemy1Shoot' : 1,
    'Enemy2' : 75,
    'Enemy2Shoot' : 1,
    'Enemy3' : 75,
    'Enemy3Shoot' : 1}

ENTITY_SCORE = {
    'Level1Bg0' : 0,
    'Level1Bg1' : 0,
    'Level1Bg2' : 0,
    'Level1Bg3' : 0,
    'Level2Bg0' : 0,
    'Level2Bg1' : 0,
    'Level2Bg2' : 0,
    'Level2Bg3' : 0,
    'Level2Bg4' : 0,
    'Level3Bg0' : 0,
    'Level3Bg1' : 0,
    'Level3Bg2' : 0,
    'Level3Bg3' : 0,
    'Player1' : 0,
    'Player1Shoot' : 0,
    'Player2' : 0,
    'Player2Shoot' : 0,
    'Enemy1' : 100,
    'Enemy1Shoot' : 0,
    'Enemy2' : 120,
    'Enemy2Shoot' : 0,
    'Enemy3' : 120,
    'Enemy3Shoot' : 0}

ENTITY_SHOOT_DELAY = {
    'Player1': 25,
    'Player2': 25,
    'Enemy1': 75,
    'Enemy2': 70,
    'Enemy3': 60}

ENTITY_SPEED = {
    'Level1Bg0' : 1,
    'Level1Bg1' : 3,
    'Level1Bg2' : 0,
    'Level1Bg3' : 1,
    'Level2Bg0' : 0,
    'Level2Bg1' : 3,
    'Level2Bg2' : 0,
    'Level2Bg3' : 1,
    'Level2Bg4' : 2,
    'Level3Bg0' : 0,
    'Level3Bg1' : 3,
    'Level3Bg2' : 1,
    'Level3Bg3' : 3,
    'Player1' : 4,
    'Player1Shoot' : 4,
    'Player2' : 4,
    'Player2Shoot' : 4,
    'Enemy1' : 3,
    'Enemy1Shoot': 8,
    'Enemy2' : 4,
    'Enemy2Shoot': 8,
    'Enemy3' : 2,
    'Enemy3Shoot': 6}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP, 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN, 'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT, 'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT, 'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL, 'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 1000

# T
TIMEOUT_LEVEL = 20000 #20s
TIMEOUT_STEP = 100 #100ms

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH/2, WIN_HEIGHT/2 - 10),
             'TitleScore': (WIN_WIDTH/2, 50),
             'EnterName': (WIN_WIDTH/2, WIN_HEIGHT/2 + 30),
             'Label': (251, 90),
             'Name': (WIN_WIDTH/2, WIN_HEIGHT/2 + 50),
             0: (WIN_WIDTH/2, 110),
             1: (WIN_WIDTH/2, 130),
             2: (WIN_WIDTH/2, 150),
             3: (WIN_WIDTH/2, 170),
             4: (WIN_WIDTH/2, 190),
             5: (WIN_WIDTH/2, 210),
             6: (WIN_WIDTH/2, 230),
             7: (WIN_WIDTH/2, 250),
             8: (WIN_WIDTH/2, 270),
             9: (WIN_WIDTH/2, 290)}