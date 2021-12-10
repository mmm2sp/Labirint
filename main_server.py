from server2 import *
from visualisation import *
from basic_pictures import *
import pygame
from lab_generation import generate

def serv_step(request):
    '''
    FixMe: Нужна документ-строка!!!!!!!!
    Args:
        request: запрос в лабиринт
    '''
    global data_client, лабиринт, игроки
    global screen, objects_client, objects_server
    global x_client, y_client, step_flag

    data_client, лабиринт, игроки = игроки[1].move(request, лабиринт, игроки)
    # в первый раз нужно передать 'NN' ПОРАБОТАТЬ!!!!!!!!!!
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

IP = socket.gethostbyname(socket.gethostname())
print(IP)

Port = 9090
conn = connection(IP, Port)

step_flag = 1  # флаг хода игрока-сервера, 1 - наш шаг, 0 - шаг врага. можно прикрутить рандом
conn.send(str(step_flag).encode('utf-8'))  # передача начального флага клиенту

data_client = 'NN00'  # клиент - тот, кто рисуется слева
data_server = 'NN00'  # сервер - тот, кто справа (небольшая путаница в обозначениях)
width = 1000
height = 600
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

visual_client(screen, width, height, 'NN00', objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)

visual_server(screen, width, height, 'NN00', objects_server, objects_client,
                                      x_server, y_server, x_client, y_client)

лабиринт, игроки = generate()

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and step_flag == 1:
            if event.key == pygame.K_ESCAPE:
                finished = True
                #FixMe: не должна вылетать ошибка при завершении игры
            elif event.key == pygame.K_UP:
                serv_step('W')
            elif event.key == pygame.K_DOWN:
                serv_step('S')
            elif event.key == pygame.K_RIGHT:
                serv_step('D')
            elif event.key == pygame.K_LEFT:
                serv_step('A')
            elif event.key == pygame.K_w:
                serv_step('w')
            elif event.key == pygame.K_s:
                serv_step('s')
            elif event.key == pygame.K_d:
                serv_step('d')
            elif event.key == pygame.K_a:
                serv_step('a')

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
            step_flag = 1  # !!!!!!!!!!!!!!!!! возможно будет ошибка
            pygame.event.clear()  # возможно исправит баг
            

pygame.quit()
conn.close()
