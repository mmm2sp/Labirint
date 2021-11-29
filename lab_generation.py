import numpy as np #При отладке так удобнее смотреть вывод лабиринта
import random

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
    global generation_lab, walls_v, walls_h
    #Матрица с вертикальными стенами
    walls_v = [['#' for y in range(HEIGHT)] for x in range(WIDTH + 1)] #Заполняем матрицу стен стенами "#"
    #Матрица с горизонтальными стенами
    walls_h = [['#' for y in range(HEIGHT + 1)] for x in range(WIDTH)] #Заполняем матрицу стен стенами "#"
    #Рабочая матрица для генерации
    generation_lab = [[0 for y in range(HEIGHT)] for x in range(WIDTH)] #Заполняем лабиринт нулями

    hosp_coords = [chosen_cells[0] % WIDTH, chosen_cells[0] // WIDTH] #Координаты больницы
    generate_walls(hosp_coords) #Запускаем рекурсию

    maximum = WIDTH * 2 + HEIGHT * 2
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
        next_portal_coords = (chosen_cells[next_portal] % WIDTH,
                          chosen_cells[next_portal] // WIDTH)
        if generation_lab[next_portal_coords[0]][next_portal_coords[1]] == 0:
            neighbors.add(next_portal_coords)
            
    return neighbors
            
def generate_walls(coords):
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
    '''
    global walls_v, walls_h
    generation_lab[coords[0]][coords[1]] = 1 #Текущая клетка посещенная
    
    neighbors = find_neighbors(coords)
    while len(neighbors) != 0: #Пока остались непосещенные соседние клетки
        cell = random.choice(list(neighbors))
        if coords[0] == cell[0] and abs(coords[1] - cell[1]) == 1:
            walls_h[coords[0]][max(coords[1],cell[1])] = '*'
        elif coords[1] == cell[1] and abs(coords[0] - cell[0]) == 1:
            walls_v[max(coords[0],cell[0])][coords[1]] = '*'
        generate_walls(cell)
        neighbors = find_neighbors(coords)

def generate():
    '''
    Главная функция генерации. Генерирует весь лабиринт
    '''
    global SIZE, WIDTH, HEIGHT, NUM_PORTAL, chosen_cells, lab
    
    WIDTH = random.randint(2, 10)
    if WIDTH <= 4:
        HEIGHT = random.randint(4, 10)
    else:
        HEIGHT = random.randint(2, 10)

    SIZE = WIDTH, HEIGHT
    NUM_PORTAL = random.randint(2, 5)
    #Должно быть строго меньше 10, иначе мы имеем 2 цифры :(
        
    lab, chosen_cells = generate_objects_in_lab()
    generate_walls_in_lab()

    # ВАЖНО! При отображении матрицу надо транспонировать(или считать х вниз, а у вправо)
    print(np.array(lab))
    print(np.array(walls_v))
    print(np.array(walls_h))




if __name__ == "__main__":
    generate()
    #FixMe в итоге по рпямому вызову ничего не должно происходить...
    print("This module is not for direct call!")
