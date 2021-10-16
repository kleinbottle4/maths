import pygame
from pygame.locals import *
from math import *
from mat import *

WIDTH = 500
FPS   = 30
DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))

pygame.init()
FONT = pygame.font.SysFont("FreeMono", 15)

RED   = 0xff0000
BLACK = (0, 0, 0)
WHITE = 0xffffff
BG_COLOUR = WHITE
FG_COLOUR = BLACK

CS = int(0.25 * WIDTH) # cube length
INCR = 0.005 # of angle t
PROJ = [[1, 0, 0],
       [0, 1, 0]]

PYG = [[1, 0], [0, -1]] # convert to pygame coordinates
XOFF = int(0.5 * WIDTH)
YOFF = XOFF

def main(argv):
    DISPLAY.fill(BG_COLOUR)
    fps_clock = pygame.time.Clock()
    cube_mat_t = [
            [0,  0,  0 ], #0
            [0,  0,  CS], #1
            [0,  CS, 0 ], #2
            [0,  CS, CS], #3
            [CS, 0,  0 ], #4
            [CS, 0,  CS], #5
            [CS, CS, 0 ], #6
            [CS, CS, CS], #7
            ]
    cube_mat = transpose(cube_mat_t)
    t_x = 0
    t_y = 0
    t_z = 0
    while True:
        fps_clock.tick(FPS)
        t_x, t_y, t_z = key_handler(t_x, t_y, t_z)
        cube_mat = matmul(rot_z(t_z),
                        matmul(rot_y(t_y),
                            matmul(rot_x(t_x), cube_mat)))
        cube_mat_t = transpose(cube_mat)
        proj_mat = matmul(PROJ, cube_mat)
        pgc_mat = matmul(PYG, proj_mat)
        pgc_mat_t = transpose(pgc_mat)

        DISPLAY.fill(BG_COLOUR)

        # join up lines
        for i, j in [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2,
            6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]:
            pygame.draw.line(DISPLAY, BLACK,
                    (pgc_mat_t[i][0]+XOFF, pgc_mat_t[i][1]+YOFF),
                    (pgc_mat_t[j][0]+XOFF, pgc_mat_t[j][1]+YOFF),
                    4)
        # highlight vertices
        for row in pgc_mat_t:
            pygame.draw.circle(DISPLAY, RED, (int(row[0])+XOFF,
                int(row[1])+YOFF), 4, 0)

        # show angle derivatives
        status = f"dθ_x/dt: {round(t_x, 2)} dθ_y/dt: {round(t_y, 2)} dθ_z/dt: {round(t_z, 2)}"
        show_angles(status)
        pygame.display.update()

def show_angles(status):
    text_surf = FONT.render(status, True, FG_COLOUR)
    text_rect = text_surf.get_rect()
    text_rect.center = int(WIDTH/2), 20
    DISPLAY.blit(text_surf, text_rect)

def key_handler(_x, _y, _z):
    # { key: (x y or z?, anti-clockwise?) }
    map_keys = {
            K_a: (0, 1),
            K_b: (0, -1),
            K_c: (1, 1),
            K_d: (1, -1),
            K_e: (2, 1),
            K_f: (2, -1),
            }
    rtn = [_x, _y, _z]
    for e in pygame.event.get():
        if e.type == QUIT:
            exit(0)
        elif e.type == KEYDOWN:
            for k, v in map_keys.items():
                if e.key == k:
                    rtn[v[0]] += INCR * v[1]
    return rtn

def rot_y(t):
    return [
            [cos(t),  0, sin(t)],
            [0,       1, 0],
            [-sin(t), 0, cos(t)] ]

def rot_x(t):
    return [
            [ 1, 0,      0],
            [ 0, cos(t), -sin(t)],
            [ 0, sin(t), cos(t)]]

def rot_z(t):
    return [
            [ cos(t), -sin(t), 0],
            [ sin(t), cos(t),  0],
            [ 0,      0,       1] ]

if __name__ == '__main__':
    from sys import argv
    main(argv)
