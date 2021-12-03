from lab_generation import generate
from lab_classes import Player
from lab_classes import Cell

def test_function():
    лабиринт, игроки = generate()
    направление = 'W'

    
    while направление != '0':
        for i in range(2):
            print('Ходит игрок', i)
            направление = input()
            ответ, лабиринт, игроки = игроки[i].move(направление, лабиринт, игроки)
            print(ответ)
            cell = лабиринт[игроки[i].coords[0]][игроки[i].coords[1]]
            print(cell.typ)
            print(cell.coords)
            print(игроки[i].key)



def check_move(move, num_player, labirint, player):
    '''
    :param move: строка с ходом (один символ)
    :param num_player: число 0 или 1 в зависимости от хода игрока
    :param labirint: Матрица с лабиринтом
    :param player: список с координатами всех (двух) игроков
    Returns:
        answer: строка с ответом
        labirint: Матрица с лабиринтом
        player: список с координатами всех (двух) игроков
    
    global labirint, player #Матрица с лабиринтом, список с координатами всех (двух) игроков
    answer = ''
    x_coord = player[num_player][0]
    y_coord = player[num_player][1]
    if move == 'W':
        answer = labirint[x_coord][y_coord].move_up()
    if move == 'S':
        answer = labirint[x_coord][y_coord].move_down()
    if move == 'A':
        answer = labirint[x_coord][y_coord].move_left()
    if move == 'D':
        answer = labirint[x_coord][y_coord].move_right()'''

if __name__ == "__main__":
    print("This module is not for direct call!")
    test_function()
    #FixMe в итоге по прямому вызову ничего не должно происходить...
   
