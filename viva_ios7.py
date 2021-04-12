# encoding=utf-8
import os
import time
import sys
from random import *

# ВВОД ПЕРВИЧНЫХ ДАННЫХ

print("Ширина и высота (Число клеток)")
WIDTH = int(input()) * 10
HEIGHT = int(input()) * 10
FPS = 60
TICK = 0.05  # ВРЕМЯ ОБНОВЛЕНИЯ ПОЛЯ (В СЕКУНДАХ)

# ЦВЕТА
COLORS = ["-", "1", "2", "3"]


def check(x, y, list_xy):
    col = 0
    try:
        for i in range(-1, 1):
            for j in range(-1, 1):
                if i != 0 and j != 0:
                    if list_xy[x + i][y + j] != 0:
                        col += 1
        return col
    except IndexError:
        print("Впоймал IndexError")


def rcords(x, y):
    rx, ry = randint(-1, 1), randint(-1, 1)
    nx, ny = x + rx, y + ry
    if nx < 0:
        nx = WIDTH // 10 - 1
    if nx > WIDTH // 10 - 1:
        nx = 0
    if ny < 0:
        ny = HEIGHT // 10 - 1
    if ny > HEIGHT // 10 - 1:
        ny = 0
    return rx, ry, nx, ny


def rmove(markedx, markedy, list_xy):
    for i in range(0, len(markedx)):
        x, y = markedx[i], markedy[i]
        if check(x, y, list_xy) >= 8: continue
        rx, ry, nx, ny = rcords(x, y)
        try:
            while list_xy[nx][ny] != 0:
                rx, ry, nx, ny = rcords(x, y)
        except IndexError:
            print("Впоймал IndexError")
        if nx < len(list_xy[x]) - 1 or ny < len(list_xy[x]) - 1:
            list_xy[nx][ny] = list_xy[x][y]
            if nx != x or ny != y: list_xy[x][y] = 0
    return list_xy


# ФУНКЦИЯ, ГДЕ КЛЕТКА ПО КОЭФФИЦИЭТАМ ЛИБО ОСТАЁТСЯ СОБОЙ, ЛИБО СТАНОВИТСЯ НЕЗАРЯЖ+НЕМАСС (1-3 ИЛИ 0)

def krand(cell):
    return cell * randint(0, 1) * randint(0, 1)


# СОЗДАНИЕ СЕТКИ

def tabrandom(w, h):
    return [[krand(randint(1, 3)) for _ in range(w)] for __ in range(h)]


# ОСНОВНАЯ ФУНКЦИЯ

def main():
    running = True
    list_xy = tabrandom(WIDTH // 10, HEIGHT // 10)
    while running:
        # ОСНОВНАЯ ПРОГРАММА НИЖЕ
        markedx = list()
        markedy = list()
        for i in range(0, WIDTH - 1, 10):  # РАБОТАЕТ НЕ ТРОГАЙ
            print()
            for j in range(0, HEIGHT - 1, 10):
                sys.stdout.write(COLORS[list_xy[i // 10][j // 10]] + " ")
                if list_xy[i // 10][j // 10] != 0: markedx.append(i // 10), markedy.append(j // 10)
        list_xy = rmove(markedx, markedy, list_xy)
        print("")
        print(len(markedx))
        time.sleep(0.3)
        os.system("clear")


if __name__ == '__main__':
    main()
