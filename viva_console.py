import os
import time
from random import *

# ВВОД ПЕРВИЧНЫХ ДАННЫХ

print("Ширина и высота (Число клеток)")
WIDTH = int(input()) * 10
HEIGHT = int(input()) * 10
FPS = 60
TICK = 0.05  # ВРЕМЯ ОБНОВЛЕНИЯ ПОЛЯ (В СЕКУНДАХ)

# ВВОД КОЭФФИЦИЭНТОВ КЛЕТОК

print("Введите коэффициэнты клеток от ЗАР+НЕМАС, НЕЗАР+МАС, ЗАР+МАС")
k01 = int(input())  # КОЭФ ЗАР+НЕМАС
k10 = int(input())  # КОЭФ НЕЗАР+МАС
k11 = int(input())  # КОЭФ ЗАР+МАС

# ЦВЕТА
COLORS = ["-", "1", "2", "3"]


def rcords(x, y):
    rx, ry = randint(-1, 1), randint(-1, 1)
    nx, ny = x + rx, y + ry
    if (rx * rx) + (ry * ry) == 0:
        rx = randint(-1, 1)
        if not rx: ry = randrange(-1, 1, 2)
        else: ry = randint(-1, 1)
        nx, ny = x + rx, y + ry
    if nx < 1:
        nx = x + 1
    if nx > WIDTH // 10 - 2:
        nx = x - 1
    if ny < 1:
        ny = y + 1
    if ny > HEIGHT // 10 - 2:
        ny = y - 1
    return rx, ry, nx, ny



def rmove(markedx, markedy, list_xy):
    for i in range(0, len(markedx)):
        x, y = markedx[i], markedy[i]
        rx, ry, nx, ny = rcords(x, y)
        if list_xy[nx][ny] == 0:
            list_xy[nx][ny] = list_xy[x][y]
            if nx != x or ny != y: list_xy[x][y] = 0
    return list_xy


# ФУНКЦИЯ, ГДЕ КЛЕТКА ПО КОЭФФИЦИЭТАМ ЛИБО ОСТАЁТСЯ СОБОЙ, ЛИБО СТАНОВИТСЯ НЕЗАРЯЖ+НЕМАСС (1-3 ИЛИ 0)

def krand(cell):
    if cell == 1:
        cell = choices([1, 0], weights=[k01, 100 - k01])[0]
    elif cell == 2:
        cell = choices([2, 0], weights=[k10, 100 - k10])[0]
    elif cell == 3:
        cell = choices([3, 0], weights=[k11, 100 - k11])[0]
    return cell


# СОЗДАНИЕ СЕТКИ

def tabrandom(w, h):
    return [[krand(randint(1, 3)) for _ in range(w)] for __ in range(h)]


# ОСНОВНАЯ ФУНКЦИЯ

def main():
    running = True
    list_xy = tabrandom(WIDTH // 10, HEIGHT // 10)
    while running:
        # ОСНОВНАЯ ПРОГРАММА НИЖЕ
        markedx, markedy = list(), list()
        for i in range(0, WIDTH - 1, 10):  # РАБОТАЕТ НЕ ТРОГАЙ
            print()
            for j in range(0, HEIGHT - 1, 10):
                print(COLORS[list_xy[i // 10][j // 10]], end=" ")
                if list_xy[i // 10][j // 10] != 0: markedx.append(i // 10), markedy.append(j // 10)
        list_xy = rmove(markedx, markedy, list_xy)
        print("")
        print(len(markedx))
        time.sleep(0.05)
        os.system("cls")


if __name__ == '__main__':
    main()
