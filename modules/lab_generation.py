import numpy as np  # При отладке так удобнее смотреть вывод лабиринта
import random
from modules.lab_classes import Cell
from modules.lab_classes import Player


def find_neighbors(coords):
    '''
    Ищет соседей, в том числе следующий портал, которые не посещены
    Args:
        coords: координаты текущей клетки
    Returns:
        neighbors: множество неизведанных соседних
    '''
    neighbors = set()
    if coords[0] > 0 and generation_lab[coords[0] - 1][coords[1]] == 0:
        neighbors.add((coords[0] - 1, coords[1]))
    if coords[0] < WIDTH - 1 and generation_lab[coords[0] + 1][coords[1]] == 0:
        neighbors.add((coords[0] + 1, coords[1]))
    if coords[1] > 0 and generation_lab[coords[0]][coords[1] - 1] == 0:
        neighbors.add((coords[0], coords[1] - 1))
    if coords[1] < HEIGHT - 1 and generation_lab[coords[0]][coords[1] + 1] == 0:
        neighbors.add((coords[0], coords[1] + 1))

    if lab[coords[0]][coords[1]] > '0' and lab[coords[0]][coords[1]] < str(NUM_PORTAL):
        next_portal = int(lab[coords[0]][coords[1]]) + 1
        next_portal_coords = (chosen_cells[next_portal] % WIDTH,
                              chosen_cells[next_portal] // WIDTH)
        if generation_lab[next_portal_coords[0]][next_portal_coords[1]] == 0:
            neighbors.add(next_portal_coords)

    return neighbors


def generate_walls(coords, way):
    '''
    Рекурсивная функция, позволяющая генерировать лабиринт

    Отмечаем текущую клетку как посещенную
    Ищем непосещенные соседние клетки (в т ч следующий портал)
    Пока есть подходящие соседние клетки:
        Выбираем случайную клетку из соседних
        Убираем стенку между текущей клеткой и выбранной
        Вызываем функцию для выбранной клетки
        Ищем непосещенные соседние клетки (в т ч следующий портал)

    Args:
        coords: координаты текущей клетки
        way: текущий маршрут
    '''
    global walls_v, walls_h, equip_coords, way_re
    generation_lab[coords[0]][coords[1]] = 1  # Текущая клетка посещенная
    way.append(coords)
    if coords == equip_coords:
        way_re = way.copy()
    neighbors = find_neighbors(coords)
    while len(neighbors) != 0:  # Пока остались непосещенные соседние клетки
        cell = random.choice(list(neighbors))
        if coords[0] == cell[0] and abs(coords[1] - cell[1]) == 1:
            walls_h[coords[0]][max(coords[1], cell[1])] = '*'
        elif coords[1] == cell[1] and abs(coords[0] - cell[0]) == 1:
            walls_v[max(coords[0], cell[0])][coords[1]] = '*'
        generate_walls(cell, way)
        neighbors = find_neighbors(coords)
    way = way[:len(way) - 1:]


def generate_objects_in_lab():
    '''
    Генерирует объекты в лабиринте
    Returns:
        lab: матрица с лабиринтом
        chosen_cells: список из выбранных клеток
    '''
    lab = [['0' for y in range(HEIGHT)] for x in range(WIDTH)]  # Заполняем лабиринт "нулями"
    chosen_cells = random.sample(range(WIDTH * HEIGHT), NUM_PORTAL + 3)  # Выбираем случайные клетки для объектов

    lab[chosen_cells[0] % WIDTH][chosen_cells[0] // WIDTH] = 'R'  # Больница = Respown
    lab[chosen_cells[-1] % WIDTH][chosen_cells[-1] // WIDTH] = 'E'  # Арсенал = Equipment center
    lab[chosen_cells[-2] % WIDTH][chosen_cells[-2] // WIDTH] = 'K'  # Ключ
    for i in range(1, len(chosen_cells) - 2):
        lab[chosen_cells[i] % WIDTH][chosen_cells[i] // WIDTH] = str(i)  # В этих клетках порталы
    return lab, chosen_cells


def generate_walls_in_lab():
    '''
    Генерирует объекты в лабиринте
    '''
    global generation_lab, walls_v, walls_h, equip_coords
    # Матрица с вертикальными стенами
    walls_v = [['|' for y in range(HEIGHT)] for x in range(WIDTH + 1)]  # Заполняем матрицу стен стенами "#"
    # Матрица с горизонтальными стенами
    walls_h = [['-' for y in range(HEIGHT + 1)] for x in range(WIDTH)]  # Заполняем матрицу стен стенами "#"
    # Рабочая матрица для генерации
    generation_lab = [[0 for y in range(HEIGHT)] for x in range(WIDTH)]  # Заполняем лабиринт нулями

    resp_coords = (chosen_cells[0] % WIDTH, chosen_cells[0] // WIDTH)  # Координаты больницы
    equip_coords = (chosen_cells[-1] % WIDTH, chosen_cells[-1] // WIDTH)  # Координаты арсенала
    generate_walls(resp_coords, [])  # Запускаем рекурсию

    # Генерируем положение двери
    num_door = random.randint(0, (WIDTH + HEIGHT) * 2 - 1)
    if num_door < WIDTH:
        walls_h[num_door][0] = '@'
    elif num_door < WIDTH * 2:
        walls_h[num_door - WIDTH][HEIGHT] = '@'
    elif num_door < 2 * WIDTH + HEIGHT:
        walls_v[0][num_door - 2 * WIDTH] = '@'
    else:
        walls_v[WIDTH][num_door - 2 * WIDTH - HEIGHT] = '@'


def generate_minotaurus():
    '''Отвечает за генерацию минотавров, не препятствующих прохождению лабиринта'''
    global useless_cells, lab
    max_num_minotaurus = max(min(len(useless_cells) - 2, 10), 0)
    min_num_minotaurus = max(max_num_minotaurus - 4, 0)
    num_minotaurus = random.randint(min_num_minotaurus, max_num_minotaurus)
    minotaurus = random.sample(list(useless_cells), num_minotaurus)
    for minotaur in minotaurus:
        lab[minotaur[0]][minotaur[1]] = 'M'
    useless_cells = useless_cells - set(minotaurus)


def generate_players():
    '''
    Отвечает за генерацию начальных положений игроков
    Returns:
        players: список из 2х игроков типа Player
    '''
    global useless_cells, lab
    players_coords = random.sample(list(useless_cells), 2)
    useless_cells = useless_cells - set(players_coords)
    players = []
    for i in range(len(players_coords)):
        players.append(Player(i, list(players_coords[i])))
        coords = players_coords[i]
        lab[coords[0]][coords[1]] = 'G' + str(i)
    return players


def generate_labirint():
    '''
    Генерирует матрицу элементов типа Cell
    Returns:
        labirint: матрица элементов типа Cell
    '''
    labirint = [['' for y in range(HEIGHT)] for x in range(WIDTH)]  # Заполняем лабиринт ничем
    for x in range(WIDTH):
        for y in range(HEIGHT):
            labirint[x][y] = Cell((x, y), lab, walls_v, walls_h)
    return labirint


def generate():
    '''
    Главная функция генерации. Генерирует весь лабиринт
    Returns:
        labirint: матрица элементов типа Cell, полностью описывающая лабиринт
        players_coords: координаты игроков (список списков)
    '''
    global SIZE, WIDTH, HEIGHT, NUM_PORTAL, chosen_cells, lab
    global way_re, useful_cells, useless_cells

    # Определяем основные параметры
    WIDTH = random.randint(2, 7)
    if WIDTH == 2:
        HEIGHT = random.randint(5, 7)
    elif WIDTH <= 4:
        HEIGHT = random.randint(4, 7)
    else:
        HEIGHT = random.randint(2, 7)
    SIZE = WIDTH, HEIGHT
    NUM_PORTAL = random.randint(2, 5)  # Должно быть строго меньше 10

    lab, chosen_cells = generate_objects_in_lab()
    way_re = []  # Путь из больницы в арсенал. Состоит из координат клеток маршрута
    generate_walls_in_lab()

    # Определяем, какие клетки заняты
    useful_cells = set()
    for number in chosen_cells:
        useful_cells.add((number % WIDTH, number // WIDTH))
    useless_cells = set((x, y) for y in range(HEIGHT) for x in range(WIDTH))
    useless_cells = useless_cells - useful_cells
    players = generate_players()

    useless_cells = useless_cells - set(way_re)
    generate_minotaurus()

    labirint = generate_labirint()
    #visualisation_of_generated_lab()

    return labirint, players


def visualisation_of_generated_lab():
    '''
    Функция для отладки. Отображает лабиринт
    '''
    global lab, walls_h, walls_v
    vis_lab = ['' for y in range(2 * HEIGHT + 2)]

    vis_lab[0] = ' '
    for x in range(WIDTH):
        vis_lab[0] += (walls_h[x][0])
        vis_lab[0] += ' '

    for y in range(HEIGHT):

        for x in range(WIDTH):
            vis_lab[2 * y + 1] += (walls_v[x][y])
            vis_lab[2 * y + 1] += (lab[x][y])
        vis_lab[2 * y + 1] += (walls_v[x + 1][y])

        vis_lab[2 * y + 2] = ' '
        for x in range(WIDTH):
            vis_lab[2 * y + 2] += (walls_h[x][y + 1])
            vis_lab[2 * y + 2] += ' '

    for y in range(len(vis_lab)):
        print(vis_lab[y])


if __name__ == "__main__":
    print("This module is not for direct call!")
