from basic_pictures import *
import pygame


def visual_client(screen, width, height, data_client, objects_client, objects_server, x_client, y_client,
                  x_server, y_server):
    '''
    Функция получает: данные об экране(высота, ширина),
    информацию, которую передали игроку-клиенту,
    массивы с объектами обоих игроков,
    координаты обоих игроков.
    Функция обрабатывает смещение игрока(W,A,S,D)
    и рисует то, что он открыл для себя за свой ход
    '''
    screen.fill((255, 255, 255))
    l = 20

    v_client = 0
    h_client = 0
    data_movement = str(data_client[0])
    data_object = str(data_client[1])

    flag = 0

    if str(data_movement) == 'W':
        y_client -= 20
    elif str(data_movement) == 'S':
        y_client += 20
    elif str(data_movement) == 'A':
        x_client -= 20
    elif str(data_movement) == 'D':
        x_client += 20

    N = len(objects_client)

    for obj in objects_client[N-1]:
        obj.draw()

    if str(data_object) == 'W':
        wall = Wall(screen, x_client, y_client, l, (0, 0, 0), 'w')
        objects_client[N-1].append(wall)
        wall.draw()
    elif str(data_object) == 'A':
        wall = Wall(screen, x_client, y_client, l, (0, 0, 0), 'a')
        objects_client[N-1].append(wall)
        wall.draw()
    elif str(data_object) == 'S':
        wall = Wall(screen, x_client, y_client, l, (0, 0, 0), 's')
        objects_client[N-1].append(wall)
        wall.draw()
    elif str(data_object) == 'D':
        wall = Wall(screen, x_client, y_client, l, (0, 0, 0), 'd')
        objects_client[N-1].append(wall)
        wall.draw()
    elif str(data_object) == 'F':
        door = Door(screen, x_client, y_client, l, (120, 50, 0), 'w')
        objects_client[N-1].append(door)
        door.draw()
    elif str(data_object) == 'C':
        door = Door(screen, x_client, y_client, l, (120, 50, 0), 'a')
        objects_client[N-1].append(door)
        door.draw()
    elif str(data_object) == 'V':
        door = Door(screen, x_client, y_client, l, (120, 50, 0), 's')
        objects_client[N-1].append(door)
        door.draw()
    elif str(data_object) == 'B':
        door = Door(screen, x_client, y_client, l, (120, 50, 0), 'd')
        objects_client[N-1].append(door)
        door.draw()
    elif str(data_object) == 'K':
        key = Key(screen, x_client, y_client, l)
        objects_client[N-1].append(key)
        key.draw()
    elif str(data_object) == 'R':
        revival = Revival(screen, x_client, y_client, l)
        objects_client[N-1].append(revival)
        revival.draw()
    # разобраться отдельно
    elif str(data_object) == 'P':
        portal = Portal(screen, x_client, y_client, l)
        objects_client[N-1].append(portal)
        x_client = width / 4
        y_client = height * 2 / 3

        portal = Portal(screen, x_client, y_client, l)
        new_objects_client = []
        new_objects_client.append(portal)
        objects_client.append(new_objects_client)
        pygame.draw.rect(screen, (255, 255, 255), (0, height / 3 + 5, width / 2 - 5, height * 2 / 3))
        portal.draw()
        # создали навую рисовалку, нужно об этом как-то сообщить
        flag = 1

    elif str(data_object) == 'E':
        armory = Armory(screen, x_client, y_client, l)
        objects_client[N-1].append(armory)
        armory.draw()
    elif str(data_object) == 'N':
        exp = Explored_square(screen, x_client, y_client, l)
        objects_client[N-1].append(exp)
        exp.draw()

    #разобраться отдельно
    elif str(data_object) == 'M':
        minotaur = Minotaur(screen, x_client, y_client, l)
        objects_client[N-1].append(minotaur)

        x_client = width * 1 / 4
        y_client = height * 2 / 3
        revival = Revival(screen, x_client, y_client, l)
        # рисуем по-новому
        new_objects_client = []
        new_objects_client.append(revival)
        objects_client.append(new_objects_client)
        pygame.draw.rect(screen, (255, 255, 255), (0, height/3 + 5, width/2 - 5, height*2 /3))
        revival.draw()
        # создали навую рисовалку, нужно об этом как-то сообщить
        flag = 1

    player = Player(screen, x_client, y_client, l)
    player.draw()

    N1 = len(objects_server)
    for obj in objects_server[N1-1]:
            obj.draw()

    another_player = Another_Player(screen, x_server, y_server, l)
    another_player.draw()

    boundaries = Boundaries(screen, width, height)
    boundaries.draw()

    Arrow_botton1 = Arrow_botton(screen, width, height, 7 / 480 * width)
    Arrow_botton1.draw()

    Arrow_botton2 = Arrow_botton(screen, width, height, 247 / 480 * width)
    Arrow_botton2.draw()

    pygame.display.update()

    return screen, objects_client, objects_server, x_client, y_client, flag


def visual_server(screen, width, height, data_server, objects_server, objects_client, x_server, y_server,
                  x_client, y_client):
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

    flag = 0
    pygame.time.Clock().tick(60)
    v_server = 0
    h_server = 0
    data_movement = str(data_server[0])
    data_object = str(data_server[1])

    if str(data_movement) == 'W':
        y_server -= 20
    elif str(data_movement) == 'S':
        y_server += 20
    elif str(data_movement) == 'A':
        x_server -= 20
    elif str(data_movement) == 'D':
        x_server += 20

    N = len(objects_server)

    #for i in range(0, 6, 1):

    for obj in objects_server[N - 1]:
        obj.draw()

    if str(data_object) == 'W':
        wall = Wall(screen, x_server, y_server, l, (0, 0, 0), 'w')
        objects_server[N - 1].append(wall)
        wall.draw()
    elif str(data_object) == 'A':
        wall = Wall(screen, x_server, y_server, l, (0, 0, 0), 'a')
        objects_server[N - 1].append(wall)
        wall.draw()
    elif str(data_object) == 'S':
        wall = Wall(screen, x_server, y_server, l, (0, 0, 0), 's')
        objects_server[N - 1].append(wall)
        wall.draw()
    elif str(data_object) == 'D':
        wall = Wall(screen, x_server, y_server, l, (0, 0, 0), 'd')
        objects_server[N - 1].append(wall)
        wall.draw()
    elif str(data_object) == 'F':
        door = Door(screen, x_server, y_server, l, (120, 50, 0), 'w')
        objects_server[N - 1].append(door)
        door.draw()
    elif str(data_object) == 'C':
        door = Door(screen, x_server, y_server, l, (120, 50, 0), 'a')
        objects_server[N - 1].append(door)
        door.draw()
    elif str(data_object) == 'V':
        door = Door(screen, x_server, y_server, l, (120, 50, 0), 's')
        objects_server[N - 1].append(door)
        door.draw()
    elif str(data_object) == 'B':
        door = Door(screen, x_server, y_server, l, (120, 50, 0), 'd')
        objects_server[N - 1].append(door)
        door.draw()
    elif str(data_object) == 'K':
        key = Key(screen, x_server, y_server, l)
        objects_server[N - 1].append(key)
        key.draw()
    elif str(data_object) == 'R':
        revival = Revival(screen, x_server, y_server, l)
        objects_server[N - 1].append(revival)
        revival.draw()
    elif str(data_object) == 'P':
        portal = Portal(screen, x_server, y_server, l)
        objects_server[N - 1].append(portal)
        x_server = width * 3 / 4
        y_server = height * 2 / 3

        portal = Portal(screen, x_server, y_server, l)
        new_objects_server = []
        new_objects_server.append(portal)
        objects_server.append(new_objects_server)
        pygame.draw.rect(screen, (255, 255, 255), (width / 2 + 5, height * 1 / 3 + 5, width / 2, height * 2 / 3))
        portal.draw()
        flag = 1

    elif str(data_object) == 'E':
        armory = Armory(screen, x_server, y_server, l)
        objects_server[N-1].append(armory)
        armory.draw()
    elif str(data_object) == 'N':
        exp = Explored_square(screen, x_server, y_server, l)
        objects_server[N-1].append(exp)
        exp.draw()

    elif str(data_object) == 'M':
        minotaur = Minotaur(screen, x_server, y_server, l)
        objects_server[N-1].append(minotaur)

        x_server = width * 3 / 4
        y_server = height * 2 / 3
        revival = Revival(screen, x_server, y_server, l)

        new_objects_server = []
        new_objects_server.append(revival)
        objects_server.append(new_objects_server)
        pygame.draw.rect(screen, (255, 255, 255), (width / 2 + 5, height * 1 /3 + 5, width/2, height * 2 / 3))
        revival.draw()
        flag = 1

    another_player = Another_Player(screen, x_server, y_server, l)
    another_player.draw()

    N1 = len(objects_client)
    for obj in objects_client[N1 - 1]:
        obj.draw()

    player = Player(screen, x_client, y_client, l)
    player.draw()

    boundaries = Boundaries(screen, width, height)
    boundaries.draw()

    Arrow_botton1 = Arrow_botton(screen, width, height, 7 / 480 * width)
    Arrow_botton1.draw()

    Arrow_botton2 = Arrow_botton(screen, width, height,  247/ 480 * width)
    Arrow_botton2.draw()

    pygame.display.update()

    return screen, objects_server, objects_client, x_server, y_server, flag


def visual_parts(width, height, objects_server, objects_client, client_parts, server_parts):

    # рисование левого куска клиента
    if (client_parts[0] >= 0) and (client_parts[0] <= len(objects_client) - 1):
        x1 = objects_client[client_parts[0]][0].x
        y1 = objects_client[client_parts[0]][0].y
        dx1 = 3 / 8 * width - x1
        dy1 = 1 / 6 * height - y1
        for i in objects_client[client_parts[0]]:
            i.x += dx1
            i.y += dy1
            i.draw()
    # правого
    if client_parts[1] >= 0 and (client_parts[1] <= len(objects_client) - 1):
        x2 = objects_client[client_parts[1]][0].x
        y2 = objects_client[client_parts[1]][0].y
        dx2 = 1 / 8 * width - x2
        dy2 = 1 / 6 * height - y2
        for i in objects_client[client_parts[1]]:
            i.x += dx2
            i.y += dy2
            i.draw()

    # рисование левого у сервера
    if server_parts[0] >= 0 and (server_parts[0] <= len(objects_server) - 1):
        x3 = objects_server[server_parts[0]][0].x
        y3 = objects_server[server_parts[0]][0].y
        dx3 = 7 / 8 * width - x3
        dy3 = 1 / 6 * height - y3
        for i in objects_server[server_parts[0]]:
            i.x += dx3
            i.y += dy3
            i.draw()

    # правого
    if server_parts[1] >= 0 and (server_parts[1] <= len(objects_server) - 1):
        x4 = objects_server[server_parts[1]][0].x
        y4 = objects_server[server_parts[1]][0].y
        dx4 = 5 / 8 * width - x4
        dy4 = 1 / 6 * height - y4
        for i in objects_server[server_parts[1]]:
            i.x += dx4
            i.y += dy4
            i.draw()

    pygame.display.update()
    return objects_server, objects_client








