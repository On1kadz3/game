import math
#game settings

SCREEN_WIDTH        =   1200
SCREEN_HEIGHT       =   800
SCREEN_HALF_WIDTH   =   SCREEN_WIDTH   // 2
SCREEN_HALF_HEIGHT  =   SCREEN_HEIGHT  // 2

#player settings

player_position = (SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT)

player_speed = 5

player_angle = 0

FIELD_OF_VIEW = math.pi / 3

HALF_FIELD_OF_VIEW =FIELD_OF_VIEW /2

NUM_RAYS_IN_FIELD_OF_VIEW = 90

DELTA_ANGLE = FIELD_OF_VIEW / NUM_RAYS_IN_FIELD_OF_VIEW

MAX_DEPTH = 200

FPS = 40
#map

TILE = 90
#TILE = 60

#mini map

MAP_SCALE = 5

MAP_TILE = TILE // MAP_SCALE

MAP_POSITION = (0, SCREEN_HEIGHT - SCREEN_HEIGHT // MAP_SCALE)
#colors

BLACK   = (0,0,0)

DARKGRAY = (110,110,110)

WHITE   = (255,255,255)

RED     = (220,0,0)

ORANGE  = (180,140,0)

YELLOW  = (0,120,120)

GREEN   = (0,220,0)

BLUE    = (0,0,220)

PURPLE  = (120,0,120)



#ray_casting

DISTANCE_TO_WALL = NUM_RAYS_IN_FIELD_OF_VIEW /2 * math.tan(HALF_FIELD_OF_VIEW)

PROJECT_COEFFICIENT = DISTANCE_TO_WALL * TILE

SCALE = SCREEN_WIDTH // NUM_RAYS_IN_FIELD_OF_VIEW


# FPS settings

FPS_POSITION =(SCREEN_WIDTH - 65, 5)
