import pygame
from cmath import *
from math import *

WIDTH = 1000
HALFWIDTH = int(WIDTH/2)
DISPLAY = pygame.display.set_mode((WIDTH,WIDTH))
RED = (255,0,0)
WHITE = (255, 255, 255)
GREEN = (0,255,0)
RIGHT = 0.5
LEFT = - RIGHT
SCALE = HALFWIDTH / RIGHT
N = 1000
DISPLAY.fill(WHITE)
i = complex(0, 1)

def g(z):
    return ((1 + i)*(z.real)**3 - (1 - i)*(z.imag)**3) / ( z * z.conjugate() )

def f(z):
    h = 0.00001
    return (g(z + h) - g(z))/h


def main():
    for x in linspace(LEFT, RIGHT, N):
        for y in linspace(LEFT, RIGHT, N):
            plot(complex(x,y), f(complex(x, y)))
        pygame.display.update()
        print("Finished x =", x, ".")
    input("Press key to exit.")
    print("Done")


def plot(z, fz):
    r, theta = polar(fz)
#    lightness = 100 * r**2 /(1 + r**2) # r = 0 is darkest
    lightness = 50
    hue = int(360 * 0.5 * (1 + (theta / pi)))
#    hue = 0.5 * (1 + (theta / pi))
#   color = pygame.Color(int(hue * 255), 255 - int(hue * 255), 255, 255)
    color = pygame.Color(255,255,255,255)
    color.hsla = (hue, 100, lightness, 100)
    rect = pygame.Rect(0, 0, 0, 0)
    rect.center = to_pygame_coords(z, SCALE)
    rect.width = WIDTH / N
    rect.height = rect.width
    pygame.draw.rect(DISPLAY, color, rect)

def linspace(start, stop, n):
    start = LEFT
    stop = RIGHT
    step = (stop - start) / float(n)
    rtn = []
    assert step > 0, "step is not positive"
    while start <= stop:
        rtn.append(start)
        start += step
    return rtn

def to_pygame_coords(z, scale):
    a = HALFWIDTH + z.real * scale
    b = HALFWIDTH - z.imag * scale
    return (a, b)

main()
