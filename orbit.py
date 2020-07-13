#!env python

from Vector import *

import pygame
from pygame.locals import *


#Colors
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (127, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

def draw(screen, vector, size=10, color=RED):
    pygame.draw.rect(screen, color, ((vector.x-size/2, vector.y-size/2),(size, size)))


res_x = 1024
res_y = 768
pygame.init()
screen = pygame.display.set_mode((res_x, res_y), pygame.FULLSCREEN)

sun = Vector2D(res_x/2, res_y/2)
position = Vector2D(res_x/2, res_y/4)
velocity = Vector2D(50, 0)
acceleration = Vector2D(0, 0)
delta_t = .1

running = True
while running:
    #update
    acceleration = sun-position
    acceleration.norm = 20
    velocity = velocity + acceleration*delta_t
    position = position + velocity*delta_t

    screen.fill(BLACK)
    draw(screen, position, color=BLUE)
    draw(screen, sun, color=YELLOW)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key in (pygame.K_q, pygame.K_ESCAPE):
                running = False
