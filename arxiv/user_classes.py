import pygame
import random
from modules.server import *
from modules.visualisation import *
from modules.lab_generation import generate

class User:
    def __init__(self, typ_player, width, height):
        
        self.is_player = typ_player #True-игрок, False-противник
        self.objects = [[]]
        self.data = 'NN00'
        self.y = height * 2 / 3
        if self.is_player:
            self.x = width / 4
        else:
            self.x = width * 3 / 4
        

        
    

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

def serv_step(request):
    '''
    Функция обрабатывает ход сервера: рисует изменения вследствие хода на экране и отправляет данные о ходе на
    удаленный компьютер соперника.
    Args:
        request: запрос в лабиринт (направление стрельбы (wasd) или ходьбы(WASD))
    '''

    global data_player, лабиринт, игроки
    global screen, objects_player, objects_enemy
    global x_player, y_player, x_enemy, y_enemy, step_flag

    # запрос в матрицу лабиринта для совершения хода
    data_player, лабиринт, игроки = игроки[1].move(request, лабиринт, игроки)
    # визуализация хода
    say_to_client_about_serv_step(data_player, conn)
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
    # сообщение сопернику о ходе
    return bool(vis[8])     # проверка на конец игры


width = 1000
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

IP = socket.gethostbyname(socket.gethostname())
conn = False
Port = 9090

# рисование главного меню перед стартом игры
menu_server(screen, width, height, IP)
while not conn:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        # в случае нажатия на клавишу подключиться, создает соедиение с клиентом
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            if (x > width / 2 - 200) and (x < width / 2 + 200) and (y > height / 2 - 100) and (y < height / 2 + 100):
                conn = connection(IP, Port)


# кто ходит первым выбирается случайным образом
step_flag = random.randint(0, 1)  # флаг хода игрока-сервера, 1 - наш шаг, 0 - шаг врага
conn.send(str(step_flag).encode('utf-8'))  # передача начального флага клиенту
step_flag = bool(step_flag) #True, если ход пользователя

лабиринт, игроки = generate() # создание лабиринта
game_preparing()
finished = False

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: finished = True
        elif event.type == pygame.KEYDOWN and step_flag:
            if event.key == pygame.K_ESCAPE: finished = True
            # ход игрока
            elif event.key == pygame.K_UP: finished = serv_step('W')
            elif event.key == pygame.K_DOWN: finished = serv_step('S')
            elif event.key == pygame.K_RIGHT: finished = serv_step('D')
            elif event.key == pygame.K_LEFT: finished = serv_step('A')
            elif event.key == pygame.K_w: finished = serv_step('w')
            elif event.key == pygame.K_s: finished = serv_step('s')
            elif event.key == pygame.K_d: finished = serv_step('d')
            elif event.key == pygame.K_a: finished = serv_step('a')

    # ход соперника
    if not step_flag and not finished:
        # обработка хода соперника, аналогично ходу игрока

        data_enemy, лабиринт, игроки = answer_to_client_step(лабиринт, conn,
                                                              игроки)
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
conn.close()
