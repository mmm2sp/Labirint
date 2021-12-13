import pygame
from modules.client import *
from modules.visualisation import *


def game_preparing():
    #FixMe: Нужна документ-строка

    global data_player, data_enemy, objects_player, objects_enemy
    global x_player, y_player, x_enemy, y_enemy, return_player, return_enemy
    
    data_player = 'NN00'  # информация о начальном состоянии игрока (слева)
    data_enemy = 'NN00'  # информация о начальном состоянии противника (справа)
    objects_player = [[]] # открытые куски карты игрока
    objects_enemy = [[]] # открытые куски карты противника

    x_player = width / 4
    y_player = height * 2 / 3
    x_enemy = width * 3 / 4
    y_enemy = height * 2 / 3

    visual_player(screen, width, height, 'NN00', objects_player,
                  objects_enemy, x_player, y_player, x_enemy, y_enemy)
    visual_enemy(screen, width, height, 'NN00', objects_enemy,
                 objects_player, x_enemy, y_enemy, x_player, y_player)

    # начальное рисование флажка над ходящим игроком
    if step_flag: player_step(screen, width, height)
    else: enemy_step(screen, width, height)
    
    pygame.display.update()

    
def client_step(request):
    '''
    Функция обрабатывает ход клиента: отправляет запрос на сервер о своем ходе,
    получает ответ от сервера, рисует изменения в случае удачного хода
    Args:
        request: запрос на сервер (направление стрельбы (wasd) или ходьбы(WASD))
    '''
    global sock
    global screen, width, height, data_player, objects_player
    global objects_enemy, x_player, y_player, x_enemy, y_enemy, step_flag

    # запрос на сервер, сообщение серверу о ходе
    data_player = ask_server(request, sock)
    # рисование изменений
    vis = visual_player(screen, width, height, data_player, objects_player,
                                  objects_enemy, x_player, y_player, x_enemy, y_enemy)
    enemy_step(screen, width, height)

    screen = vis[0]
    objects_player = vis[1]
    objects_enemy = vis[2]
    x_player = vis[3]
    y_player = vis[4]
    x_enemy = vis[5]
    y_enemy = vis[6]
    step_flag = False

    # отдельно рассмотрен случай окончания игры для избежания бага
    if vis[8] == 0:
        objects_enemy, objects_player = visual_parts(width, height, objects_enemy, objects_player,
                                                     [len(objects_player) - 2, len(objects_player) - 3],
                                                     [len(objects_enemy) - 2, len(objects_enemy) - 3])
        # случай, если произошло убийство
        if data_player[1] == 'G':
            key_and_knifes(screen, width, height, data_player, 'AB00')
        else:
            key_and_knifes(screen, width, height, data_player, data_enemy)

    return  bool(vis[8])


width = 1000
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

# рисование стартового меню
menu_client(screen, width, height)
inf = ['', 0]
IP = ''
while inf[1] != 1:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # ввод адреса сервера, к которому подключаемся
        inf = Typing(IP, width / 2, height / 2, event, screen)
        IP = inf[0]
        # в случае нажатия на пробел, производим подключение
        if inf[1] == 1:
            break
IP = inf[0]
Port = 9090
sock = connection(IP, Port)


step_flag = int((sock.recv(1024)).decode('utf-8'))  # флаг хода игрока-сервера, получаем начальное значение от сервера
step_flag = not bool(step_flag) #True, если ход пользователя

game_preparing()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: finished = True
        elif event.type == pygame.KEYDOWN and step_flag:
            if event.key == pygame.K_ESCAPE: finished = True
            # ход игрока
            elif event.key == pygame.K_UP: finished = client_step('W')
            elif event.key == pygame.K_DOWN: finished = client_step('S')
            elif event.key == pygame.K_RIGHT: finished = client_step('D')
            elif event.key == pygame.K_LEFT: finished = client_step('A')
            elif event.key == pygame.K_w: finished = client_step('w')
            elif event.key == pygame.K_s: finished = client_step('s')
            elif event.key == pygame.K_d: finished = client_step('d')
            elif event.key == pygame.K_a: finished = client_step('a')

    # ход соперника, аналогичен ходу игрока
    if not step_flag and not finished:
        data_enemy = catch_server_steps(sock)
        vis = visual_enemy(screen, width, height, data_enemy, objects_enemy, objects_player,
                                     x_enemy, y_enemy, x_player, y_player)
        player_step(screen, width, height)

        screen = vis[0]
        objects_enemy = vis[1]
        objects_player = vis[2]
        x_enemy = vis[3]
        y_enemy = vis[4]
        x_player = vis[5]
        y_player = vis[6]

        if vis[8] == 0:
            objects_enemy, objects_player = visual_parts(width, height, objects_enemy, objects_player,
                                                         [len(objects_player) - 2, len(objects_player) - 3],
                                                         [len(objects_enemy) - 2, len(objects_enemy) - 3])
            # случай, если произошло убийство
            if data_enemy[1] == 'G':
                key_and_knifes(screen, width, height, 'AB00', data_enemy)
            else:
                key_and_knifes(screen, width, height, data_player, data_enemy)
        else: finished = True
        step_flag = True
        pygame.event.clear()
        #Очистка очереди, чтобы не обрабатывались нажатия во время чужого хода

pygame.quit()
sock.close()
