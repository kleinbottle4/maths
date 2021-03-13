import pygame
from pygame.locals import *
from math import *
from mat import *

WIDTH = 500
FPS   = 30
RED   = 0xff0000
BLACK = (0, 0, 0)
WHITE = 0xffffff
BG_COLOUR = WHITE
FG_COLOUR = BLACK
CS = 100 # cube size
DISPLAY = pygame.display.set_mode((WIDTH, WIDTH))
XOFF = 2*CS
YOFF = 2*CS
INCR = 0.005
pygame.init()
FONT = pygame.font.Font(None, 24)

def main(argv):
    DISPLAY.fill(BG_COLOUR)
    fps_clock = pygame.time.Clock()
    cube_arr = [ 
            [[0],  [0],  [0] ], #0
            [[0],  [0],  [CS]], #1
            [[0],  [CS], [0] ], #2
            [[0],  [CS], [CS]], #3
            [[CS], [0],  [0] ], #4
            [[CS], [0],  [CS]], #5
            [[CS], [CS], [0] ], #6
            [[CS], [CS], [CS]], #7
            ]
    # random points:
    #cube_arr = [ [[4], [91], [69]], [[63], [36], [89]], [[58], [79],
    #    [61]], [[58], [61], [82]], [[69], [96], [42]], [[37], [86],
    #        [70]], [[88], [61], [39]], [[26], [6], [1]]]
    theta_x = 0
    theta_y = 0
    theta_z = 0
    while True:
        fps_clock.tick(FPS)
        theta_x, theta_y, theta_z = key_handler(theta_x, theta_y, theta_z)
        cube_arr = [
                matmul( rotZ(theta_z),
                    matmul( rotY(theta_y),
                        matmul( rotX(theta_x), i)))
                    for i in cube_arr ]
        DISPLAY.fill(BG_COLOUR)
        for i, j in [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3), (2,
            6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]:
            pygame.draw.line(DISPLAY, BLACK,
                    (cube_arr[i][0][0]+XOFF, cube_arr[i][1][0]+YOFF),
                    (cube_arr[j][0][0]+XOFF, cube_arr[j][1][0]+YOFF),
                    4)
        for i in cube_arr:
            pygame.draw.circle(DISPLAY, RED, (int(i[0][0])+XOFF,
                int(i[1][0])+YOFF), 4, 0)
        status = f"dθ_x/dt: {round(theta_x, 2)} dθ_y/dt: {round(theta_y, 2)} dθ_z/dt: {round(theta_z, 2)}"
        show_angles(status)
        pygame.display.update()

def show_angles(status):
    text_surf = FONT.render(status, True, FG_COLOUR)
    text_rect = text_surf.get_rect()
    text_rect.center = int(WIDTH/2), 20
    DISPLAY.blit(text_surf, text_rect)

def key_handler(_x, _y, _z):
    x, y, z = _x, _y, _z
    for e in pygame.event.get():
        if e.type == QUIT:
            exit(0)
        elif e.type == KEYDOWN:
            if e.key == K_z:
                z += INCR
            elif e.key == K_a:
                z -= INCR
            elif e.key == K_x:
                x += INCR
            elif e.key == K_r:
                x -= INCR
            elif e.key == K_y:
                y += INCR
            elif e.key == K_9:
                y -= INCR
    return x, y, z

def rotY(theta):
    return [
            [cos(theta), 0, sin(theta)],
            [0, 1, 0],
            [-sin(theta), 0, cos(theta)] ]

def rotX(theta):
    return [
            [ 1, 0, 0],
            [ 0, cos(theta), -sin(theta)],
            [ 0, sin(theta), cos(theta)]]

def rotZ(theta):
    return [
            [ cos(theta), -sin(theta), 0],
            [ sin(theta), cos(theta), 0],
            [ 0, 0, 1]]

if __name__ == '__main__':
    from sys import argv
    main(argv)
