#!env python
"""
A bouncing ball.

A ball is dropped under the a gravitation field oriented vertically (pointing down).

When the ball hits the ground, part of the energy is absorbed and not restituted.

Collision with the ground is managed by resetting the position to ground-level.
This prevents the ball from getting trapped (doesn't seem to happen in practice
but this is a risk and I don't want to deal with it here).

Collisions with the sides is fully elastic (no loss).

There is no drag force and no friction on the ground or sides.
"""
import pygame
from Vector import Vector2D

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
# screen = pygame.display.set_mode((res_x, res_y), pygame.FULLSCREEN)
screen = pygame.display.set_mode((res_x, res_y))

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
interrupt = False
while running:
    #update
    border(screen)
    position = position + velocity*delta_t
    velocity = velocity + acceleration*delta_t
    if position.y > res_y:
        position.y = res_y
        velocity.y = -.7*velocity.y

    if position.x < 0:
        velocity.x = -velocity.x
        position.x = 0
    elif position.x > res_x:
        velocity.x = -velocity.x
        position.x = res_x

    screen.fill(BLACK)
    draw(screen, position)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key in (pygame.K_q, pygame.K_ESCAPE):
                running = False
            if key == pygame.K_b:
                interrupt = True
            if key == pygame.K_SPACE:
                position = Vector2D(10, 100)
                velocity = Vector2D(30, 0)
