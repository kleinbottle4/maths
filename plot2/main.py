# -*- eval: (outshine-mode 1); -*-
import pygame
import pygame.locals
import sys
from math import *
from cmath import *

# * needed before globals
# ** get_arg
def get_arg(s, use_default = False, default = 1):
    try:
        i = ARGV.index(s)
    except ValueError:
        if use_default:
            return default
        else:
            return input(f"{s}: ")
    else:
        return ARGV[i + 1]

# ** return a list of real numbers
def get_range(msg):
    rtn = []
    n = 0
    push = START
    while push <= END:
        rtn.append(push)
        push += RESOLUTION
    return rtn

# *  return a function of form Type -> Type
def get_function(s):
    return eval("lambda t : " + get_arg(s))

# **  drawing
# **   draw the grid
def draw_grid():
    DISPLAY.fill(WHITE)
    # vertical
    for i in range(0, HWIDTH + 1, GRID_GAP * ZOOM):
        pygame.draw.line(DISPLAY, BLACK, (HWIDTH + i, 0), (HWIDTH + i, WIDTH), THICKNESS)
        pygame.draw.line(DISPLAY, BLACK, (HWIDTH - i, 0), (HWIDTH - i, WIDTH), THICKNESS)
    # vertical
    for i in range(0, HWIDTH + 1, GRID_GAP * ZOOM):
        pygame.draw.line(DISPLAY, BLACK, (0, HWIDTH + i), (WIDTH, HWIDTH + i), THICKNESS)
        pygame.draw.line(DISPLAY, BLACK, (0, HWIDTH - i), (WIDTH, HWIDTH - i), THICKNESS)
    # origin
    pygame.draw.circle(DISPLAY, BLUE, (HWIDTH, HWIDTH), THICKNESS * 2)
    pygame.display.update()

# **   draw a line of complex numbers
def draw_line(line, colour):
    pygame.draw.lines(DISPLAY, colour, False, line_to_pygame(line), THICKNESS)
    pygame.display.update()

# **   get pygame coords
def complex_to_pygame(z):
    return (int(HWIDTH + ZOOM * z.real), int(HWIDTH - ZOOM * z.imag))

def line_to_pygame(line):
    return [ complex_to_pygame(z) for z in line ]

# **  line utilities

# * config
WHITE = "#FFFFFF"
RED = "#FF0000"
BLACK = "#000000"
BLUE = '#0000FF'
ARGV = sys.argv
HWIDTH = 500
WIDTH = 2 * HWIDTH
THICKNESS = 3
GRID_GAP = int(get_arg('-g', True, 1))
ZOOM = int(get_arg('-z', True, 100))
RESOLUTION = float(get_arg("-r", True, 0.1))
START = float(get_arg("-s", True, -100))
END = float(get_arg("-e", True, 100))
TS = get_range("range of ts: ")

# * helper functions
# ** intended to be used for lines of complex numbers
def transform_line(line, function):
    rtn = []
    for z in line:
        try:
            rtn.append(function(z))
        except Exception as e:
            print(f'z = {z}\nError "{e}"')
            continue
    return rtn

# **  return a line of complex numbers defined parametrically as x + iy = f_x(t) + i f_y(t)
def get_line(msg):
    x_function = get_function("-x")
    y_function = get_function("-y")
    line = [ complex(x_function(t), y_function(t)) for t in TS ]
    return line

# ***  other
# * loop
def loop():
    line = get_line("line: ")
    function = get_function("-f")
    transformed_line = transform_line(line, function)
    draw_line(line, BLUE)
    draw_line(transformed_line, RED)

# * main
DISPLAY = pygame.display.set_mode((WIDTH,WIDTH))
draw_grid()
while True:
    print('New loop...')
    try:
        loop()
    except Exception as e:
        print(f'Error with loop: "{e}"')
    else:
        print('Done.')
    # remove ARGV after first iteration to remove -x -y and -f
    ARGV = []
    if pygame.locals.QUIT in [event.type for event in pygame.event.get()]:
        quit()
