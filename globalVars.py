# coding=UTF-8

# from globalVars import * : seulement des pseudo-constantes

etherIP = '127.0.0.1'
#etherIP = '192.168.1.3'
#etherIP = '192.168.1.5'
#etherIP = '192.168.1.6'

screen_size = [800,600]

top_left = [200,100]
bottom_left = [200,300]
top_right = [600,100]
bottom_right = [600,300]

score_pos = [550,40]
score2_pos = [259,40]

# X Y position on bottom left of each paddle (="flips")
ball_origin = [400,300,200]
text_pos = [300,500,200]
BALL_acc = 0.06
PADDLE_height = 100
PADDLE_width = 10
PADDLE3D_height = 100
PADDLE3D_width = 100
FACT3D = 2
FLIPS_lorigin = [10,300,0]
FLIPS_rorigin = [780,300,400]
flips_attraction = 0.007

xy_center = [screen_size[0]/2,screen_size[1]/2]

DEFAULT_SPOKES = range(0,359,60)
DEFAULT_PLAYER_EXPLODE_COLOR = 0xFFFF00
DEFAULT_SIDE_COUNT = 6
DREARRANGE_SIDES = .02


CRASH_SHAKE_MAX = 6
TDN_CRASH = 200

GAME_FS_QUIT = -1
GAME_FS_MENU = 0
GAME_FS_PLAY = 1
GAME_FS_LAUNCH = 2
GAME_FS_GAMEOVER = 3

BUMPERS_COLOR_YELLOW = 0xFFFF00
BUMPERS_COLOR_RED = 0xFF0000
BUMPERS_COLOR_BLACK = 0x000000
BUMPERS_SIZE_X = 60
BUMPERS_SIZE_Y = 110
BUMPERS_FORCE = 1.1

LASER_CENTER_X = 140
LASER_CENTER_Y = 8921
LASER_ZOOM_X = -21
LASER_ZOOM_Y = -15.5
LASER_SIZE_X = 32000
LASER_SIZE_Y = 32000

BALL_SPEED = 5
BALL_MAX = 4
BALL_SIZE_X = 3
BALL_SIZE_Y = 3
LASER_ANGLE = 0



GRAVITY = 0.0001

NO_BGM = False
#NO_BGM = True
