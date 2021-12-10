from server2 import *
from visualisation import *
from basic_pictures import *
import pygame
from lab_generation import generate
from lab_classes import Player
from lab_classes import Cell

IP = socket.gethostbyname(socket.gethostname())
print(IP)

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

                    objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                                  [len(objects_client)-2, len(objects_client)-3],
                                                                  [len(objects_server)-2, len(objects_server)-3])
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

                    objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                                  [len(objects_client)-2, len(objects_client)-3],
                                                                  [len(objects_server)-2, len(objects_server)-3])
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

                    objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                                  [len(objects_client) - 2, len(objects_client) - 3],
                                                                  [len(objects_server) - 2, len(objects_server) - 3])
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

                    objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                                  [len(objects_client) - 2, len(objects_client) - 3],
                                                                  [len(objects_server) - 2, len(objects_server) - 3])
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

            objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                          [len(objects_client) - 2, len(objects_client) - 3],
                                                          [len(objects_server) - 2, len(objects_server) - 3])
            # изменение лабиринта!!!!
            pygame.event.clear()  # возможно исправит баг
            step_flag = 1  # !!!!!!!!!!!!!!!!! возможно будет ошибка

pygame.quit()
conn.close()