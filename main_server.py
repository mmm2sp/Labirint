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
    global screen, objects_player, objects_enemy
    global x_player, y_player, x_enemy, y_enemy, step_flag

    data_client, лабиринт, игроки = игроки[1].move(request, лабиринт, игроки)
    # в первый раз нужно передать 'NN' ПОРАБОТАТЬ!!!!!!!!!!
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
    step_flag = 0

    if Return_client[8] == 0:
        objects_enemy, objects_player = visual_parts(width, height, objects_enemy, objects_player,
                                                                  [len(objects_player)-2, len(objects_player)-3],
                                                                  [len(objects_enemy)-2, len(objects_enemy)-3])
    say_to_client_about_serv_step(data_client, conn)
    # изменение лабиринта в зависимости от data_client!!!!!



IP = socket.gethostbyname(socket.gethostname())
print(IP)
width = 1000
height = 600
finished = False
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

while not finished:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if (x > width/2-200) and (x<width/2+200) and(y>height/2-100) and (y<height/2+100):
                finished = True
        menu_server(screen, width, height, IP)

Port = 9090
conn = connection(IP, Port)

step_flag = 1  # флаг хода игрока-сервера, 1 - наш шаг, 0 - шаг врага. можно прикрутить рандом
conn.send(str(step_flag).encode('utf-8'))  # передача начального флага клиенту


data_client = 'NN00'  # клиент - тот, кто рисуется слева
data_server = 'NN00'  # сервер - тот, кто справа (небольшая путаница в обозначениях)

objects_player = [[]]
objects_enemy = [[]]

x_player = width / 4
y_player = height * 2 / 3
x_enemy = width * 3 / 4
y_enemy = height * 2 / 3
Return_server = []
Return_client = []


finished = False

visual_player(screen, width, height, 'NN00', objects_player,
                                  objects_enemy, x_player, y_player, x_enemy, y_enemy)
visual_enemy(screen, width, height, 'NN00', objects_enemy,
                                  objects_player, x_enemy, y_enemy, x_player, y_player)
if step_flag == 1:
    player_step(screen, width, height)
elif step_flag == 0:
    enemy_step(screen, width, height)
pygame.display.update()

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
                                                          [len(objects_player) - 2, len(objects_player) - 3])
            # изменение лабиринта!!!!
            step_flag = 1  # !!!!!!!!!!!!!!!!! возможно будет ошибка
            pygame.event.clear()  # возможно исправит баг
            

pygame.quit()
conn.close()
