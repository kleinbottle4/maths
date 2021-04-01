import pygame
from pygame.locals import *
import cmath

WIDTH = 500
HALFWIDTH = int(WIDTH/2)
BG = 0xffffff
FG = 0x000000

RMAX = 1250
IMAX = 1250
RSTEP = 10
ISTEP = 10
FN = lambda z : cmath.sqrt(z)

ZOOMX = 1
ZOOMY = 1

def main(argv):
    DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))
    DISPLAY.fill(BG)
    px = pygame.PixelArray(DISPLAY)
    a = 0
    while a <= RMAX:
        b = 0
        while b <= IMAX:
            w = complex(a, b)
            z = FN(w)
            x = int(ZOOMX*z.real) + HALFWIDTH
            y = HALFWIDTH - int(ZOOMY*z.imag)
            if 0 <= x < WIDTH and 0 <= y < WIDTH:
                px[x, y] = FG
            b = incr(b, ISTEP)
        print(f"Re: {a}")
        pygame.display.update()
        if is_quit(): return 0
        a = incr(a, RSTEP)
    print('done')
    del px
    while True:
        if is_quit():
            return 0

def is_quit():
    return pygame.locals.QUIT in [e.type for e in pygame.event.get()]

# incr tries to increase |z| gradually
def incr(x, step):
    rtn = 0
    if x < 0:
        rtn = -x
    else:
        rtn = -x - step
    return rtn

if __name__ == '__main__':
    from sys import argv
    main(argv)
