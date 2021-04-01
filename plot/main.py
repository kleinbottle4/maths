import pygame
from pygame.locals import *
import math
import cmath

WIDTH = 500
FPS   = 30
BG = 0x000000
FG = 0xffffff

def main(argv):
    DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))
    DISPLAY.fill(BG)
    px = pygame.PixelArray(DISPLAY)

    MIN = -50
    MAX = 50
    STEP = 0.5

    a = MIN
    while a < MAX:
        b = MIN
        while b < MAX:
            z = complex(a, b) ** 2
            print(str(z))
            x = int(z.real) + 250
            y = - int(z.imag) + 250
            if 0 <= x < 500 and 0 <= y < 500:
                px[x, y] = FG
                pygame.display.update()
            b += STEP
        a += STEP
    del px

    while True:
        if is_quit():
            return 0

def is_quit():
    return pygame.locals.QUIT in [e.type for e in pygame.event.get()]

if __name__ == '__main__':
    from sys import argv
    main(argv)
