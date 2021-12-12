from server2 import *
from visualisation import *
import random
import pygame
from lab_generation import generate


def serv_step(request):
    '''
    Функция обрабатывает ход сервера: рисует изменения вследствие хода на экране и отправляет данные о ходе на
    удаленный компьютер соперника.
    Args:
        request: запрос в лабиринт (направление стрельбы (wasd) или ходьбы(WASD))
    '''

    global data_client, лабиринт, игроки
    global screen, objects_player, objects_enemy
    global x_player, y_player, x_enemy, y_enemy, step_flag

    # запрос в матрицу лабиринта для совершения хода
    data_client, лабиринт, игроки = игроки[1].move(request, лабиринт, игроки)
    # визуализация хода
    say_to_client_about_serv_step(data_client, conn)
    Return_client = visual_player(screen, width, height, data_client, objects_player,
                                  objects_enemy, x_player, y_player, x_enemy, y_enemy)
    enemy_step(screen, width, height)

    screen = Return_client[0]
    objects_player = Return_client[1]
    objects_enemy = Return_client[2]
    x_player = Return_client[3]
    y_player = Return_client[4]
    x_enemy = Return_client[5]
    y_enemy = Return_client[6]
    step_flag = 0

    # отдельно рассмотрен случай окончания игры для избежания бага
    if Return_client[8] == 0:
        objects_enemy, objects_player = visual_parts(width, height, objects_enemy, objects_player,
                                                     [len(objects_player) - 2, len(objects_player) - 3],
                                                     [len(objects_enemy) - 2, len(objects_enemy) - 3])
        # случай, если произошло убийство
        if data_client[1] == 'G':
            key_and_knifes(screen, width, height, data_client, 'AB00')
        else:
            key_and_knifes(screen, width, height, data_client, data_server)
    # сообщение сопернику о ходе
    return Return_client[8]


IP = socket.gethostbyname(socket.gethostname())

width = 1000
height = 600
finished = False
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

conn = False
Port = 9090

# рисование главного меню перед стартом игры
while not conn:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        # в случае нажатия на клавишу подключиться, создает соедиение с клиентом
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if (x > width / 2 - 200) and (x < width / 2 + 200) and (y > height / 2 - 100) and (y < height / 2 + 100):
                conn = connection(IP, Port)
        menu_server(screen, width, height, IP)

# кто ходит первым выбирается случайным образом
step_flag = random.randint(0, 1)  # флаг хода игрока-сервера, 1 - наш шаг, 0 - шаг врага. можно прикрутить рандом
conn.send(str(step_flag).encode('utf-8'))  # передача начального флага клиенту

data_client = 'NN00'  # клиент - тот, кто рисуется слева
data_server = 'NN00'  # сервер - тот, кто справа (небольшая путаница в обозначениях)

# открытые куски карты
objects_player = [[]]
objects_enemy = [[]]

x_player = width / 4
y_player = height * 2 / 3
x_enemy = width * 3 / 4
y_enemy = height * 2 / 3
Return_server = []
Return_client = []

visual_player(screen, width, height, 'NN00', objects_player,
              objects_enemy, x_player, y_player, x_enemy, y_enemy)
visual_enemy(screen, width, height, 'NN00', objects_enemy,
             objects_player, x_enemy, y_enemy, x_player, y_player)

# начальное рисование флажка над ходящим игроком
if step_flag == 1:
    player_step(screen, width, height)
elif step_flag == 0:
    enemy_step(screen, width, height)
pygame.display.update()

# создание лабиринта
лабиринт, игроки = generate()

finished = False

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # ход игрока
        elif event.type == pygame.KEYDOWN and step_flag == 1:
            if event.key == pygame.K_ESCAPE:
                finished = True
                # FixMe: не должна вылетать ошибка при завершении игры
            elif event.key == pygame.K_UP:
                # проверка на конец игры
                if serv_step('W') == 1:
                    finished = True
            elif event.key == pygame.K_DOWN:
                if serv_step('S') == 1:
                    finished = True
            elif event.key == pygame.K_RIGHT:
                if serv_step('D') == 1:
                    finished = True
            elif event.key == pygame.K_LEFT:
                if serv_step('A') == 1:
                    finished = True
            elif event.key == pygame.K_w:
                if serv_step('w') == 1:
                    finished = True
            elif event.key == pygame.K_s:
                if serv_step('s') == 1:
                    finished = True
            elif event.key == pygame.K_d:
                if serv_step('d') == 1:
                    finished = True
            elif event.key == pygame.K_a:
                if serv_step('a') == 1:
                    finished = True

    # ход соперника
    if step_flag == 0 and (finished is False):
        # обработка хода соперника, аналогично ходу игрока

        data_server, лабиринт, игроки = answer_to_client_step(лабиринт, conn,
                                                              игроки)
        Return_server = visual_enemy(screen, width, height, data_server, objects_enemy, objects_player,
                                     x_enemy, y_enemy, x_player, y_player)
        player_step(screen, width, height)

        screen = Return_server[0]
        objects_enemy = Return_server[1]
        objects_player = Return_server[2]
        x_enemy = Return_server[3]
        y_enemy = Return_server[4]
        x_player = Return_server[5]
        y_player = Return_server[6]

        if Return_server[8] == 0:
            objects_enemy, objects_player = visual_parts(width, height, objects_enemy, objects_player,
                                                         [len(objects_player) - 2, len(objects_player) - 3],
                                                         [len(objects_enemy) - 2, len(objects_enemy) - 3])
            # случай, если произошло убийство
            if data_server[1] == 'G':
                key_and_knifes(screen, width, height, 'AB00', data_server)
            else:
                key_and_knifes(screen, width, height, data_client, data_server)
        if Return_server[8] == 1:
            finished = True

        step_flag = 1
        pygame.event.clear()

pygame.quit()
conn.close()
