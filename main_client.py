from client2 import *
from visualisation import *
import pygame

def client_step(request):
    '''
    FixMe: Нужна документ-строка!!!!!!!!
    Args:
        request: запрос на сервер
    '''
    global sock
    global screen, width, height, data_client, objects_client
    global objects_server, x_client, y_client, x_server, y_server, step_flag

    data_client = ask_server(request, sock)  # в первый раз нужно передать 'NN'
    Return_client = visual_client(screen, width, height, data_client, objects_client,
                                  objects_server, x_client, y_client, x_server, y_server)
    Your_step(screen, width, height)
    key_and_knifes(screen, width, height, data_client, data_server)
    screen = Return_client[0]
    objects_client = Return_client[1]
    objects_server = Return_client[2]
    x_client = Return_client[3]
    y_client = Return_client[4]
    step_flag = 1
    if Return_client[6] == 0:
        objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                 [len(objects_client) - 2, len(objects_client) - 3],
                                                 [len(objects_server) - 2, len(objects_server) - 3])


IP = '192.168.0.102'
Port = 9090
sock = connection(IP, Port)

step_flag = int((sock.recv(1024)).decode('utf-8'))  # флаг хода игрока-сервера, получаем начальное значение от сервера
# 0 - наш шаг, 1 - шаг врага

data_client = 'NN00'
data_server = 'NN00'
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
screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))
pygame.display.update()
finished = False

visual_client(screen, width, height, 'NN00', objects_client,
                                                  objects_server, x_client, y_client, x_server, y_server)

visual_server(screen, width, height, 'NN00', objects_server, objects_client,
                                      x_server, y_server, x_client, y_client)

while not finished:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and step_flag == 0:
            if event.key == pygame.K_ESCAPE:
                finished = True
            elif event.key == pygame.K_UP:
                client_step('W')
            elif event.key == pygame.K_DOWN:
                client_step('S')
            elif event.key == pygame.K_RIGHT:
                client_step('D')
            elif event.key == pygame.K_LEFT:
                client_step('A')
            elif event.key == pygame.K_w:
                client_step('w')
            elif event.key == pygame.K_s:
                client_step('s')
            elif event.key == pygame.K_d:
                client_step('d')
            elif event.key == pygame.K_a:
                client_step('a')

    # ход соперника
    if step_flag == 1:
        data_server = catch_server_steps(sock)  # в первый раз нужно передать 'NN'
        Return_server = visual_server(screen, width, height, data_server, objects_server, objects_client,
                                      x_server, y_server, x_client, y_client)
        Opponent_step(screen, width, height)
        key_and_knifes(screen, width, height, data_client, data_server)
        screen = Return_server[0]
        objects_server = Return_server[1]
        objects_client = Return_server[2]
        x_server = Return_server[3]
        y_server = Return_server[4]
        if Return_server[6] == 0:
            objects_server, objects_client = visual_parts(width, height, objects_server, objects_client,
                                                      [len(objects_client) - 2, len(objects_client) - 3],
                                                      [len(objects_server) - 2, len(objects_server) - 3])

        step_flag = 0  # !!!!!!!!!!!!!!!!!!!!!!!!!
        pygame.event.clear() #Очищаем очередь

pygame.quit()
sock.close()
