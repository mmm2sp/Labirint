import numpy as np #При отладке так удобнее смотреть вывод лабиринта
import random

class Cell:
    '''Класс клетка, хранящий всю необходимую информацию о клетке лабиринта'''
    coords = (-1, -1)
    typ = '0'
    up = '-'
    down = '-'
    left = '|'
    right = '|'
    equipment = []
    def __init__(self, coords, lab, walls_v, walls_h):
        '''
        Заполняет параметры в соответствии с полученными данными
        Args:
            coords: координаты клетки
            lab: матрица лабиринта
            walls_v: матрица вертикальных стенок
            walls_h: матрица горизонатльных стенок
        '''
        self.coords = coords
        self.typ = lab[coords[0]][coords[1]]
        if self.typ == 'A':
            self.equipment.append('A')
        if self.typ == 'K':
            self.equipment.append('k')
        self.up = walls_h[coords[0]][coords[1]]
        self.down = walls_h[coords[0]][coords[1] + 1]
        self.left = walls_v[coords[0]][coords[1]]
        self.right = walls_v[coords[0] + 1][coords[1]]


def generate_objects_in_lab():
    '''
    Генерирует объекты в лабиринте
    Returns:
        lab: матрица с лабиринтом
        chosen_cells: список из выбранных клеток
    '''
    lab = [['0' for y in range(HEIGHT)] for x in range(WIDTH)] #Заполняем лабиринт "нулями"
    chosen_cells = random.sample(range(WIDTH * HEIGHT), NUM_PORTAL+3) #Выбираем случайные клетки для объектов

    lab[chosen_cells[0] % WIDTH][chosen_cells[0] // WIDTH] = 'H' #Больница = Hospital
    lab[chosen_cells[-1] % WIDTH][chosen_cells[-1] // WIDTH] = 'A' #Арсенал
    lab[chosen_cells[-2] % WIDTH][chosen_cells[-2] // WIDTH] = 'K' #Ключ
    for i in range(1, len(chosen_cells) - 2):
        lab[chosen_cells[i] % WIDTH][chosen_cells[i] // WIDTH] = str(i) #В этих клетках порталы
    return lab, chosen_cells

def generate_walls_in_lab():
    '''
    Генерирует объекты в лабиринте
    '''
    global generation_lab, walls_v, walls_h, ars_coords
    #Матрица с вертикальными стенами
    walls_v = [['|' for y in range(HEIGHT)] for x in range(WIDTH + 1)] #Заполняем матрицу стен стенами "#"
    #Матрица с горизонтальными стенами
    walls_h = [['-' for y in range(HEIGHT + 1)] for x in range(WIDTH)] #Заполняем матрицу стен стенами "#"
    #Рабочая матрица для генерации
    generation_lab = [[0 for y in range(HEIGHT)] for x in range(WIDTH)] #Заполняем лабиринт нулями

    hosp_coords = (chosen_cells[0] % WIDTH, chosen_cells[0] // WIDTH) #Координаты больницы
    ars_coords = (chosen_cells[-1] % WIDTH, chosen_cells[-1] // WIDTH) #Координаты арсенала
    generate_walls(hosp_coords, []) #Запускаем рекурсию

    #Генерируем положение двери
    num_door = random.randint(0, (WIDTH + HEIGHT)*2 - 1)
    if num_door < WIDTH:
        walls_h[num_door][0] = '@'
    elif num_door < WIDTH*2:
        walls_h[num_door - WIDTH][HEIGHT] = '@'
    elif num_door < 2*WIDTH + HEIGHT:
        walls_v[0][num_door - 2*WIDTH] = '@'
    else:
        walls_v[WIDTH][num_door - 2*WIDTH - HEIGHT] = '@'

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
        #print('next_portal is ', next_portal)
        next_portal_coords = (chosen_cells[next_portal] % WIDTH,
                          chosen_cells[next_portal] // WIDTH)
        #print('next_portal_coords are ', next_portal_coords)
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
    global walls_v, walls_h, ars_coords, way_ha
    generation_lab[coords[0]][coords[1]] = 1 #Текущая клетка посещенная
    way.append(coords)
    if coords == ars_coords:
        way_ha = way.copy()
    #print(way)
    neighbors = find_neighbors(coords)
    while len(neighbors) != 0: #Пока остались непосещенные соседние клетки
        cell = random.choice(list(neighbors))
        if coords[0] == cell[0] and abs(coords[1] - cell[1]) == 1:
            walls_h[coords[0]][max(coords[1],cell[1])] = '*'
        elif coords[1] == cell[1] and abs(coords[0] - cell[0]) == 1:
            walls_v[max(coords[0],cell[0])][coords[1]] = '*'
        #else:
            #print("We are going into portal")
        generate_walls(cell, way)
        neighbors = find_neighbors(coords)
    way = way[:len(way_ha)-1:]

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

def generate_labirint():
    '''
    Генерирует матрицу элементов типа Cell
    Returns:
        labirint: матрица элементов типа Cell
    '''
    labirint = [['' for y in range(HEIGHT)] for x in range(WIDTH)] #Заполняем лабиринт ничем
    for x in range(WIDTH):
        for y in range(HEIGHT):
            labirint[x][y] = Cell((x, y), lab, walls_v, walls_h)
    return labirint

def generate():
    '''
    Главная функция генерации. Генерирует весь лабиринт
    ВАЖНО! При отображении матрицу надо транспонировать(или считать х вниз, а у вправо)
    Returns:
        labirint: матрица элементов типа Cell, полностью описывающая лабиринт
    '''
    global SIZE, WIDTH, HEIGHT, NUM_PORTAL, chosen_cells, lab
    global way_ha, useful_cells, useless_cells

    #Определяем основные параметры
    WIDTH = random.randint(2, 7)
    if WIDTH <= 4:
        HEIGHT = random.randint(4, 7)
    else:
        HEIGHT = random.randint(2, 7)
    SIZE = WIDTH, HEIGHT
    NUM_PORTAL = random.randint(2, 5) #Должно быть строго меньше 10, иначе 2 цифры
    
    lab, chosen_cells = generate_objects_in_lab()
    way_ha = []
    generate_walls_in_lab()

    #Определяем, какие клетки можно загромождать
    useful_cells = set(way_ha)
    for number in chosen_cells:
        useful_cells.add((number % WIDTH, number // WIDTH))
    useless_cells = set((x, y) for y in range(HEIGHT) for x in range(WIDTH))
    useless_cells = useless_cells - useful_cells
    generate_minotaurus()
    
    labirint = generate_labirint()
    visualisation_of_generated_lab()

def visualisation_of_generated_lab():
    '''
    Функция для отладки. Отображает корректно лабиринт (транспонированный)
    '''
    global lab, walls_h, walls_v
    vis_lab = ['' for y in range(2*HEIGHT + 2)]
    
    vis_lab[0] = ' '
    for x in range(WIDTH):
        vis_lab[0] += (walls_h[x][0])
        vis_lab[0] += " "
    
    for y in range(HEIGHT):
        
        for x in range(WIDTH):
            vis_lab[2*y + 1] += (walls_v[x][y])
            vis_lab[2*y + 1] += (lab[x][y])
        vis_lab[2*y + 1] += (walls_v[x + 1][y])
        
        vis_lab[2*y + 2] = ' '
        for x in range(WIDTH):
            vis_lab[2*y + 2] += (walls_h[x][y+1])
            vis_lab[2*y + 2] += " "

    for y in range(len(vis_lab)):
        print(vis_lab[y])
        
    print('ВАЖНО! далее х вниз, а у вправо')
    print(np.array(lab))
    print(np.array(walls_v))
    print(np.array(walls_h))


if __name__ == "__main__":
    Лабиринт = generate()
    #FixMe в итоге по прямому вызову ничего не должно происходить...
    print("This module is not for direct call!")
