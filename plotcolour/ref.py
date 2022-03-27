import pygame
import pygame.font
from pygame.locals import *
from cmath import *

WIDTH = 601
HWIDTH = int(WIDTH/2)
LWIDTH = 2

BG = 0xffffff
FG = 0x000000
MG = 0x0000C0
BLUE = Color(0,0,200)

FG_H1 = 0xff0000
FG_H2 = 0x00ff00
FG_V1 = 0xffff00
FG_V2 = 0xff00ff

# defaults
GAP = "1"
RES = "0.1"

FN = "z"
MAT = "1 0 0 1"

ZOOM = 100

DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))

pygame.init()
FONT = pygame.font.SysFont(None, 20)

def get_opts(argv):
    global bg, fg, fn, mat, _min, _max, gap, res, zoom, orig
    bg  = get_bg(argv, BG)
    fg  = get_fg(argv, FG, bg)
    fn  = eval("lambda z : " + get_arg(argv, "-f", FN))
    mat = [float(i) for i in get_arg(argv, "-m", MAT).split()]
    gap = int  (get_arg(argv, "-g", GAP))
    res = float(get_arg(argv, "-r", RES))
    zoom= float(get_arg(argv, '-z', ZOOM))
    _max= int  (get_arg(argv, "-max", int(HWIDTH/zoom)))
    _min= int  (get_arg(argv, "-min", -_max))
    orig= '-O' not in argv

def main(argv):
    get_opts(argv)

    DISPLAY.fill(bg)

    if orig:
        draw_orig_lines()

    pygame.display.update()

    for i in range(_min, _max+1, gap):
        #print(i)
        try:
            proc_line(i, fn, mat, True,  fg, res)
            proc_line(i, fn, mat, False, fg, res)
            pygame.display.update()
        except Exception as e:
            print('main:', e)
        if is_quit():
            return 0

    print('done')
    while True:
        if is_quit():
            return 0

def draw_orig_lines():
    for i in range(_min, _max+1, gap):
        proc_line(i, lambda z : z, (1, 0, 0, 1), False, MG, res)
        proc_line(i, lambda z : z, (1, 0, 0, 1), True,  MG, res)
        fontimg = FONT.render(str(i), True, BLUE)
        DISPLAY.blit(fontimg, to_pygame_coords(i,0))
        DISPLAY.blit(fontimg, to_pygame_coords(0,i))

def proc_line(i, function, matrix, is_horizontal, foreground_colour, resolution):
    line1 = line( i, _min, _max, is_horizontal, resolution)
    line2 = transform_line(line1, function, matrix)
    colour = line_colour(i, is_horizontal)
    try:
        pygame.draw.lines(DISPLAY, colour, False, line2, LWIDTH)
    except Exception as e:
        print("proc_line:", e)
        print(line2)

def transform_line(line, fn, mat):
    rtn = []
    for z in line:
        try:
            w = fn(complex(z[0],z[1]))
            a11, a12, a21, a22 = mat
        except Exception as e:
            print("transform_line:", e)
        else:
            x = w.real
            y = w.imag
            nx = x * a11 + y * a12
            ny = x * a21 + y * a22
            rtn.append(tuple(to_pygame_coords(nx, ny)))
    return rtn

def to_pygame_coords(x, y):
    return int(HWIDTH + zoom*x), int(HWIDTH - zoom*y)

def is_quit():
    return pygame.locals.QUIT in [e.type for e in pygame.event.get()]

def line(k, _min, _max, is_h, resolution):
    # k: the (if is_h y x) value of the line
    # is_h : Is the line horizontal?
    rtn = []
    i = _min
    while i <= _max:
        rtn.append( (is_h * i + (not is_h) * k, (not is_h) * i + is_h * k) )
        i += resolution
    return rtn

def get_fg(argv, fg_def, bg):
    if "-M" in argv:
        return inv_clr(bg)
    else:
        if "-i" in argv:
            return inv_clr(fg_def)
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

def line_colour(k, is_horizontal):
    if is_horizontal:
        return Color(188, 0, 0)# (0xff0000 * abs(k) + 0x00ffff * (_max - abs(k)))/_max
    else:
        return Color(0, 128, 0)

import sys
main(sys.argv)
