import pygame
from pygame.locals import *
import cmath

WIDTH = 500
HALFWIDTH = int(WIDTH/2)

BG = 0xffffff
FG = (0x000000, 0x0000ff)

GAP = 10
RES = 0.1

FN = lambda z : 200000/z**2

MAX = HALFWIDTH
MIN = -MAX

ZOOMX = 1
ZOOMY = ZOOMX

DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))

def main(argv):
    bg = get_bg(argv, BG)
    fg = get_fg(argv, FG, bg)
    DISPLAY.fill(bg)
    for i in range(MIN, MAX+1, GAP):
        print(f"Im(z) = {i} ...")
        proc_line(i, True, fg)
        print(f"Re(z) = {i} ...")
        proc_line(i, False, fg)
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
        try:
            w = fn(complex(z[0],z[1]))
        except:
            continue
        else:
            rtn.append((w.real, w.imag))
    return rtn

def to_pygame_coords(line):
    return [ (HALFWIDTH + int(ZOOMX*x), HALFWIDTH - int(ZOOMY*y))
            for x, y in line ]

def line(k, _min, _max, is_h, res):
    rtn = []
    i = _min
    while i <= _max:
        rtn.append( (is_h * i + (not is_h) * k, (not is_h) * i + is_h * k) )
        i += res
    return rtn

def proc_line(i, is_h, fg):
    line1 = line( i, -HALFWIDTH, HALFWIDTH, is_h, RES)
    line2 = transform_line(line1, FN)
    line3 = to_pygame_coords(line2)
    colour = fg[is_h]
    try:
        pygame.draw.lines( DISPLAY, colour, False, line3)
    except:
        print("failed")

def get_fg(argv, fg_def, bg):
    if "-m" in argv:
        i = inv_clr(bg)
        return (i, i)
    else:
        if "-i" in argv:
            return [inv_clr(i) for i in fg_def]
        else:
            return fg_def

def get_bg(argv, bg_def):
    if "-i" in argv:
        return inv_clr(bg_def)
    else:
        return bg_def

def inv_clr(h):
    return 0xffffff - h

import sys
main(sys.argv)
