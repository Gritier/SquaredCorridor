import pygame as pg

#COSTANTS
WIDTH = 720
HEIGHT = 720
BASE_SIZE = 40

#ENUMS
ENUM_DIRECTIONS = {
    'left': [-1,0],
    'right': [1,0],
    'down': [0,1],
    'up': [0,-1]
}


#INITIALIZE GAME ENV
def init():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((WIDTH, HEIGHT))


#METHODS
def move(direction, pos):
    pos.x += movement_speed * dt * direction[0]
    pos.y += movement_speed * dt * direction[1]
