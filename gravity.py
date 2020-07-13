#!env python

import pygame
from Vector import Vector2D

# Physics constants
EARTH_M = 5.9722*pow(10, 24) # earth mass in kg
SUN_M = 1.989*pow(10, 30) # sun mass in kg
INITIAL_EARTH_VELOCITY = 30300 # average earth orbital speed in m/s
ONE_AU = 149597870700 # mean sun-earth distance: one Astronomical Unit in meters
G = 6.67430*pow(10, -11) # gravitational constant

#Colors
GRAY = (127, 127, 127)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_RED = (127, 0 ,0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


def F(m1, m2, r):
    return G*m1*m2/pow(r,2)

def A(f, m):
    return f/m

def draw(screen, vector, size=10, color=RED):
    pygame.draw.rect(screen, color, ((vector.x-size/2, vector.y-size/2), (size, size)))


def main() -> None:
    res_x = 1024
    res_y = 768
    pygame.init()
    # screen = pygame.display.set_mode((res_x, res_y), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((res_x, res_y))

    screen_center = Vector2D(res_x/2, res_y/2)
    scale = res_y/(2.5*ONE_AU)

    sun = Vector2D(0, 0)
    earth = Vector2D(0, ONE_AU)
    velocity = Vector2D(INITIAL_EARTH_VELOCITY, 0)

    acceleration = Vector2D(0, 0)
    delta_t = 3.65*86400 # in s. The delta_time for each frame.

    running = True

    screen.fill(BLACK)
    while running:
        #update
        force = F(EARTH_M, SUN_M, (earth-sun).norm)
        accel_norm = A(force, EARTH_M)
        acceleration = sun-earth
        acceleration.norm = accel_norm
        velocity = velocity + acceleration*delta_t
        earth = earth + velocity*delta_t

        # screen.fill(BLACK)
        draw(screen, earth*scale+screen_center, size=3, color=BLUE)
        draw(screen, sun*scale+screen_center, color=YELLOW)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False

if __name__ == "__main__":
    main()
