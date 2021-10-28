import pygame
from pygame.locals import *
from cmath import *
from math import *
import cmath
import math

WIDTH = 1000
HWIDTH = int(WIDTH/2)
GRID_SPACE = 10
SF = 100
MAX = int(HWIDTH)
MIN = -MAX

BG = 0xffffff
FG = 0x000000
INK = 0x0000ff

E = 0.01

def approx(x, y, e):
    return y - e <= x <= y + e

# FILTER = lambda z : \
#         approx(phase(z-1)-phase(z+1), tau/12, E) \
#         or approx(phase(z-1)-phase(z+1), -5 * tau/12, E)
FILTER = lambda z : approx(abs(z-1), 1, 0.1)
DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))

def main(argv):
    DISPLAY.fill(BG)
    pxarray = pygame.PixelArray(DISPLAY)
    draw_grid_lines()
    pygame.display.update()
    debug = "-d" in argv
    for x in range(MIN,MAX):
        for y in range(MIN,MAX):
            z = complex(x/SF,y/SF)
            try:
                if FILTER(z):
                    px = int(x + HWIDTH)
                    py = int(HWIDTH - y)
                    pxarray[px, py] = INK
                    if debug:
                        print(z, end = ' : ')
                        print(px, py)
            except Exception as e:
                print('!!!', e)
    pygame.display.update()
    del pxarray
    input()

def draw_grid_lines():
    for i in range(0, WIDTH, GRID_SPACE):
        if i == HWIDTH:
            thickness = 2
        else:
            thickness = 1
        pygame.draw.line(DISPLAY, FG, (i, 0), (i, WIDTH), thickness)
        pygame.draw.line(DISPLAY, FG, (0, i), (WIDTH, i), thickness)

import sys
main(sys.argv)
