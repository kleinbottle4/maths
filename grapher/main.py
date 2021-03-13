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
    p = 10
    sx = 100
    sy = 100
    expr = "c"
    while expr != 'q':
        if expr == 'c':
            reset_disp(display)
        elif expr == 'p':
            p = int(input('Precision: '))
        elif expr == 'sx':
            sx = int(input('Scale x: '))
        elif expr == 'sy':
            sy = int(input('Scale y: '))
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
    x = - HW
    while x < HW - 1:
        try:
            y = eval(expr)
        except Exception as e:
            print(e)
        py = int((HW - y) * sy)
        px = int((x + HW) * sx)
        try:
            parr[px][py] = FG_COLOUR
        except IndexError as e:
            print(e, ':', px, py)
        except Exception as e:
            print('Draw graph:', e)
        else:
            print(f"f({round(x, 1)}) = {round(y, 1)}")

        x += 1 / p
    del parr
    pygame.display.update()

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
