from server2 import *
from visualisation import *
import pygame
from lab_generation import generate


def serv_step(request):
    '''
    FixMe: Нужна документ-строка!!!!!!!!
    Args:
        request: запрос в лабиринт
    '''
    global data_client, лабиринт, игроки
    global screen, flag_client, objects_client, objects_server
    global x_client, y_client, step_flag

    data_client, лабиринт, игроки = игроки[1].move(request, лабиринт, игроки)
    # в первый раз нужно передать 'NN' ПОРАБОТАТЬ!!!!!!!!!!
    Return_client = visual_client(screen, width, height, flag_client, data_client, objects_client,
                                  objects_server, x_client, y_client, x_server, y_server)
    screen = Return_client[0]
    flag_client = Return_client[1]
    objects_client = Return_client[2]
    objects_server = Return_client[3]
    x_client = Return_client[4]
    y_client = Return_client[5]
    step_flag = 0

    say_to_client_about_serv_step(data_client, conn)
    # изменение лабиринта в зависимости от data_client!!!!!



IP = '192.168.1.65'
Port = 9090
conn = connection(IP, Port)

step_flag = 1  # флаг хода игрока-сервера, 1 - наш шаг, 0 - шаг врага. можно прикрутить рандом
conn.send(str(step_flag).encode('utf-8'))  # передача начального флага клиенту

data_client = 'NN'  # клиент - тот, кто рисуется слева
data_server = 'NN'  # сервер - тот, кто справа (небольшая путаница в обозначениях)
width = 1000
height = 600
objects_client = [[] * 1] * 6
objects_server = [[] * 1] * 6
flag_client = 0
flag_server = 0
x_client = width / 8
y_client = height / 6
x_server = width * 5 / 8
y_server = height / 6
Return_server = []
Return_client = []
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
pygame.display.update()
finished = False
clock = pygame.time.Clock()
FPS = 20

visual_client(screen, width, height, flag_client, 'NN', objects_client,
              objects_server, x_client, y_client, x_server, y_server)

visual_server(screen, width, height, flag_server, 'NN', objects_server, objects_client,
              x_server, y_server, x_client, y_client)

лабиринт, игроки = generate() #Создание лабиринта

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and step_flag == 1:
            if event.key == pygame.K_UP:
                serv_step('W')
            elif event.key == pygame.K_DOWN:
                serv_step('S')
            elif event.key == pygame.K_RIGHT:
                serv_step('D')
            elif event.key == pygame.K_LEFT:
                serv_step('A')

    if step_flag == 0: # обработка хода соперника
        data_server, лабиринт, игроки = answer_to_client_step(лабиринт, conn, игроки)
        # в первый раз нужно передать 'NN'
        Return_server = visual_server(screen, width, height, flag_server, data_server, objects_server, objects_client,
                                      x_server, y_server, x_client, y_client)
        screen = Return_server[0]
        flag_server = Return_server[1]
        objects_server = Return_server[2]
        objects_client = Return_server[3]
        x_server = Return_server[4]
        y_server = Return_server[5]
        pygame.event.clear() #Очищаем очередь
        step_flag = 1


pygame.quit()
conn.close()
