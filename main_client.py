from client2 import *
from visualisation import *
import pygame

IP = '192.168.0.104'
Port = 9090
sock = connection(IP, Port)

step_flag = int((sock.recv(1024)).decode('utf-8'))  # флаг хода игрока-сервера, получаем начальное значение от сервера
# 0 - наш шаг, 1 - шаг врага

data_client = 'NN'
data_server = 'NN'
width = 1200
height = 800 
objects_client = [[]*1]*6
objects_server = [[]*1]*6
flag_client = 0
flag_server = 0
x_client = width/8
y_client = height/6
x_server = width*5/8
y_server = height/6
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

                if event.key == pygame.K_UP:

                        data_client = ask_server('W', sock)  # в первый раз нужно передать 'NN'
                        Return_client = visual_client(screen, width, height, flag_client, data_client, objects_client,
                                                      objects_server, x_client, y_client, x_server, y_server)
                        screen = Return_client[0]
                        flag_client = Return_client[1]
                        objects_client = Return_client[2]
                        objects_server = Return_client[3]
                        x_client = Return_client[4]
                        y_client = Return_client[5]
                        step_flag = 1

                if event.key == pygame.K_DOWN:

                    data_client = ask_server('S',
                                             sock)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, flag_client, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    flag_client = Return_client[1]
                    objects_client = Return_client[2]
                    objects_server = Return_client[3]
                    x_client = Return_client[4]
                    y_client = Return_client[5]
                    step_flag = 1

                if event.key == pygame.K_RIGHT:
                    data_client = ask_server('D',
                                             sock)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, flag_client, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    flag_client = Return_client[1]
                    objects_client = Return_client[2]
                    objects_server = Return_client[3]
                    x_client = Return_client[4]
                    y_client = Return_client[5]
                    step_flag = 1

                if event.key == pygame.K_LEFT:
                    data_client = ask_server('A',
                                             sock)  # в первый раз нужно передать 'NN'
                    Return_client = visual_client(screen, width, height, flag_client, data_client, objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)
                    screen = Return_client[0]
                    flag_client = Return_client[1]
                    objects_client = Return_client[2]
                    objects_server = Return_client[3]
                    x_client = Return_client[4]
                    y_client = Return_client[5]
                    step_flag = 1

    # ход соперника
    if step_flag == 1:
        data_server = catch_server_steps(sock)  # в первый раз нужно передать 'NN'
        Return_server = visual_server(screen, width, height, flag_server, data_server, objects_server, objects_client,
                                      x_server, y_server, x_client, y_client)
        screen = Return_server[0]
        flag_server = Return_server[1]
        objects_server = Return_server[2]
        objects_client = Return_server[3]
        x_server = Return_server[4]
        y_server = Return_server[5]

        step_flag = 0  # !!!!!!!!!!!!!!!!!!!!!!!!!

pygame.quit()
sock.close()