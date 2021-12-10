from client2 import *
from visualisation import *
import pygame

IP = '192.168.0.102'
Port = 9090
sock = connection(IP, Port)

step_flag = int((sock.recv(1024)).decode('utf-8'))  # флаг хода игрока-сервера, получаем начальное значение от сервера
# 0 - наш шаг, 1 - шаг врага

data_client = 'NN'
data_server = 'NN'
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
screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))
pygame.display.update()
finished = False

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        elif event.type == pygame.KEYDOWN:
            if step_flag == 0:

                antibag = 0  # чтобы инфа отправлялась на сервер только 1 раз

                if event.key == pygame.K_UP and antibag == 0:

                    data_client = ask_server('W', sock)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                                      objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    objects_client = Return_client[1]
                    objects_server = Return_client[2]
                    x_client = Return_client[3]
                    y_client = Return_client[4]
                    step_flag = 1

                    objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                                      [len(objects_client) - 2, len(objects_client) - 3],
                                                                      [len(objects_server) - 2, len(objects_server) - 3])
                    antibag = 1

                if event.key == pygame.K_DOWN and antibag == 0:

                    data_client = ask_server('S',
                                             sock)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    objects_client = Return_client[1]
                    objects_server = Return_client[2]
                    x_client = Return_client[3]
                    y_client = Return_client[4]
                    step_flag = 1

                    objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                                  [len(objects_client) - 2, len(objects_client) - 3],
                                                                  [len(objects_server) - 2, len(objects_server) - 3])
                    antibag = 1

                if event.key == pygame.K_RIGHT and antibag == 0:
                    data_client = ask_server('D',
                                             sock)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    objects_client = Return_client[1]
                    objects_server = Return_client[2]
                    x_client = Return_client[3]
                    y_client = Return_client[4]
                    step_flag = 1
                    objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                                  [len(objects_client) - 2, len(objects_client) - 3],
                                                                  [len(objects_server) - 2, len(objects_server) - 3])
                    antibag = 1

                if event.key == pygame.K_LEFT and antibag == 0:
                    data_client = ask_server('A',
                                             sock)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    objects_client = Return_client[1]
                    objects_server = Return_client[2]
                    x_client = Return_client[3]
                    y_client = Return_client[4]
                    step_flag = 1
                    objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                                  [len(objects_client) - 2, len(objects_client) - 3],
                                                                  [len(objects_server) - 2, len(objects_server) - 3])
                    antibag = 1

    # ход соперника
    if step_flag == 1:
        data_server = catch_server_steps(sock)  # в первый раз нужно передать 'NN'
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

        step_flag = 0  # !!!!!!!!!!!!!!!!!!!!!!!!!

pygame.quit()
sock.close()