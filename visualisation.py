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
    data_key = bool(data_client[2]) #Есть ли у игрока ключ
    data_bullets = int(data_client[3]) #Количество пуль у игрока

    flag = 0
    final_flag = 0

    N = len(objects_client)

    for obj in objects_client[N-1]:
        obj.draw()

    #Сначала проверяем второй символ: действия, если стена или дверь
    set_move = {'W', 'A', 'S', 'D'}
    if data_object in set_move:
        wall = Wall(screen, x_client, y_client, l, (0, 0, 0), data_object.lower())
        objects_client[N-1].append(wall)
        wall.draw()
    elif data_object.upper() in set_move:
        door = Door(screen, x_client, y_client, l, (120, 50, 0), data_object.lower())
        objects_client[N-1].append(door)
        door.draw()
        
    #Сдвигаем изображение, если первый символ указывает направление или что там дверь, а игрок с ключом   
    if data_movement == 'W': y_client -= 20
    elif data_movement == 'S': y_client += 20
    elif data_movement == 'A': x_client -= 20
    elif data_movement == 'D': x_client += 20
    elif data_movement == 'w':
        y_client -= 20
        final_frame(screen, width, height, 1)
        final_flag = 1
    elif data_movement == 's':
        y_client += 20
        final_frame(screen, width, height, 1)
        final_flag = 1
    elif data_movement == 'a':
        x_client -= 20
        final_frame(screen, width, height, 1)
        final_flag = 1
    elif data_movement == 'd':
        x_client += 20
        final_frame(screen, width, height, 1)
        final_flag = 1
    elif data_movement == 'G': #Умер второй игрок
        print('RRR')
        #FixMe: надо реализовать смерть СЕРВЕРА в этом случае
    else: #Не переместились
        data_object = data_movement
        #Отрисовываем то, что в текущей клетке

    if final_flag == 0:

        if data_object == 'K':
            key = Key(screen, x_client, y_client, l)
            objects_client[N-1].append(key)
            key.draw()
        elif data_object == 'R':
            revival = Revival(screen, x_client, y_client, l)
            objects_client[N-1].append(revival)
            revival.draw()
        # разобраться отдельно
        elif data_object == 'P':
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

        elif data_object == 'E':
            armory = Armory(screen, x_client, y_client, l)
            objects_client[N-1].append(armory)
            armory.draw()
        elif data_object == 'N':
            exp = Explored_square(screen, x_client, y_client, l)
            objects_client[N-1].append(exp)
            exp.draw()

        #разобраться отдельно
        elif data_object == 'M':
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
        elif data_object == 'm':
            dead_minotaur = Dead_minotaur(screen, x_client, y_client, l)
            objects_client[N-1].append(dead_minotaur)
            dead_minotaur.draw()

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

    return screen, objects_client, objects_server, x_client, y_client, flag, final_flag


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

    final_flag = 0
    flag = 0
    pygame.time.Clock().tick(60)
    v_server = 0
    h_server = 0
    data_movement = str(data_server[0])
    data_object = str(data_server[1])
    data_key = bool(data_server[2]) #Есть ли у игрока ключ
    data_bullets = int(data_server[3]) #Количество пуль у игрока

    N = len(objects_server)

    #for i in range(0, 6, 1):

    for obj in objects_server[N - 1]:
        obj.draw()

    #Сначала проверяем второй символ: действия, если стена или дверь
    set_move = {'W', 'A', 'S', 'D'}
    if data_object in set_move:
        wall = Wall(screen, x_server, y_server, l, (0, 0, 0), data_object.lower())
        objects_server[N - 1].append(wall)
        wall.draw()
    elif data_object.upper() in set_move:
        door = Door(screen, x_server, y_server, l, (120, 50, 0), data_object.lower())
        objects_server[N - 1].append(door)
        door.draw()

    #Сдвигаем изображение, если первый символ указывает направление или что там дверь, а игрок с ключом     
    if data_movement == 'W': y_server -= 20
    elif data_movement == 'S': y_server += 20
    elif data_movement == 'A': x_server -= 20
    elif data_movement == 'D': x_server += 20
    elif data_movement == 'w':
        y_client -= 20
        final_frame(screen, width, height, 0)
        final_flag = 1
    elif data_movement == 's':
        y_server += 20
        final_frame(screen, width, height, 0)
        final_flag = 1
    elif data_movement == 'a':
        x_server -= 20
        final_frame(screen, width, height, 0)
        final_flag = 1
    elif data_movement == 'd':
        x_server += 20
        final_frame(screen, width, height, 0)
        final_flag = 1
    elif data_movement == 'G': #Умер второй игрок
        print('RRR')
        #FixMe: надо реализовать смерть КЛИЕНТА в этом случае
    else: #Не переместились
        data_object = data_movement
        #Отрисовываем то, что в текущей клетке

    if final_flag == 0:

        if data_object == 'K':
            key = Key(screen, x_server, y_server, l)
            objects_server[N - 1].append(key)
            key.draw()
        elif data_object == 'R':
            revival = Revival(screen, x_server, y_server, l)
            objects_server[N - 1].append(revival)
            revival.draw()
        elif data_object == 'P':
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

        elif data_object == 'E':
            armory = Armory(screen, x_server, y_server, l)
            objects_server[N-1].append(armory)
            armory.draw()
        elif data_object == 'N':
            exp = Explored_square(screen, x_server, y_server, l)
            objects_server[N-1].append(exp)
            exp.draw()

        elif data_object == 'M':
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
        elif data_object == 'm':
            dead_minotaur = Dead_minotaur(screen, x_server, y_server, l)
            objects_server[N-1].append(dead_minotaur)
            dead_minotaur.draw()

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

    return screen, objects_server, objects_client, x_server, y_server, flag, final_flag


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

def menu_server(screen, width, height):
    '''
    Функция рисует стартовый экран игрока, создающего сервер
    '''
    screen.fill((255,255,255))
    Opened_door(screen, width//8, height//5, 100).draw()
    Button(screen, width/2, height/2).draw()
    Minotaur(screen, width*5//6, height//4, 200).draw()
    Key(screen, width*5.25//6, height*3//4, 200).draw()
    x = width//24*4
    y = height*5.5//8
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
    screen.fill((255,255,255))
    Opened_door(screen, width//8, height//5, 100).draw()
    Typing_window(screen, width/2, height/2).draw()
    Minotaur(screen, width*5//6, height//4, 200).draw()
    Key(screen, width*5.25//6, height*3//4, 200).draw()
    x = width//24*4
    y = height*5.5//8
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
    Функция рисует на экране "анимацию" с сообщением о ситуации:
    Если situation = 0 - это проигрыш
    situation = 1 - это победа
    '''
    if situation == 0:
        winnercolor = (100, 100, 255)
        losercolor =(0, 200, 0)
        f = pygame.font.Font(None, 150)
        text = f.render('DEFEAT...', True, (255, 0, 0))
        
    if situation == 1:
        winnercolor = (0, 200, 0)
        losercolor =(100, 100, 255)
        f = pygame.font.Font(None, 150)
        text = f.render('VICTORY!', True, (0, 200, 0))
        
    screen.fill((255,255,255))
    Men(screen, width*3//4, height*2.5//8, winnercolor).draw_body()
    Men(screen, width*3//4, height*2.5//8, winnercolor).draw_legs_stand()
    Closed_door(screen, width//4, height//5, width//4).draw()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)
    
    screen.fill((255,255,255))
    Closed_door(screen, width//4, height//5, width//4).draw()
    Men(screen, width*4//8, height*2.5//8, winnercolor).draw_body()
    Men(screen, width*4//8, height*2.5//8, winnercolor).draw_legs_stand()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Fully_opened_door(screen, width//4, height//5, width//4).draw()
    Men(screen, width*3//8, height*2.5//8, winnercolor).draw_body()
    Men(screen, width*3//8, height*2.5//8, winnercolor).draw_legs_stand()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Opened_door(screen, width//4, height//5, width//4).draw()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Corner(screen, width, height).draw()
    Men(screen, width*5//8, height*2.5//8, losercolor).draw_body()
    Men(screen, width*5//8, height*2.5//8, losercolor).draw_legs_stand()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Corner(screen, width, height).draw()
    Men(screen, width*5//8, height*3//8, losercolor).draw_body()
    Men(screen, width*5//8, height*3//8, losercolor).draw_legs_sit()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Corner(screen, width, height).draw()
    Men(screen, width*5//8, height*3//8, (230, 230, 230)).draw_body()
    Men(screen, width*5//8, height*3//8, (230, 230, 230)).draw_legs_sit()
    Web(screen, width//4, height//2, 100).draw()
    Web(screen, width//8*6, height//5*3, 50).draw()
    Skull(screen, width*5//8, height*3//8, 150).draw()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)
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
    Функция рисует на экране "анимацию" с сообщением о ситуации:
    Если situation = 0 - это проигрыш
    situation = 1 - это победа
    '''
    if situation == 0:
        winnercolor = (100, 100, 255)
        losercolor =(0, 200, 0)
        f = pygame.font.Font(None, 150)
        text = f.render('DEFEAT...', True, (255, 0, 0))
        
    if situation == 1:
        winnercolor = (0, 200, 0)
        losercolor =(100, 100, 255)
        f = pygame.font.Font(None, 150)
        text = f.render('VICTORY!', True, (0, 200, 0))
        
    screen.fill((255,255,255))
    Men(screen, width*3//4, height*2.5//8, winnercolor).draw_body()
    Men(screen, width*3//4, height*2.5//8, winnercolor).draw_legs_stand()
    Closed_door(screen, width//4, height//5, width//4).draw()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)
    
    screen.fill((255,255,255))
    Closed_door(screen, width//4, height//5, width//4).draw()
    Men(screen, width*4//8, height*2.5//8, winnercolor).draw_body()
    Men(screen, width*4//8, height*2.5//8, winnercolor).draw_legs_stand()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Fully_opened_door(screen, width//4, height//5, width//4).draw()
    Men(screen, width*3//8, height*2.5//8, winnercolor).draw_body()
    Men(screen, width*3//8, height*2.5//8, winnercolor).draw_legs_stand()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Opened_door(screen, width//4, height//5, width//4).draw()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Corner(screen, width, height).draw()
    Men(screen, width*5//8, height*2.5//8, losercolor).draw_body()
    Men(screen, width*5//8, height*2.5//8, losercolor).draw_legs_stand()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Corner(screen, width, height).draw()
    Men(screen, width*5//8, height*3//8, losercolor).draw_body()
    Men(screen, width*5//8, height*3//8, losercolor).draw_legs_sit()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

    screen.fill((255,255,255))
    Corner(screen, width, height).draw()
    Men(screen, width*5//8, height*3//8, (230, 230, 230)).draw_body()
    Men(screen, width*5//8, height*3//8, (230, 230, 230)).draw_legs_sit()
    Web(screen, width//4, height//2, 100).draw()
    Web(screen, width//8*6, height//5*3, 50).draw()
    Skull(screen, width*5//8, height*3//8, 150).draw()
    screen.blit(text,(width*2.5//8, height//20))
    pygame.display.update()
    pygame.time.Clock().tick(1)

def key_and_knifes(screen, width, height, data_client, data_server):
    data_key_client = int(data_client[2]) #Есть ли у КЛИЕНТА ключ
    data_bullets_client = int(data_client[3]) #Количество пуль у КЛИЕНТА
    data_key_server = int(data_server[2]) #Есть ли у СЕРВЕРА ключ
    data_bullets_server = int(data_server[3]) #Количество пуль у СЕРВЕРА
    if data_key_client == 1:
        Getted_key(screen, width*7//16, height*7//8, 40).draw()
    if data_key_server == 1:
        Getted_key(screen, width*15//16, height*7//8, 40).draw()
    x = width//16
    y = height*7//8
    for i in range (data_bullets_client):
        Knife(screen, x, y, 40).draw()
        x+=40
    x = width*9//16
    for i in range (data_bullets_server):
        Knife(screen, x, y, 40).draw()
        x+=40

def Your_step(screen, width, height):
    Flag(screen, width//4, height//3 + 40, 60, (0, 220, 0)).draw()

def Opponent_step(screen, width, height):
    Flag(screen, width//4*3, height//3 + 40, 60, (255, 0, 0)).draw()
    

        



    
