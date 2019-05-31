import numpy as np
#import pygame
import pygame as py
from pygame import gfxdraw as dw
import sys
def calculate_the_heat():
    for i in range(1, size):
        for j in range(1, size):
            if i != size - 1 and j != size - 1:
                grid[i][j] = grid[i][j] + kf * (grid[i - 1][j] + grid[i + 1][j] + grid[i][j - 1] + grid[i][j + 1] - 4.0 * grid[i][j])
            if grid[i][j] < 1.0:
                grid[i][j] = 0.0


size = 200
grid = np.zeros((size, size))
py.init()
window = py.display.set_mode((size, size))
window.fill((0, 0, 255))
py.display.update()
kf = 0.25
while True:
    calculate_the_heat()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    if py.mouse.get_pressed()[0]:
        grid[py.mouse.get_pos()[0]][py.mouse.get_pos()[1]] = 400.0
    for i in range(size):
        for j in range(size):
            if grid[i][j] > 0.0 and grid[i][j] < 1024.0:
                dw.circle(window, i, j, 2, (255, 255 - int(grid[i][j]) % 256, 255 - int(grid[i][j]) % 256))
            elif grid[i][j] > 1024.0:
                dw.circle(window, i, j, 2, (255, 255, 255))
            else:
                dw.circle(window, i, j, 1, (0, 0, 255))

    py.display.update()
