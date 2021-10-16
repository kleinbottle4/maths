import pygame
from pygame.locals import *
import cmath
import math

WIDTH = 700
HWIDTH = int(WIDTH/2)
GRID_SPACE = 10
MAX = HWIDTH
MIN = -HWIDTH
SF = WIDTH/5

BG = 0xffffff
FG = 0x000000
INK = 0xff0000

def approx(x, y, e):
    return y - e <= x <= y + e

FILTER = lambda z : approx(cmath.phase(z-SF) - cmath.phase(z), 1, 0.01)
DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))

def main(argv):
    pxarray = pygame.PixelArray(DISPLAY)
    DISPLAY.fill(BG)
    pygame.display.update()
    draw_grid_lines()
    debug = "-d" in argv
    for x in range(MIN,MAX):
        if debug:
            print(x)
        for y in range(MIN,MAX):
            z = complex(x,y)
            try:
                if FILTER(z):
                    pxarray[x + HWIDTH, HWIDTH - y] = INK
            except Exception as e:
                print(e)
    pygame.display.update()
    del pxarray
    while True:
        if is_quit():
            return 0

def draw_grid_lines():
    for i in range(0, WIDTH, GRID_SPACE):
        if i == HWIDTH:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(DISPLAY, FG, (i, 0), (i, WIDTH), thickness)
        pygame.draw.line(DISPLAY, FG, (0, i), (WIDTH, i), thickness)

def is_quit():
    return pygame.locals.QUIT in [e.type for e in pygame.event.get()]

import sys
main(sys.argv)
