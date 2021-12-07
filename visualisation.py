from basic_pictures import *
import pygame


def visual_client(screen, width, height, data_client, objects_client, objects_server, x_client, y_client,
                  x_server, y_server):
    screen.fill((255, 255, 255))

    v_client = 0
    h_client = 0
    data_movement = str(data_client[0])
    data_object = str(data_client[1])

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
        wall = Wall(screen, x_client, y_client, (0, 0, 0), 'w')
        objects_client[N-1].append(wall)
        wall.draw()
    elif str(data_object) == 'A':
        wall = Wall(screen, x_client, y_client, (0, 0, 0), 'a')
        objects_client[N-1].append(wall)
        wall.draw()
    elif str(data_object) == 'S':
        wall = Wall(screen, x_client, y_client, (0, 0, 0), 's')
        objects_client[N-1].append(wall)
        wall.draw()
    elif str(data_object) == 'D':
        wall = Wall(screen, x_client, y_client, (0, 0, 0), 'd')
        objects_client[N-1].append(wall)
        wall.draw()
    elif str(data_object) == 'F':
        door = Door(screen, x_client, y_client, (120, 50, 0), 'w')
        objects_client[N-1].append(door)
        door.draw()
    elif str(data_object) == 'C':
        door = Door(screen, x_client, y_client, (120, 50, 0), 'a')
        objects_client[N-1].append(door)
        door.draw()
    elif str(data_object) == 'V':
        door = Door(screen, x_client, y_client, (120, 50, 0), 's')
        objects_client[N-1].append(door)
        door.draw()
    elif str(data_object) == 'B':
        door = Door(screen, x_client, y_client, (120, 50, 0), 'd')
        objects_client[N-1].append(door)
        door.draw()
    elif str(data_object) == 'K':
        key = Key(screen, x_client, y_client)
        objects_client[N-1].append(key)
        key.draw()
    elif str(data_object) == 'R':
        revival = Revival(screen, x_client, y_client)
        objects_client[N-1].append(revival)
        revival.draw()
    # разобраться отдельно
    elif str(data_object) == 'P':
        portal = Portal(screen, x_client, y_client)
        objects_client[N-1].append(portal)
        x_client = width / 4
        y_client = height * 2 / 3

        portal = Portal(screen, x_client, y_client)
        new_objects_client = []
        new_objects_client.append(portal)
        objects_client.append(new_objects_client)
        portal.draw()
        # создали навую рисовалку, нужно об этом как-то сообщить

    elif str(data_object) == 'E':
        armory = Armory(screen, x_client, y_client)
        objects_client[N-1].append(armory)
        armory.draw()
    elif str(data_object) == 'N':
        exp = Explored_square(screen, x_client, y_client)
        objects_client[N-1].append(exp)
        exp.draw()

    #разобраться отдельно
    elif str(data_object) == 'M':
        minotaur = Minotaur(screen, x_client, y_client)
        objects_client[N-1].append(minotaur)

        x_client = width * 1 / 4
        y_client = height * 2 / 3
        revival = Revival(screen, x_client, y_client)
        # рисуем по-новому
        new_objects_client = []
        new_objects_client.append(revival)
        objects_client.append(new_objects_client)
        revival.draw()
        # создали навую рисовалку, нужно об этом как-то сообщить


    player = Player(screen, x_client, y_client)
    player.draw()

    N1 = len(objects_server)
    for obj in objects_server[N1-1]:
            obj.draw()

    another_player = Another_Player(screen, x_server, y_server)
    another_player.draw()

    boundaries = Boundaries(screen, width, height)
    boundaries.draw()

    pygame.display.update()

    return screen, objects_client, objects_server, x_client, y_client


def visual_server(screen, width, height, data_server, objects_server, objects_client, x_server, y_server,
                  x_client, y_client):
    screen.fill((255, 255, 255))
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
        wall = Wall(screen, x_server, y_server, (0, 0, 0), 'w')
        objects_server[N - 1].append(wall)
        wall.draw()
    elif str(data_object) == 'A':
        wall = Wall(screen, x_server, y_server, (0, 0, 0), 'a')
        objects_server[N - 1].append(wall)
        wall.draw()
    elif str(data_object) == 'S':
        wall = Wall(screen, x_server, y_server, (0, 0, 0), 's')
        objects_server[N - 1].append(wall)
        wall.draw()
    elif str(data_object) == 'D':
        wall = Wall(screen, x_server, y_server, (0, 0, 0), 'd')
        objects_server[N - 1].append(wall)
        wall.draw()
    elif str(data_object) == 'F':
        door = Door(screen, x_server, y_server, (120, 50, 0), 'w')
        objects_server[N - 1].append(door)
        door.draw()
    elif str(data_object) == 'C':
        door = Door(screen, x_server, y_server, (120, 50, 0), 'a')
        objects_server[N - 1].append(door)
        door.draw()
    elif str(data_object) == 'V':
        door = Door(screen, x_server, y_server, (120, 50, 0), 's')
        objects_server[N - 1].append(door)
        door.draw()
    elif str(data_object) == 'B':
        door = Door(screen, x_server, y_server, (120, 50, 0), 'd')
        objects_server[N - 1].append(door)
        door.draw()
    elif str(data_object) == 'K':
        key = Key(screen, x_server, y_server)
        objects_server[N - 1].append(key)
        key.draw()
    elif str(data_object) == 'R':
        revival = Revival(screen, x_server, y_server)
        objects_server[N - 1].append(revival)
        revival.draw()
    elif str(data_object) == 'P':
        portal = Portal(screen, x_server, y_server)
        objects_server[N - 1].append(portal)
        x_server = width * 3 / 4
        y_server = height * 2 / 3

        portal = Portal(screen, x_server, y_server)
        new_objects_server = []
        new_objects_server.append(portal)
        objects_server.append(new_objects_server)
        portal.draw()

    elif str(data_object) == 'E':
        armory = Armory(screen, x_server, y_server)
        objects_server[N-1].append(armory)
        armory.draw()
    elif str(data_object) == 'N':
        exp = Explored_square(screen, x_server, y_server)
        objects_server[N-1].append(exp)
        exp.draw()

    elif str(data_object) == 'M':
        minotaur = Minotaur(screen, x_server, y_server)
        objects_server[N-1].append(minotaur)

        x_server = width * 3 / 4
        y_server = height * 2 / 3
        revival = Revival(screen, x_server, y_server)

        new_objects_server = []
        new_objects_server.append(revival)
        objects_server.append(new_objects_server)
        revival.draw()

    another_player = Another_Player(screen, x_server, y_server)
    another_player.draw()

    N1 = len(objects_client)
    for obj in objects_client[N1 - 1]:
        obj.draw()

    player = Player(screen, x_client, y_client)
    player.draw()

    boundaries = Boundaries(screen, width, height)
    boundaries.draw()

    pygame.display.update()

    return screen, objects_server, objects_client, x_server, y_server

# Написать стартовое меню

# Написать экран победы и поражения



