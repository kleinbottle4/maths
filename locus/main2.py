import pygame
from pygame.locals import *
import cmath
import math

WIDTH = 100
HWIDTH = int(WIDTH/2)
GRID_SPACE = 10
SF = 10
MAX = int(HWIDTH/SF)
MIN = -MAX

BG = 0xffffff
FG = 0x000000
INK = 0xff0000

FILTER = lambda z : True
DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))

def main(argv):
    DISPLAY.fill(BG)
    pxarray = pygame.PixelArray(DISPLAY)
    pygame.display.update()
    for x in range(MIN,MAX):
        for y in range(MIN,MAX):
            z = complex(x,y)
            zx = int(SF*x + HWIDTH)
            zy = int(HWIDTH - SF*y)
            try:
                pxarray[zx, zy] = INK
            except Exception as e:
                print(e)
    pygame.display.update()
    del pxarray
    input()

import sys
main(sys.argv)
