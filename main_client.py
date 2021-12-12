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
    global screen, width, height, data_client, objects_player
    global objects_enemy, x_player, y_player, x_enemy, y_enemy, step_flag

    data_client = ask_server(request, sock)  # в первый раз нужно передать 'NN'
    Return_client = visual_player(screen, width, height, data_client, objects_player,
                                  objects_enemy, x_player, y_player, x_enemy, y_enemy)
    enemy_step(screen, width, height)
    key_and_knifes(screen, width, height, data_client, data_server)
    screen = Return_client[0]
    objects_player = Return_client[1]
    objects_enemy = Return_client[2]
    x_player = Return_client[3]
    y_player = Return_client[4]
    x_enemy = Return_client[5]
    y_enemy = Return_client[6]
    step_flag = 1
    if Return_client[8] == 0:
        objects_enemy, objects_player = visual_parts(width, height, objects_enemy, objects_player,
                                                 [len(objects_player) - 2, len(objects_player) - 3],
                                                 [len(objects_enemy) - 2, len(objects_enemy) - 3])



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
screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))
menu_client(screen, width, height)
inf = ['', 0]
IP = ''
while inf[1] != 1:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        inf = Typing(IP, width/2, height/2, event, screen)
        IP = inf[0]
        if inf[1] == 1:
            break
IP = inf[0]
Port = 9090
sock = connection(IP, Port)

step_flag = int((sock.recv(1024)).decode('utf-8'))  # флаг хода игрока-сервера, получаем начальное значение от сервера
# 0 - наш шаг, 1 - шаг врага

finished = False

visual_player(screen, width, height, 'NN00', objects_player,
                                                  objects_enemy, x_player, y_player, x_enemy, y_enemy)

visual_enemy(screen, width, height, 'NN00', objects_enemy, objects_player,
                                      x_enemy, y_enemy, x_player, y_player)

if step_flag == 0:
    player_step(screen, width, height)
elif step_flag == 1:
    enemy_step(screen, width, height)
pygame.display.update()

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
        Return_server = visual_enemy(screen, width, height, data_server, objects_enemy, objects_player,
                                      x_enemy, y_enemy, x_player, y_player)
        player_step(screen, width, height)
        key_and_knifes(screen, width, height, data_client, data_server)
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

        step_flag = 0  # !!!!!!!!!!!!!!!!!!!!!!!!!
        pygame.event.clear() #Очищаем очередь

pygame.quit()
sock.close()
