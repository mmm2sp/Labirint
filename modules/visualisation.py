import pygame
from modules.basic_pictures import *


def visual_player(screen, width, height, data_player, objects_player, objects_enemy, x_player, y_player,
                  x_enemy, y_enemy):
    '''
    Функция получает: данные об экране(высота, ширина),
    информацию, которую передали игроку-клиенту,
    массивы с объектами обоих игроков,
    координаты обоих игроков.
    Функция обрабатывает смещение игрока(W,A,S,D), меняет массивы и координаты игроков,
    и рисует то, что игрок открыл для себя за свой ход
    Функция возвращает: измененные массивы объектов игроков, измененные координаты, индикатор окончания игры
    '''
    screen.fill((255, 255, 255))
    l = 20 #сторона клетки

    pygame.time.Clock().tick(10)

    data_movement = str(data_player[0]) # Смещение игрока
    data_object = str(data_player[1]) # Открытый элемент лабиринта
    data_key = bool(data_player[2])  # Есть ли у игрока ключ
    data_bullets = int(data_player[3])  # Количество пуль у игрока

    final_flag = 0

    N = len(objects_player)

    for obj in objects_player[N - 1]:
        obj.draw()#Рисуем все уже имеющиеся в массивах объекты на полуэкране игрока

    # Сначала проверяем второй символ: действия, если стена или дверь
    set_move = {'W', 'A', 'S', 'D'}
    if data_object in set_move:
        wall = Wall(screen, x_player, y_player, l, (0, 0, 0), data_object.lower())#Рисуем стену согласно ее ориентации
        objects_player[N - 1].append(wall)
        wall.draw()
    elif data_object.upper() in set_move:
        door = Door(screen, x_player, y_player, l, (120, 50, 0), data_object.lower())#Рисуем дверь согласно ее ориентации
        objects_player[N - 1].append(door)
        door.draw()
    # залазим на часть экрана, где отрисовывается соперник
    if data_object == 'G':  # Умер второй игрок

        x_enemy = width * 3 / 4
        y_enemy = height * 2 / 3
        revival = Revival(screen, x_enemy, y_enemy, l)
        # рисуем по-новому
        new_objects_enemy = []
        new_objects_enemy.append(revival)
        objects_enemy.append(new_objects_enemy)

        # просто закрашиваем неугодные элементы
        pygame.draw.rect(screen, (255, 255, 255),
                         (width / 2 + 5, height / 3 + 5, width / 2 - 5,
                          height * 2 / 3))  # здесь может быть ошибка с флажком

        revival.draw()

        visual_parts(width, height, objects_enemy, objects_player, [len(objects_player) - 2, len(objects_player) - 3],
                     [len(objects_enemy) - 2, len(objects_enemy) - 3])

    # Сдвигаем изображение, если первый символ указывает направление или что там дверь, а игрок с ключом
    if data_movement == 'W':
        y_player -= l
    elif data_movement == 'S':
        y_player += l
    elif data_movement == 'A':
        x_player -= l
    elif data_movement == 'D':
        x_player += l
    elif data_movement == 'w':
        y_player -= l
        final_frame(screen, width, height, 1)
        final_flag = 1
    elif data_movement == 's':
        y_player += l
        final_frame(screen, width, height, 1)
        final_flag = 1
    elif data_movement == 'a':
        x_player -= l
        final_frame(screen, width, height, 1)
        final_flag = 1
    elif data_movement == 'd':
        x_player += l
        final_frame(screen, width, height, 1)
        final_flag = 1
    else:  # Не переместились
        data_object = data_movement
        # Отрисовываем то, что в текущей клетке

    if final_flag == 0:

        if data_object == 'K':# На открытой клетке ключ
            key = Key(screen, x_player, y_player, l)
            objects_player[N - 1].append(key)
            key.draw()
        elif data_object == 'R':# На открытой клетке больница
            revival = Revival(screen, x_player, y_player, l)
            objects_player[N - 1].append(revival)
            revival.draw()
        elif data_object == 'P':#На открытой клетке портал, перемещаемся в следующий
            portal = Portal(screen, x_player, y_player, l)
            objects_player[N - 1].append(portal)
            x_player = width / 4
            y_player = height * 2 / 3

            portal = Portal(screen, x_player, y_player, l)
            new_objects_player = []
            new_objects_player.append(portal)
            objects_player.append(new_objects_player)
            pygame.draw.rect(screen, (255, 255, 255), (0, height / 3 + 5, width / 2 - 5, height * 2 / 3))
            portal.draw()
        elif data_object == 'E':# На открытой клетке оружейная
            armory = Armory(screen, x_player, y_player, l)
            objects_player[N - 1].append(armory)
            armory.draw()
        elif data_object == 'N':# На открытой клетке ничего нет
            exp = Explored_square(screen, x_player, y_player, l)
            objects_player[N - 1].append(exp)
            exp.draw()
        elif data_object == 'M': #На открытой клетке минотавр, попадаем в больницу
            minotaur = Minotaur(screen, x_player, y_player, l)
            objects_player[N - 1].append(minotaur)

            x_player = width * 1 / 4
            y_player = height * 2 / 3
            revival = Revival(screen, x_player, y_player, l)
            # рисуем по-новому
            new_objects_player = []
            new_objects_player.append(revival)
            objects_player.append(new_objects_player)
            pygame.draw.rect(screen, (255, 255, 255), (0, height / 3 + 5, width / 2 - 5, height * 2 / 3))
            revival.draw()
        elif data_object == 'm':# На открытой клетке убитый минотавр
            dead_minotaur = Dead_minotaur(screen, x_player, y_player, l)
            objects_player[N - 1].append(dead_minotaur)
            dead_minotaur.draw()

        player = Player(screen, x_player, y_player, l)# Рисуем игрока
        player.draw()

        N1 = len(objects_enemy)
        for obj in objects_enemy[N1 - 1]:
            obj.draw()# Рисуем все объекты на полуэкране противника

        another_player = Another_Player(screen, x_enemy, y_enemy, l)
        another_player.draw()#Рисуем противника

        boundaries = Boundaries(screen, width, height)
        boundaries.draw()#Рисуем разделение экрана на зоны

        # может быть будет доработано
        #Arrow_botton1 = Arrow_botton(screen, width, height, 7 / 480 * width)
        #Arrow_botton1.draw()

        #Arrow_botton2 = Arrow_botton(screen, width, height, 247 / 480 * width)
        #Arrow_botton2.draw()

        pygame.display.update()

    return screen, objects_player, objects_enemy, x_player, y_player, x_enemy, y_enemy, final_flag


def visual_enemy(screen, width, height, data_enemy, objects_enemy, objects_player, x_enemy, y_enemy,
                 x_player, y_player):
    '''
    Функция получает: данные об экране(высота, ширина),
    информацию, которую передали игроку-серверу,
    массивы с объектами обоих игроков,
    координаты обоих игроков.
    Функция обрабатывает смещение игрока(W,A,S,D)
    и рисует то, что он открыл для себя за свой ход
    '''
    screen.fill((255, 255, 255))
    l = 20

    final_flag = 0
    pygame.time.Clock().tick(10)

    data_movement = str(data_enemy[0])# Смещение противника
    data_object = str(data_enemy[1])# Объект, открытый противником
    data_key = bool(data_enemy[2])  # Есть ли у игрока ключ
    data_bullets = int(data_enemy[3])  # Количество пуль у игрока

    N = len(objects_enemy)

    for obj in objects_enemy[N - 1]:
        obj.draw()#Рисуем все уже изученные противником объекты

    # Сначала проверяем второй символ: действия, если стена или дверь
    set_move = {'W', 'A', 'S', 'D'}
    if data_object in set_move:
        wall = Wall(screen, x_enemy, y_enemy, l, (0, 0, 0), data_object.lower())#Рисуем стену согласно ее ориентации
        objects_enemy[N - 1].append(wall)
        wall.draw()
    elif data_object.upper() in set_move:
        door = Door(screen, x_enemy, y_enemy, l, (120, 50, 0), data_object.lower())#Рисуем дверь согласно ее ориентации
        objects_enemy[N - 1].append(door)
        door.draw()
    elif data_object == 'G':  # Умер второй игрок
        x_player = width * 1 / 4
        y_player = height * 2 / 3
        revival = Revival(screen, x_player, y_player, l)#Помещаем его на возрождение

        new_objects_player = []
        new_objects_player.append(revival)
        objects_player.append(new_objects_player)
        # закрашиваем неугодные элементы
        pygame.draw.rect(screen, (255, 255, 255), (0, height * 1 / 3 + 5, width / 2, height * 2 / 3))

        revival.draw()

        visual_parts(width, height, objects_enemy, objects_player, [len(objects_player) - 2, len(objects_player) - 3],
                     [len(objects_enemy) - 2, len(objects_enemy) - 3])

    # Сдвигаем изображение, если первый символ указывает направление или что там дверь, а игрок с ключом
    if data_movement == 'W':
        y_enemy -= l
    elif data_movement == 'S':
        y_enemy += l
    elif data_movement == 'A':
        x_enemy -= l
    elif data_movement == 'D':
        x_enemy += l
    elif data_movement == 'w':
        y_player -= l
        final_frame(screen, width, height, 0)
        final_flag = 1
    elif data_movement == 's':
        y_enemy += l
        final_frame(screen, width, height, 0)
        final_flag = 1
    elif data_movement == 'a':
        x_enemy -= l
        final_frame(screen, width, height, 0)
        final_flag = 1
    elif data_movement == 'd':
        x_enemy += l
        final_frame(screen, width, height, 0)
        final_flag = 1
    else:  # Не переместились
        data_object = data_movement
        # Отрисовываем то, что в текущей клетке

    if final_flag == 0:

        if data_object == 'K':# На открытой клетке ключ
            key = Key(screen, x_enemy, y_enemy, l)
            objects_enemy[N - 1].append(key)
            key.draw()
        elif data_object == 'R':# На открытой клетке больница
            revival = Revival(screen, x_enemy, y_enemy, l)
            objects_enemy[N - 1].append(revival)
            revival.draw()
        elif data_object == 'P':# На открытой клетке портал, перемещаемся в следующий портал
            portal = Portal(screen, x_enemy, y_enemy, l)
            objects_enemy[N - 1].append(portal)
            x_enemy = width * 3 / 4
            y_enemy = height * 2 / 3

            portal = Portal(screen, x_enemy, y_enemy, l)
            new_objects_enemy = []
            new_objects_enemy.append(portal)
            objects_enemy.append(new_objects_enemy)
            pygame.draw.rect(screen, (255, 255, 255), (width / 2 + 5, height * 1 / 3 + 5, width / 2, height * 2 / 3))
            portal.draw()
        elif data_object == 'E':# На открытой клетке оружейная
            armory = Armory(screen, x_enemy, y_enemy, l)
            objects_enemy[N - 1].append(armory)
            armory.draw()
        elif data_object == 'N':# На открытой клетке ничего нет
            exp = Explored_square(screen, x_enemy, y_enemy, l)
            objects_enemy[N - 1].append(exp)
            exp.draw()

        elif data_object == 'M':# На открытой клетке минотавр, противник попадает в больницу
            minotaur = Minotaur(screen, x_enemy, y_enemy, l)
            objects_enemy[N - 1].append(minotaur)

            x_enemy = width * 3 / 4
            y_enemy = height * 2 / 3
            revival = Revival(screen, x_enemy, y_enemy, l)

            new_objects_enemy = []
            new_objects_enemy.append(revival)
            objects_enemy.append(new_objects_enemy)
            pygame.draw.rect(screen, (255, 255, 255), (width / 2 + 5, height * 1 / 3 + 5, width / 2, height * 2 / 3))
            revival.draw()
        elif data_object == 'm':# На открытой клетке убитый минотавр
            dead_minotaur = Dead_minotaur(screen, x_enemy, y_enemy, l)
            objects_enemy[N - 1].append(dead_minotaur)
            dead_minotaur.draw()

        another_player = Another_Player(screen, x_enemy, y_enemy, l)
        another_player.draw()# Рисуем противника

        N1 = len(objects_player)
        for obj in objects_player[N1 - 1]:
            obj.draw()# Рисуем все объекты на полуэкране игрока

        player = Player(screen, x_player, y_player, l)
        player.draw()# Рисуем игрока

        boundaries = Boundaries(screen, width, height)
        boundaries.draw()# Рисуем границы, разделяющие игровые поля

        # может быть будет доработано
        #Arrow_botton1 = Arrow_botton(screen, width, height, 7 / 480 * width)
        #Arrow_botton1.draw()

        #Arrow_botton2 = Arrow_botton(screen, width, height, 247 / 480 * width)
        #Arrow_botton2.draw()

        pygame.display.update()

    return screen, objects_enemy, objects_player, x_enemy, y_enemy, x_player, y_player, final_flag


def visual_parts(width, height, objects_enemy, objects_player, player_parts, enemy_parts):
    '''
    Функция рисует уже открытые куски карты в верхней части экрана в количестве 2
    :param player_parts: массив из двух элементов, который указывает, какие куски нужно рисовать у игрока
    :param enemy_parts: массив из двух элементов, который указывает, какие куски нужно рисовать у противника
    '''
    # рисование левого куска игрока
    if (player_parts[0] >= 0) and (player_parts[0] <= len(objects_player) - 1):
        x1 = objects_player[player_parts[0]][0].x
        y1 = objects_player[player_parts[0]][0].y
        dx1 = 3 / 8 * width - x1
        dy1 = 1 / 6 * height - y1
        for i in objects_player[player_parts[0]]:
            i.x += dx1
            i.y += dy1
            i.draw()
    # правого
    if player_parts[1] >= 0 and (player_parts[1] <= len(objects_player) - 1):
        x2 = objects_player[player_parts[1]][0].x
        y2 = objects_player[player_parts[1]][0].y
        dx2 = 1 / 8 * width - x2
        dy2 = 1 / 6 * height - y2
        for i in objects_player[player_parts[1]]:
            i.x += dx2
            i.y += dy2
            i.draw()

    # рисование левого у противника
    if enemy_parts[0] >= 0 and (enemy_parts[0] <= len(objects_enemy) - 1):
        x3 = objects_enemy[enemy_parts[0]][0].x
        y3 = objects_enemy[enemy_parts[0]][0].y
        dx3 = 7 / 8 * width - x3
        dy3 = 1 / 6 * height - y3
        for i in objects_enemy[enemy_parts[0]]:
            i.x += dx3
            i.y += dy3
            i.draw()

    # правого
    if enemy_parts[1] >= 0 and (enemy_parts[1] <= len(objects_enemy) - 1):
        x4 = objects_enemy[enemy_parts[1]][0].x
        y4 = objects_enemy[enemy_parts[1]][0].y
        dx4 = 5 / 8 * width - x4
        dy4 = 1 / 6 * height - y4
        for i in objects_enemy[enemy_parts[1]]:
            i.x += dx4
            i.y += dy4
            i.draw()

    pygame.display.update()
    return objects_enemy, objects_player


def menu_server(screen, width, height, IP):
    '''
    Функция рисует стартовый экран игрока, создающего сервер,
    на нем отображается Ip-адрес сервера и кнопка старта игры(создания лабиринта)
    принимает: экран, его высоту и ширину, IP адрес сервера
    '''
    screen.fill((255, 255, 255))
    screen.blit(pygame.font.Font(None, 50).render(str('Ваш IP-адрес: ') + str(IP), True, (0, 0, 0)),
                (width // 12 * 2, height // 20))# Отображаем IP
    Opened_door(screen, width // 8, height // 5, 100).draw()#Декоративная дверь
    Button(screen, width / 2, height / 2).draw()# Рисуем кнопку, по которой можно нажать
    Minotaur(screen, width * 5 // 6, height // 4, 200).draw()# Декоративный минотавр
    Key(screen, width * 5.25 // 6, height * 3 // 4, 200).draw()# Декоративный ключ
    # Далее рисуем небольшой декоративный лабиринтик
    x = width // 24 * 4
    y = height * 5.5 // 8
    Key(screen, x, y, 40).draw()
    Wall(screen, x, y, 40, (0, 0, 0), 'w').draw()
    Wall(screen, x, y, 40, (0, 0, 0), 'a').draw()
    Armory(screen, x, y + 40, 40).draw()
    Wall(screen, x, y + 40, 40, (0, 0, 0), 'a').draw()
    Portal(screen, x, y + 80, 40).draw()
    Wall(screen, x, y + 80, 40, (0, 0, 0), 's').draw()
    Wall(screen, x, y + 80, 40, (0, 0, 0), 'a').draw()
    Explored_square(screen, x + 40, y, 40).draw()
    Player(screen, x + 40, y, 40).draw()
    Wall(screen, x + 40, y, 40, (0, 0, 0), 'w').draw()
    Minotaur(screen, x + 40, y + 40, 40).draw()
    Explored_square(screen, x + 40, y + 80, 40).draw()
    Door(screen, x + 40, y + 80, 40, (155, 0, 0), 's').draw()
    Portal(screen, x + 80, y, 40).draw()
    Wall(screen, x + 80, y, 40, (0, 0, 0), 'w').draw()
    Wall(screen, x + 80, y, 40, (0, 0, 0), 'd').draw()
    Explored_square(screen, x + 80, y + 40, 40).draw()
    Wall(screen, x + 80, y + 40, 40, (0, 0, 0), 's').draw()
    Wall(screen, x + 80, y + 40, 40, (0, 0, 0), 'a').draw()
    Wall(screen, x + 80, y + 40, 40, (0, 0, 0), 'd').draw()
    Explored_square(screen, x + 80, y + 80, 40).draw()
    Another_Player(screen, x + 80, y + 80, 40).draw()
    Wall(screen, x + 80, y + 80, 40, (0, 0, 0), 's').draw()
    Wall(screen, x + 80, y + 80, 40, (0, 0, 0), 'd').draw()
    Wall(screen, x, y + 80, 40, (0, 0, 0), 'd').draw()
    pygame.display.update()


def menu_client(screen, width, height):
    '''
    Функция рисует стартовый экран игрока-клиента, подключающегося к серверу
    '''
    screen.fill((255, 255, 255))
    Opened_door(screen, width // 8, height // 5, 100).draw()#Декоративная дверь
    Typing_window(screen, width / 2, height / 2).draw()# Рисуем окошко, в которое нужно вводить IP-адрес сервера
    Minotaur(screen, width * 5 // 6, height // 4, 200).draw()# Декоративный минотавр
    Key(screen, width * 5.25 // 6, height * 3 // 4, 200).draw()# Декоративный ключ
    # Далее рисуем небольшой декоративный лабиринтик
    x = width // 24 * 4
    y = height * 5.5 // 8
    Key(screen, x, y, 40).draw()
    Wall(screen, x, y, 40, (0, 0, 0), 'w').draw()
    Wall(screen, x, y, 40, (0, 0, 0), 'a').draw()
    Armory(screen, x, y + 40, 40).draw()
    Wall(screen, x, y + 40, 40, (0, 0, 0), 'a').draw()
    Portal(screen, x, y + 80, 40).draw()
    Wall(screen, x, y + 80, 40, (0, 0, 0), 's').draw()
    Wall(screen, x, y + 80, 40, (0, 0, 0), 'a').draw()
    Explored_square(screen, x + 40, y, 40).draw()
    Player(screen, x + 40, y, 40).draw()
    Wall(screen, x + 40, y, 40, (0, 0, 0), 'w').draw()
    Minotaur(screen, x + 40, y + 40, 40).draw()
    Explored_square(screen, x + 40, y + 80, 40).draw()
    Door(screen, x + 40, y + 80, 40, (155, 0, 0), 's').draw()
    Portal(screen, x + 80, y, 40).draw()
    Wall(screen, x + 80, y, 40, (0, 0, 0), 'w').draw()
    Wall(screen, x + 80, y, 40, (0, 0, 0), 'd').draw()
    Explored_square(screen, x + 80, y + 40, 40).draw()
    Wall(screen, x + 80, y + 40, 40, (0, 0, 0), 's').draw()
    Wall(screen, x + 80, y + 40, 40, (0, 0, 0), 'a').draw()
    Wall(screen, x + 80, y + 40, 40, (0, 0, 0), 'd').draw()
    Explored_square(screen, x + 80, y + 80, 40).draw()
    Another_Player(screen, x + 80, y + 80, 40).draw()
    Wall(screen, x + 80, y + 80, 40, (0, 0, 0), 's').draw()
    Wall(screen, x + 80, y + 80, 40, (0, 0, 0), 'd').draw()
    Wall(screen, x, y + 80, 40, (0, 0, 0), 'd').draw()
    pygame.display.update()


def final_frame(screen, width, height, situation):
    '''
    Функция рисует на экране "анимацию" с сообщением о ситуации
    Функция получает экран, его высоту и ширину, situation:
    Если situation = 0 - это проигрыш
    situation = 1 - это победа
    '''
    if situation == 0:
        winnercolor = (100, 100, 255)
        losercolor = (0, 200, 0)
        f = pygame.font.Font(None, 150)
        text = f.render('DEFEAT...', True, (255, 0, 0))

    if situation == 1:
        winnercolor = (0, 200, 0)
        losercolor = (100, 100, 255)
        f = pygame.font.Font(None, 150)
        text = f.render('VICTORY!', True, (0, 200, 0))
        
    # Первый кадр
    screen.fill((255, 255, 255))
    Men(screen, width * 3 // 4, height * 2.5 // 8, winnercolor).draw_body()
    Men(screen, width * 3 // 4, height * 2.5 // 8, winnercolor).draw_legs_stand()
    Closed_door(screen, width // 4, height // 5, width // 4).draw()
    screen.blit(text, (width * 2.5 // 8, height // 20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    # Второй кадр
    screen.fill((255, 255, 255))
    Closed_door(screen, width // 4, height // 5, width // 4).draw()
    Men(screen, width * 4 // 8, height * 2.5 // 8, winnercolor).draw_body()
    Men(screen, width * 4 // 8, height * 2.5 // 8, winnercolor).draw_legs_stand()
    screen.blit(text, (width * 2.5 // 8, height // 20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    # Третий кадр
    screen.fill((255, 255, 255))
    Fully_opened_door(screen, width // 4, height // 5, width // 4).draw()
    Men(screen, width * 3 // 8, height * 2.5 // 8, winnercolor).draw_body()
    Men(screen, width * 3 // 8, height * 2.5 // 8, winnercolor).draw_legs_stand()
    screen.blit(text, (width * 2.5 // 8, height // 20))
    pygame.display.update()
    pygame.time.Clock().tick(1)
    
    # Четвертый кадр
    screen.fill((255, 255, 255))
    Opened_door(screen, width // 4, height // 5, width // 4).draw()
    screen.blit(text, (width * 2.5 // 8, height // 20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    # Пятый кадр
    screen.fill((255, 255, 255))
    Corner(screen, width, height).draw()
    Men(screen, width * 5 // 8, height * 2.5 // 8, losercolor).draw_body()
    Men(screen, width * 5 // 8, height * 2.5 // 8, losercolor).draw_legs_stand()
    screen.blit(text, (width * 2.5 // 8, height // 20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    # Шестой кадр
    screen.fill((255, 255, 255))
    Corner(screen, width, height).draw()
    Men(screen, width * 5 // 8, height * 3 // 8, losercolor).draw_body()
    Men(screen, width * 5 // 8, height * 3 // 8, losercolor).draw_legs_sit()
    screen.blit(text, (width * 2.5 // 8, height // 20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    # Седьмой кадр
    screen.fill((255, 255, 255))
    Corner(screen, width, height).draw()
    Men(screen, width * 5 // 8, height * 3 // 8, (230, 230, 230)).draw_body()
    Men(screen, width * 5 // 8, height * 3 // 8, (230, 230, 230)).draw_legs_sit()
    Web(screen, width // 4, height // 2, 100).draw()
    Web(screen, width // 8 * 6, height // 5 * 3, 50).draw()
    Skull(screen, width * 5 // 8, height * 3 // 8, 150).draw()
    screen.blit(text, (width * 2.5 // 8, height // 20))
    pygame.display.update()
    pygame.time.Clock().tick(2)


def key_and_knifes(screen, width, height, data_player, data_enemy):
    '''
    Функция рисует на экране количество ножей у игроков и наличие ключа у игроков
    Функция получает экран, его ширину и высоту, и информацию о ходах обоих игроков
    '''
    data_key_player = int(data_player[2])  # Есть ли у игрока ключ
    data_bullets_player = int(data_player[3])  # Количество пуль у игрока
    data_key_enemy = int(data_enemy[2])  # Есть ли у противника ключ
    data_bullets_enemy = int(data_enemy[3])  # Количество пуль у противника
    if data_key_player == 1:
        Getted_key(screen, width * 7 // 16, height * 7 // 8, 40).draw()
    if data_key_enemy == 1:
        Getted_key(screen, width * 15 // 16, height * 7 // 8, 40).draw()
    x = width // 16
    y = height * 7 // 8
    for i in range(data_bullets_player):
        Knife(screen, x, y, 40).draw()
        x += 40
    x = width * 9 // 16
    for i in range(data_bullets_enemy):
        Knife(screen, x, y, 40).draw()
        x += 40
    pygame.display.update()


def player_step(screen, width, height):
    '''
    Функция рисует флаг на экране противника, когда идет его ход
    '''
    Flag(screen, width // 4, height // 3 + 40, 60, (0, 220, 0)).draw()


def enemy_step(screen, width, height):
    '''
    Функция рисует флаг на экране игрока, когда идет его ход
    '''
    Flag(screen, width // 4 * 3, height // 3 + 40, 60, (100, 100, 255)).draw()


if __name__ == "__main__":
    print("This module is not for direct call!")
