import numpy as np #При отладке так удобнее смотреть вывод лабиринта
import random

def find_neighbors(coords):
    '''
    Ищет соседей, в том числе следующий портал, которые не посещены

    Args:
        coords: координаты текущей клетки
    Returns:
        neighbors: множество неизведанных соседних

    '''
    neighbors = set()
    if coords[0] > 0 and generated_lab[coords[0] - 1][coords[1]] == 0:
        neighbors.add((coords[0] - 1, coords[1]))
    if coords[0] < WIDTH - 1 and generated_lab[coords[0] + 1][coords[1]] == 0:
        neighbors.add((coords[0] + 1, coords[1]))
    if coords[1] > 0 and generated_lab[coords[0]][coords[1] - 1] == 0:
        neighbors.add((coords[0], coords[1] - 1))
    if coords[1] < HEIGHT - 1 and generated_lab[coords[0]][coords[1] + 1] == 0:
        neighbors.add((coords[0], coords[1] + 1))
        
    if lab[coords[0]][coords[1]] > '0' and lab[coords[0]][coords[1]] < str(NUM_PORTAL):
        next_portal = int(lab[coords[0]][coords[1]]) + 1
        next_portal_coords = (chosen_cells[next_portal] % WIDTH,
                          chosen_cells[next_portal] // WIDTH)
        if generated_lab[next_portal_coords[0]][next_portal_coords[1]] == 0:
            neighbors.add(next_portal_coords)
            
    return neighbors
            
def generate(coords):
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
    generated_lab[coords[0]][coords[1]] = 1 #Текущая клетка посещенная
    
    neighbors = find_neighbors(coords)
    while len(neighbors) != 0: #Пока остались непосещенные соседние клетки
        cell = random.choice(list(neighbors))
        if coords[0] == cell[0] and abs(coords[1] - cell[1]) == 1:
            walls_h[coords[0]][max(coords[1],cell[1])] = '*'
        elif coords[1] == cell[1] and abs(coords[0] - cell[0]) == 1:
            walls_v[max(coords[0],cell[0])][coords[1]] = '*'
        generate(cell)
        neighbors = find_neighbors(coords)


WIDTH = random.randint(2, 10)
if WIDTH <= 4:
    HEIGHT = random.randint(4, 10)
else:
    HEIGHT = random.randint(2, 10)

SIZE = WIDTH, HEIGHT

NUM_PORTAL = random.randint(3, min(9, WIDTH*HEIGHT // 5))
#Должно быть строго меньше 10, иначе мы имеем 2 цифры :(

#Матрица с лабирирнтом
lab = [['0' for y in range(HEIGHT)] for x in range(WIDTH)] #Заполняем лабиринт "нулями"

#Матрица с горизонтальными стенами
walls_h = [['#' for y in range(HEIGHT + 1)] for x in range(WIDTH)] #Заполняем матрицу стен стенами "#"

#Матрица с вертикальными стенами
walls_v = [['#' for y in range(HEIGHT)] for x in range(WIDTH + 1)] #Заполняем матрицу стен стенами "#"

#Рабочая матрица для генерации
generated_lab = [[0 for y in range(HEIGHT)] for x in range(WIDTH)] #Заполняем лабиринт нулями



chosen_cells = random.sample(range(WIDTH * HEIGHT), NUM_PORTAL+3) #Выбираем случайные клетки для объектов

lab[chosen_cells[0] % WIDTH][chosen_cells[0] // WIDTH] = 'H' #Больница = Hospital
lab[chosen_cells[-1] % WIDTH][chosen_cells[-1] // WIDTH] = 'A' #Арсенал
lab[chosen_cells[-2] % WIDTH][chosen_cells[-2] // WIDTH] = 'K' #Ключ
for i in range(1, len(chosen_cells) - 2):
    lab[chosen_cells[i] % WIDTH][chosen_cells[i] // WIDTH] = str(i) #В этих клетках порталы
    
print(np.array(lab))

hosp_coords = [chosen_cells[0] % WIDTH, chosen_cells[0] // WIDTH] #Координаты больницы

generate(hosp_coords) #Запускаем рекурсию

# ВАЖНО! При отображении матрицу надо транспонировать(или считать х вниз, а у вправо)
print(np.array(walls_v))
print(np.array(walls_h))

#if __name__ == "__main__":
#    print("This module is not for direct call!")
