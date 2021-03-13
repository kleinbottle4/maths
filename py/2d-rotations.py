# Aim: to rotate a point P by θ°:, centre O.

# MIT License

# Copyright (c) 2020 syed343 (GitHub username)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pygame
from math import sin, cos, radians

def image(m, p):
    # where m is a 2x2 matrix and p is a point
    a, b, c, d = m[0][0], m[0][1], m[1][0], m[1][1]
    e, f = p[0], p[1]
    return (a*e + b*f, c*e + d*f)

def convert_point(p, width, offset):
    # normally (0, 0) refers to the centre of the window, but not in Pygame!
    return (int(p[0] + offset), int(width - p[1] - offset))

def point_to_text(p, name):
    # e.g. "P(100, 97)"
    return '{}({:.0f}, {:.0f})'.format(name, int(p[0]), int(p[1]))

def matrix_to_text(m, name):
    n = [['{:.2f}'.format(i) for i in j] for j in m]
    return '{} = (({}, {}), ({}, {}))'.format(name, n[0][0], n[0][1], n[1][0], n[1][1])


# P is referred to as p in the code
p = [float(i) for i in input('Enter point P as a, b: ').split(',')]
# t = theta = angle (in degrees) by which P is rotated, centre origin
t = float(input('Enter starting value for angle θ°: '))

WIDTH = 500
OFFSET = int(500/2)
R = 3 # radius of plotted points
FONT_SIZE = 18
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = int(input('Enter FPS: '))

DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))
fps_clock = pygame.time.Clock()

pygame.init()
FONT = pygame.font.Font(None, FONT_SIZE) # None -> default font of OS

while True:
    t = (t + 1) % 360
    rt = radians(t)
    # m is a 2x2 matrix
    m = [[cos(rt), -1 * sin(rt)], [sin(rt), cos(rt)]]
    # P` is referred to as q in the code
    q = image(m, p)

    # background and axes
    DISPLAY.fill(WHITE)
    pygame.draw.line(DISPLAY, BLACK, (OFFSET, 0), (OFFSET, WIDTH))
    pygame.draw.line(DISPLAY, BLACK, (0, OFFSET), (WIDTH, OFFSET))

    # text in the top right of the window
    text = [FONT.render(f'{t}°', True, BLACK),
            FONT.render(point_to_text(p, 'P'), True, BLACK),
            FONT.render(point_to_text(q, 'P`'), True, BLACK),
            FONT.render(matrix_to_text(m, 'M'), True, BLACK)]

    for i, tx in enumerate(text):
        DISPLAY.blit(tx, (WIDTH - tx.get_width(), (i + 1) * tx.get_height()))

    # plot O, P, P` and the line OP`
    _p = convert_point(p, WIDTH, OFFSET)
    _q = convert_point(q, WIDTH, OFFSET)
    _o = convert_point((0, 0), WIDTH, OFFSET) 

    pygame.draw.line(DISPLAY, RED, _o, _q)
    pygame.draw.circle(DISPLAY, RED, _p, R)
    pygame.draw.circle(DISPLAY, RED, _o, R)
    pygame.draw.circle(DISPLAY, RED, _q, R)

    # update screen and check if the user wants to quit
    pygame.display.update()
    fps_clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
