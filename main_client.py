from client2 import *
from visualisation import *
import pygame


def client_step(request):
    '''
    Функция обрабатывает ход клиента: отправляет запрос на сервер о своем ходе,
    получает ответ от сервера, рисует изменения в случае удачного хода
    Args:
        request: запрос на сервер (направление стрельбы (wasd) или ходьбы(WASD))
    '''
    global sock
    global screen, width, height, data_client, objects_player
    global objects_enemy, x_player, y_player, x_enemy, y_enemy, step_flag

    # запрос на сервер, сообщение серверу о ходе
    data_client = ask_server(request, sock)
    # рисование изменений
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
    step_flag = 1

    # отдельно рассмотрен случай окончания игры для избежания бага
    if Return_client[8] == 0:
        objects_enemy, objects_player = visual_parts(width, height, objects_enemy, objects_player,
                                                     [len(objects_player) - 2, len(objects_player) - 3],
                                                     [len(objects_enemy) - 2, len(objects_enemy) - 3])
        key_and_knifes(screen, width, height, data_client, data_server)

    return Return_client[8]


data_client = 'NN00'
data_server = 'NN00'
width = 1000
height = 600
objects_player = [[]]
objects_enemy = [[]]

x_player = width / 4
y_player = height * 2 / 3
x_enemy = width * 3 / 4
y_enemy = height * 2 / 3
Return_server = []
Return_client = []
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

# рисование стортового меню
menu_client(screen, width, height)
inf = ['', 0]
IP = ''
while inf[1] != 1:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # ввод адреса сервера, к которому подключаемся
        inf = Typing(IP, width / 2, height / 2, event, screen)
        IP = inf[0]
        # в случае нажатия на пробел, производим подключение
        if inf[1] == 1:
            break
IP = inf[0]
Port = 9090
sock = connection(IP, Port)

step_flag = int((sock.recv(1024)).decode('utf-8'))  # флаг хода игрока-сервера, получаем начальное значение от сервера
# 0 - наш шаг, 1 - шаг врага

visual_player(screen, width, height, 'NN00', objects_player,
              objects_enemy, x_player, y_player, x_enemy, y_enemy)

visual_enemy(screen, width, height, 'NN00', objects_enemy, objects_player,
             x_enemy, y_enemy, x_player, y_player)

if step_flag == 0:
    player_step(screen, width, height)
elif step_flag == 1:
    enemy_step(screen, width, height)
pygame.display.update()

finished = False

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # ход игрока
        elif event.type == pygame.KEYDOWN and step_flag == 0:
            if event.key == pygame.K_ESCAPE:
                finished = True
            elif event.key == pygame.K_UP:
                # проверка на конец игры
                if client_step('W') == 1:
                    finished = True
            elif event.key == pygame.K_DOWN:
                if client_step('S') == 1:
                    finished = True
            elif event.key == pygame.K_RIGHT:
                if client_step('D') == 1:
                    finished = True
            elif event.key == pygame.K_LEFT:
                if client_step('A') == 1:
                    finished = True
            elif event.key == pygame.K_w:
                if client_step('w') == 1:
                    finished = True
            elif event.key == pygame.K_s:
                if client_step('s') == 1:
                    finished = True
            elif event.key == pygame.K_d:
                if client_step('d') == 1:
                    finished = True
            elif event.key == pygame.K_a:
                if client_step('a') == 1:
                    finished = True

    # ход соперника, аналогичен ходу игрока
    if step_flag == 1 and (finished is False):
        data_server = catch_server_steps(sock)
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
            key_and_knifes(screen, width, height, data_client, data_server)

        if Return_server[8] == 1:
            finished = True

        step_flag = 0
        pygame.event.clear()  # очистка очереди для избежания багов

pygame.quit()
sock.close()
