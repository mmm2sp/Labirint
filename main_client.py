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
    global screen, width, height, flag_client, data_client, objects_client
    global objects_server, x_client, y_client, x_server, y_server, step_flag

    data_client = ask_server(request, sock)  # в первый раз нужно передать 'NN'
    Return_client = visual_client(screen, width, height, flag_client, data_client, objects_client,
                                  objects_server, x_client, y_client, x_server, y_server)
    screen = Return_client[0]
    flag_client = Return_client[1]
    objects_client = Return_client[2]
    objects_server = Return_client[3]
    x_client = Return_client[4]
    y_client = Return_client[5]
    step_flag = 1
    pygame.event.clear() #Очищаем очередь
    



IP = '192.168.1.65'
Port = 9090
sock = connection(IP, Port)

step_flag = int((sock.recv(1024)).decode('utf-8'))  # флаг хода игрока-сервера, получаем начальное значение от сервера
# 0 - наш шаг, 1 - шаг врага

data_client = 'NN'
data_server = 'NN'
width = 1000
height = 600 
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
clock = pygame.time.Clock()
FPS = 20

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and step_flag == 0:
            if event.key == pygame.K_UP:
                client_step('W')
            elif event.key == pygame.K_DOWN:
                client_step('S')
            elif event.key == pygame.K_RIGHT:
                client_step('D')
            elif event.key == pygame.K_LEFT:
                client_step('A')
    
    if step_flag == 1: # ход соперника
        data_server = catch_server_steps(sock)  # в первый раз нужно передать 'NN'
        Return_server = visual_server(screen, width, height, flag_server, data_server, objects_server, objects_client,
                                      x_server, y_server, x_client, y_client)
        screen = Return_server[0]
        flag_server = Return_server[1]
        objects_server = Return_server[2]
        objects_client = Return_server[3]
        x_server = Return_server[4]
        y_server = Return_server[5]
        pygame.event.clear() #Очищаем очередь
        step_flag = 0

pygame.quit()
sock.close()
