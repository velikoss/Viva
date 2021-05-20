import time

import numpy
import numpy as np
import pygame

rng = np.random.default_rng()

# ВВОД ПЕРВИЧНЫХ ДАННЫХ

print("Ширина и высота (Число клеток)")
WIDTH = int(input()) * 10
WIDTHG = WIDTH // 10
FPS = 60
TICK = 0.2  # ВРЕМЯ ОБНОВЛЕНИЯ ПОЛЯ (В СЕКУНДАХ)

# ВВОД КОЭФФИЦИЭНТОВ КЛЕТОК

print("Введите коэффициэнты клеток от ЗАР+НЕМАС, НЕЗАР+МАС, ЗАР+МАС")
k01 = float(input()) / 100  # КОЭФ ЗАР+НЕМАС
k10 = float(input()) / 100  # КОЭФ НЕЗАР+МАС
k11 = float(input()) / 100  # КОЭФ ЗАР+МАС

# ЦВЕТА

COLORS = [(0, 0, 0), (0, 0, 200), (100, 100, 100), (200, 200, 200)]


def check(d, ii):
    print(d[ii])
    f = np.array(np.where(np.logical_and((d[:, 0] - d[ii][0]) ** 2 < 2, (d[:, 1] - d[ii][1]) ** 2 < 2))[0])
    lenf = len(f)
    lastlenf = -1
    while lenf != lastlenf:
        lastlenf = len(f)
        for i in f:
            f1 = np.array(np.where(np.logical_and((d[:, 0] - d[i][0]) ** 2 < 2, (d[:, 1] - d[i][1]) ** 2 < 2)))
            f = np.unique(np.append(f, f1))
        lenf = len(f)
    # print(f)
    return f


def rcords(x, y):
    rx = np.random.randint(0, 3) - 1
    ry = np.random.randint(0, 3) - 1
    nx, ny = x + rx, y + ry
    if nx < 0:
        nx = WIDTHG - 1
    elif nx > WIDTHG - 1:
        nx = 0
    if ny < 0:
        ny = WIDTHG - 1
    elif ny > WIDTHG - 1:
        ny = 0
    return rx, ry, nx, ny


def move(mgrid, grid):
    nlist = [check(mgrid, 0)]
    for _ in range(len(mgrid)):
        nlist = list((*nlist,check(mgrid,_)))
    nlist = np.unique(nlist, nlist,  axis=0)
    print(nlist)
    # x = mgrid[_][0]
    # y = mgrid[_][1]
    # rx, ry, nx, ny = rcords(x, y)
    # result = np.where((mgrid == (x, y)).all(axis=1))[0][0]
    # f = check(mgrid, result)
    # f.sort()
    # for i in f:
    #     x1 = mgrid[i][0]
    #     y1 = mgrid[i][1]
    #     nx1 = x1 + rx
    #     ny1 = y1 + ry
    #     if nx1 < 0:
    #         nx1 = WIDTHG - 1
    #     elif nx1 > WIDTHG - 1:
    #         nx1 = 0
    #     if ny1 < 0:
    #         ny1 = WIDTHG - 1
    #     elif ny1 > WIDTHG - 1:
    #         ny1 = 0
    #     if grid[nx1][ny1] == 0:
    #         grid[nx1][ny1] = grid[x1][y1]
    #         grid[x1][y1] = 0
    return grid


def main():
    running = True
    grid = rng.choice(4, WIDTHG * WIDTHG, p=[1 - (k01 + k10 + k11), k01, k10, k11]).reshape(WIDTHG, WIDTHG)
    # print(grid)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(0, WIDTHG, 1):
            for j in range(0, WIDTHG, 1):
                pygame.draw.rect(screen, COLORS[grid[i][j]], (i * 10, j * 10, 10, 10))
        mgrid = np.where(grid != 0)
        mgrid = np.array(mgrid)
        mgrid = mgrid.transpose()
        grid = move(mgrid, grid)
        pygame.display.flip()
        time.sleep(TICK)
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("vivatest")
    font = pygame.font.SysFont("Tahoma", 15, True)
    clock = pygame.time.Clock()
    main()
