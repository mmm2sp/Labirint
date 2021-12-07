from server2 import *
from visualisation import *
from basic_pictures import *
import pygame
from lab_generation import generate
from lab_classes import Player
from lab_classes import Cell

IP = '192.168.0.102'
Port = 9090
conn = connection(IP, Port)

step_flag = 1  # флаг хода игрока-сервера, 1 - наш шаг, 0 - шаг врага. можно прикрутить рандом
conn.send(str(step_flag).encode('utf-8'))  # передача начального флага клиенту

data_client = 'NN'  # клиент - тот, кто рисуется слева
data_server = 'NN'  # сервер - тот, кто справа (небольшая путаница в обозначениях)
width = 1200
height = 800
objects_client = [[]]
objects_server = [[]]

N_client = len(objects_client)
N_server = len(objects_server)

# то какие фрагменты мы рисуем сверху экрана
client_pict = [N_client - 2, N_client - 3]
server_pict = [N_server - 2, N_server - 3]

x_client = width / 4
y_client = height * 2 / 3
x_server = width * 3 / 4
y_server = height * 2 / 3
Return_server = []
Return_client = []
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
pygame.display.update()
finished = False

visual_client(screen, width, height, 'NN', objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)

visual_server(screen, width, height, 'NN', objects_server, objects_client,
                                      x_server, y_server, x_client, y_client)

лабиринт, игроки = generate()

while not finished:

    # этот кусок не выполняется
    # рисование пройденных фрагментов
    # рисование левого у клиента
    pygame.time.Clock().tick(60)
    print(N_client)
    if client_pict[0] >= 0:
        print(2)
        x = objects_client[client_pict[0]][0].x
        y = objects_client[client_pict[0]][0].y
        dx = 0
        dy = 0
        if x != 3/8 * width and y != 1/6 * height:
            dx = 3/8 * width - x
            dy = 1/6 * height - y
            print('dfdfd')
        for i in objects_client[client_pict[0]]:
            print('aaaaaa')
            i.x += dx
            i.y += dy
            i.draw()
            pygame.display.update()
    # правого
    if client_pict[1] >= 0:
        x = objects_client[client_pict[1]][0].x
        y = objects_client[client_pict[1]][0].y
        dx = 0
        dy = 0
        if x != 1/8 * width and y != 1/6 * height:
            dx = 1/8 * width - x
            dy = 1/6 * height - y
        for i in objects_client[client_pict[1]]:
            i.x += dx
            i.y += dy
            i.draw()
            pygame.display.update()

    # рисование левого у сервера
    if server_pict[0] >= 0:
        x = objects_server[server_pict[0]][0].x
        y = objects_server[server_pict[0]][0].y
        dx = 0
        dy = 0
        if x != 7 / 8 * width and y != 1 / 6 * height:
            dx = 7 / 8 * width - x
            dy = 1 / 6 * height - y
        for i in objects_server[server_pict[0]]:
            i.x += dx
            i.y += dy
            i.draw()
            pygame.display.update()
    # правого
    if server_pict[1] >= 0:
        x = objects_server[server_pict[1]][0].x
        y = objects_server[server_pict[1]][0].y
        dx = 0
        dy = 0
        if x != 5 / 8 * width and y != 1 / 6 * height:
            dx = 5 / 8 * width - x
            dy = 1 / 6 * height - y
        for i in objects_server[server_pict[1]]:
            i.x += dx
            i.y += dy
            i.draw()
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.KEYDOWN:
            if step_flag == 1:

                antibag = 0  # чтобы инфа отправлялась на сервер только 1 раз

                if event.key == pygame.K_UP and antibag == 0:
                    data_client, лабиринт, игроки = игроки[1].move('W', лабиринт, игроки)  # в первый раз нужно передать 'NN' ПОРАБОТАТЬ!!!!!!!!!!
                    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    objects_client = Return_client[1]
                    objects_server = Return_client[2]
                    x_client = Return_client[3]
                    y_client = Return_client[4]
                    step_flag = 0

                    say_to_client_about_serv_step(data_client, conn)
                    # изменение лабиринта в зависимости от data_client!!!!!
                    antibag = 1

                if event.key == pygame.K_DOWN and antibag == 0:
                    data_client, лабиринт, игроки = игроки[1].move('S', лабиринт, игроки)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    objects_client = Return_client[1]
                    objects_server = Return_client[2]
                    x_client = Return_client[3]
                    y_client = Return_client[4]
                    step_flag = 0

                    say_to_client_about_serv_step(data_client, conn)
                    # изменение лабиринта
                    antibag = 1

                if event.key == pygame.K_RIGHT and antibag == 0:
                    data_client, лабиринт, игроки = игроки[1].move('D', лабиринт, игроки)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    objects_client = Return_client[1]
                    objects_server = Return_client[2]
                    x_client = Return_client[3]
                    y_client = Return_client[4]
                    step_flag = 0

                    say_to_client_about_serv_step(data_client, conn)
                    # изменение лабиринта
                    antibag = 1

                if event.key == pygame.K_LEFT and antibag == 0:
                    data_client, лабиринт, игроки = игроки[1].move('A', лабиринт, игроки)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    objects_client = Return_client[1]
                    objects_server = Return_client[2]
                    x_client = Return_client[3]
                    y_client = Return_client[4]
                    step_flag = 0

                    say_to_client_about_serv_step(data_client, conn)
                    # изменение лабиринта
                    antibag = 1

    # ход соперника
    if step_flag == 0:
        # обработка хода соперника

        data_server, лабиринт, игроки = answer_to_client_step(лабиринт, conn, игроки)  # в первый раз нужно передать 'NN'

        Return_server = visual_server(screen, width, height, data_server, objects_server, objects_client,
                                      x_server, y_server, x_client, y_client)
        screen = Return_server[0]
        objects_server = Return_server[1]
        objects_client = Return_server[2]
        x_server = Return_server[3]
        y_server = Return_server[4]

        # изменение лабиринта!!!!
        pygame.event.clear()  # возможно исправит баг
        step_flag = 1  # !!!!!!!!!!!!!!!!! возможно будет ошибка


pygame.quit()
conn.close()