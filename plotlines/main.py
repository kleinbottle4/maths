import pygame
from pygame.locals import *
import cmath

WIDTH = 601
HWIDTH = int(WIDTH/2)
LWIDTH = 2

BG = 0xffffff
FG = (0x000000, 0xff0000)
MG = 0xC0C0C0

MAX = HWIDTH
MIN = -HWIDTH

# defaults
GAP = "10"
RES = "1"

FN = "z"
MAT = "1 0 0 1"

DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))

def main(argv):
    bg  = get_bg(argv, BG)
    fg  = get_fg(argv, FG, bg)
    fn  = eval("lambda z : " + get_arg(argv, "-f", FN))
    mat = [float(i) for i in get_arg(argv, "-m", MAT).split()]
    gap = int  (get_arg(argv, "-g", GAP))
    res = float(get_arg(argv, "-r", RES))
    zoom= float(get_arg(argv, '-z', WIDTH / (10 * int(GAP))))
    orig= '-O' not in argv
    DISPLAY.fill(bg)
    if orig:
        for i in range(MIN, MAX+1, gap):
            proc_line(i, lambda z : z, (1, 0, 0, 1), False, (MG,MG), WIDTH - 2, zoom)
            proc_line(i, lambda z : z, (1, 0, 0, 1), True,  (MG,MG), WIDTH - 2, zoom)
    for i in range(MIN, MAX+1, gap):
        print(i)
        proc_line(i, fn, mat, True,  fg, res, zoom)
        proc_line(i, fn, mat, False, fg, res, zoom)
        pygame.display.update()
        if is_quit(): return 0
    print('done')
    while True:
        if is_quit(): return 0

def proc_line(i, fn, mat, is_h, fg, res, zoom):
    line1 = line( i, -HWIDTH, HWIDTH, is_h, res)
    line2 = transform_line(line1, fn, mat, zoom)
    colour = fg[is_h]
    try:
        pygame.draw.lines(DISPLAY, colour, False, line2, LWIDTH)
    except Exception as e:
        print("proc_line:", e)
        print(line2)

def transform_line(line, fn, mat, zoom):
    rtn = []
    for z in line:
        try:
            w = fn(complex(z[0],z[1]))
            a11, a12, a21, a22 = mat
        except Exception as e:
            print("transform", e)
        else:
            x = w.real
            y = w.imag
            nx = zoom * (x * a11 + y * a12)
            ny = zoom * (x * a21 + y * a22)
            rtn.append(tuple(to_pygame_coords(nx, ny)))
    return rtn

def to_pygame_coords(x, y):
    return HWIDTH + int(x), HWIDTH - int(y)

def is_quit():
    return pygame.locals.QUIT in [e.type for e in pygame.event.get()]

def line(k, _min, _max, is_h, res):
    rtn = []
    i = _min
    while i <= _max:
        rtn.append( (is_h * i + (not is_h) * k, (not is_h) * i + is_h * k) )
        i += res
    return rtn

def get_fg(argv, fg_def, bg):
    if "-M" in argv:
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

def get_arg(argv, s, _def):
    if s in argv:
        i = argv.index(s)
        return argv[i + 1]
    else:
        return _def

def inv_clr(h):
    return 0xffffff - h

import sys
main(sys.argv)
