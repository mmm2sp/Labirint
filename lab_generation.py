import numpy as np #При отладке так удобнее смотреть вывод лабиринта
import random

SIZE = WIDTH, HEIGHT = 5, 5
NUM_PORTAL = 5
empty_lab = [['0' for x in range(WIDTH)] for y in range(HEIGHT)] #Заполняем лабиринт нулями

choosen_cells = random.sample(range(WIDTH * HEIGHT), NUM_PORTAL+3) #Выбираем случайные клетки для объектов

empty_lab[choosen_cells[0] % WIDTH][choosen_cells[0] // WIDTH] = 'H' #Больница = Hospital
empty_lab[choosen_cells[1] % WIDTH][choosen_cells[1] // WIDTH] = 'A' #Арсенал
empty_lab[choosen_cells[2] % WIDTH][choosen_cells[2] // WIDTH] = 'K' #Ключ
for i in range(3, len(choosen_cells)):
    empty_lab[choosen_cells[i] % WIDTH][choosen_cells[i] // WIDTH] = str(i-2) #В этих клетках порталы
    
print(np.array(empty_lab))

#if __name__ == "__main__":
#    print("This module is not for direct call!")
