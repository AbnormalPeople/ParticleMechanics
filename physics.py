#!/Users/alexandre/opt/anaconda3/envs/Coding/bin/python

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

def draw(screen, vector, size=10):
    pygame.draw.rect(screen, RED, ((vector.x-size/2, vector.y-size/2),(size, size)))

res_x = 1024
res_y = 768
pygame.init()
screen = pygame.display.set_mode((res_x, res_y), pygame.FULLSCREEN)

def border(screen):
    pygame.draw.line(screen, RED, (0, 0), (res_x, 0), 1)
    pygame.draw.line(screen, RED, (0, 0), (0, res_y), 1)
    pygame.draw.line(screen, RED, (res_x, 0), (res_x, res_y), 1)
    pygame.draw.line(screen, RED, (0, res_y), (res_x, res_y), 1)


position = Vector2D(10, 100)
velocity = Vector2D(30, 0)
acceleration = Vector2D(0, 20)
delta_t = .1

running = True
while running:
    #update
    border(screen)
    position = position + velocity*delta_t
    velocity = velocity + acceleration*delta_t
    if position.y > res_y:
        position.y = res_y
        velocity.y = -.8*velocity.y

    if position.x < 0 or position.x > res_x:
        velocity.x = -velocity.x

    screen.fill(BLACK)
    draw(screen, position)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key in (pygame.K_q, pygame.K_ESCAPE):
                running = False

            if key == pygame.K_SPACE:
                position = Vector2D(10, 100)
                velocity = Vector2D(30, 0)
