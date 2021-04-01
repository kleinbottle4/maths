import pygame
from pygame.locals import *
import cmath

WIDTH = 500
HALFWIDTH = int(WIDTH/2)
BG = 0xffffff
FG = 0x000000

GAP = 1
RES = 1

FN = lambda z : z ** 2

MAX = 25
MIN = -MAX

ZOOMX = 1
ZOOMY = ZOOMX

DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))

def main():
    DISPLAY.fill(BG)
    for i in range(MIN, MAX, GAP):
        print(f"Im(z) = {i} ...")
        proc_line(i,False)
        print(f"Re(z) = {i} ...")
        proc_line(i,True)
        pygame.display.update()
        if is_quit(): return 0
    print('done')
    while True:
        if is_quit(): return 0

def is_quit():
    return pygame.locals.QUIT in [e.type for e in pygame.event.get()]

def transform_line(line, fn):
    rtn = []
    for z in line:
        w = fn(complex(z[0],z[1]))
        rtn.append((w.real, w.imag))
    return rtn

def to_pygame_coords(line):
    return [ (HALFWIDTH + int(ZOOMX*x), HALFWIDTH - int(ZOOMY*y))
            for x, y in line ]

def line(k, _min, _max, is_h, res):
    rtn = []
    i = _min
    while i <= _max:
        rtn.append( (is_h * i + (not is_h) * k, (not is_h) * i + is_h
            * k) )
        i += res
    return rtn

def proc_line(i, is_h):
    pygame.draw.lines( DISPLAY, FG, False,
            to_pygame_coords( transform_line(
                    line( i, -HALFWIDTH, HALFWIDTH, is_h, RES), FN)))

if __name__ == '__main__':
    main()
