import pygame
from pygame.locals import *
import cmath

WIDTH = 500
BG = 0xffffff
FG = 0x000000

def main(argv):
    DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))
    DISPLAY.fill(BG)
    px = pygame.PixelArray(DISPLAY)

    MIN = -10
    MAX = 10
    STEP = 0.1

    # x^2 - x - 1 = 0
    PHI = 1.61803398875
    PHI2 = -0.61803398875

    a = MIN
    while a < MAX:
        b = MIN
        while b < MAX:
            w = complex(a, b)
            z = (PHI**w - PHI2**w) / (PHI - PHI2)
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
