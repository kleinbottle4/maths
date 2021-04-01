import pygame
from pygame.locals import *
from math import *

WIDTH = 500
HW = WIDTH / 2
GR_WIDTH = 10
BG_COLOUR = 0xffffff
GR_COLOUR = 0x000000
FG_COLOUR = 0xff0000

def main(argv):
    display = pygame.display.set_mode((WIDTH, WIDTH))
    p = 0.04
    sx = 25
    sy = 25
    expr = "c"
    while expr != 'q':
        if expr == 'c':
            reset_disp(display)
        elif expr == 'p':
            p = float(input('Precision: '))
        elif expr == 'sx':
            sx = float(input('Scale x: '))
        elif expr == 'sy':
            sy = float(input('Scale y: '))
        else:
            try:
                draw_graph(display, p, sx, sy, expr)
            except Exception as e:
                print(e)
        try:
            expr = input('f(x) = ')
        except Exception as e:
            print(e)
    return

def reset_disp(display):
    display.fill(BG_COLOUR)
    draw_grid(display)
    pygame.display.update()

def draw_graph(display, p, sx, sy, expr):
    parr = pygame.PixelArray(display)
    x = - ceil(HW / sx)
    y = 0
    while x < floor(HW / sy):
        try:
            y = eval(expr)
        except Exception as e:
            print(e)
            x += p
            continue
        py = int(HW - (y * sy))
        px = int((x * sx) + HW)
        if 0 <= px < WIDTH and 0 <= py < WIDTH:
            parr[px, py] = FG_COLOUR
        print(f"f({x})) = {y}")
        x += p
        pygame.display.update()
    del parr

def draw_grid(display):
    i = 0
    while i < WIDTH:
        pygame.draw.line(display, GR_COLOUR, (i, 0), (i, WIDTH))
        pygame.draw.line(display, GR_COLOUR, (0, i), (WIDTH, i))
        i += GR_WIDTH

def is_quit():
    return pygame.locals.QUIT in [e.type for e in pygame.event.get()]

if __name__ == '__main__':
    from sys import argv
    main(argv)
