from basic_pictures import *
import pygame

def visual_client(screen, width, height, flag_client, data_client, objects_client, objects_server, x_client, y_client, x_server, y_server):
    
    l = 20
    screen.fill((255,255,255))
    pygame.time.Clock().tick(60)
    v_client = 0
    h_client = 0
    data_movement = str(data_client[0])
    data_object = str(data_client[1])

    if str(data_movement) == 'W':
        y_client-=20
    elif str(data_movement) == 'S':
        y_client+=20
    elif str(data_movement) == 'A':
        x_client-=20
    elif str(data_movement) == 'D':
        x_client+=20
            
    for i in range(0,6,1):
        for obj in objects_client[i]:
            obj.draw()
                    
    if str(data_object) == 'W':
        wall=Wall(screen,x_client, y_client, l, (0, 0, 0), 'w')
        objects_client[flag_client].append(wall)
        wall.draw()
    elif str(data_object) == 'A':
        wall=Wall(screen, x_client, y_client, l, (0, 0, 0), 'a')
        objects_client[flag_client].append(wall)
        wall.draw()
    elif str(data_object) == 'S':
        wall=Wall(screen, x_client, y_client, l, (0, 0, 0), 's')
        objects_client[flag_client].append(wall)
        wall.draw()
    elif str(data_object) == 'D':
        wall=Wall(screen, x_client, y_client, l, (0, 0, 0), 'd')
        objects_client[flag_client].append(wall)
        wall.draw()
    elif str(data_object) == 'F':
        door=Door(screen, x_client, y_client, l, (120, 50, 0), 'w')
        objects_client[flag_client].append(door)
        door.draw()
    elif str(data_object) == 'C':
        door=Door(screen, x_client, y_client, l, (120, 50, 0), 'a')
        objects_client[flag_client].append(door)
        door.draw()
    elif str(data_object) == 'V':
        door=Door(screen, x_client, y_client, l, (120, 50, 0), 's')
        objects_client[flag_client].append(door)
        door.draw()
    elif str(data_object) == 'B':
        door=Door(screen,  x_client, y_client, l, (120, 50, 0), 'd')
        objects_client[flag_client].append(door)
        door.draw()
    elif str(data_object) == 'K':
        key=Key(screen, x_client, y_client, l)
        objects_client[flag_client].append(key)
        key.draw()
    elif str(data_object) == 'R':
        revival=Revival(screen, x_client, y_client, l)
        objects_client[flag_client].append(revival)
        revival.draw()
    elif str(data_object) == 'P':
        portal=Portal(screen, x_client, y_client, l)
        objects_client[flag_client].append(portal)
        portal.draw()
        if flag_client <= 1:
            flag_client = 2
        if flag_client == 2:
            flag_client += 1
            x_client = width/8
            y_client = height/2
            portal=Portal(screen, x_client, y_client, l)
            objects_client[flag_client].append(portal)
            portal.draw()
        elif flag_client == 3:
            flag_client += 1
            x_client = width*3/8
            y_client = height/2
            portal=Portal(screen, x_client, y_client, l)
            objects_client[flag_client].append(portal)
            portal.draw()
        elif flag_client == 4:
            flag_client += 1
            x_client = width/8
            y_client = height*5/6
            portal=Portal(screen, x_client, y_client, l)
            objects_client[flag_client].append(portal)
            portal.draw()
        elif flag_client == 5:
            flag_client = 2
            x_client = width*3/8
            y_client = height*5/6
            portal=Portal(screen, x_client, y_client, l)
            objects_client[flag_client].append(portal)
            portal.draw()
    elif str(data_object) == 'E':
        armory=Armory(screen, x_client, y_client, l)
        objects_client[flag_client].append(armory)
        armory.draw()
    elif str(data_object) == 'N':
        exp=Explored_square(screen, x_client, y_client, l)
        objects_client[flag_client].append(exp)
        exp.draw()
    elif str(data_object) == 'M':
        minotaur=Minotaur(screen, x_client, y_client, l)
        objects_client[flag_client].append(minotaur)
        minotaur.draw()
        flag_client = 1
        x_client = width*3/8
        y_client = height/6
        revival=Revival(screen, x_client, y_client, l)
        objects_client[flag_client].append(revival)
        revival.draw()
          
    player=Player(screen, x_client, y_client, l)
    player.draw()

    for i in range(0,6,1):
        for obj in objects_server[i]:
            obj.draw()

    another_player=Another_Player(screen, x_server, y_server, l)
    another_player.draw()

    boundaries = Boundaries(screen, width, height)
    boundaries.draw()

    pygame.display.update()

    return screen, flag_client, objects_client, objects_server, x_client, y_client

    
def visual_server(screen, width, height, flag_server, data_server, objects_server, objects_client, x_server, y_server, x_client, y_client):

    l = 20
    screen.fill((255,255,255))
    pygame.time.Clock().tick(60)
    v_server = 0
    h_server = 0
    data_movement = str(data_server[0])
    data_object = str(data_server[1])

    if str(data_movement) == 'W':
        y_server-=20
    elif str(data_movement) == 'S':
        y_server+=20
    elif str(data_movement) == 'A':
        x_server-=20
    elif str(data_movement) == 'D':
        x_server+=20
            
    for i in range(0,6,1):
        for obj in objects_server[i]:
            obj.draw()
                    
    if str(data_object) == 'W':
        wall=Wall(screen,x_server, y_server, l, (0, 0, 0), 'w')
        objects_server[flag_server].append(wall)
        wall.draw()
    elif str(data_object) == 'A':
        wall=Wall(screen, x_server, y_server, l, (0, 0, 0), 'a')
        objects_server[flag_server].append(wall)
        wall.draw()
    elif str(data_object) == 'S':
        wall=Wall(screen, x_server, y_server, l, (0, 0, 0), 's')
        objects_server[flag_server].append(wall)
        wall.draw()
    elif str(data_object) == 'D':
        wall=Wall(screen, x_server, y_server, l, (0, 0, 0), 'd')
        objects_server[flag_server].append(wall)
        wall.draw()
    elif str(data_object) == 'F':
        door=Door(screen, x_server, y_server, l, (120, 50, 0), 'w')
        objects_server[flag_server].append(door)
        door.draw()
    elif str(data_object) == 'C':
        door=Door(screen, x_server, y_server, l, (120, 50, 0), 'a')
        objects_server[flag_server].append(door)
        door.draw()
    elif str(data_object) == 'V':
        door=Door(screen, x_server, y_server, l, (120, 50, 0), 's')
        objects_server[flag_server].append(door)
        door.draw()
    elif str(data_object) == 'B':
        door=Door(screen,  x_server, y_server, l, (120, 50, 0), 'd')
        objects_server[flag_server].append(door)
        door.draw()
    elif str(data_object) == 'K':
        key=Key(screen, x_server, y_server, l)
        objects_server[flag_server].append(key)
        key.draw()
    elif str(data_object) == 'R':
        revival=Revival(screen, x_server, y_server, l)
        objects_server[flag_server].append(revival)
        revival.draw()
    elif str(data_object) == 'P':
        portal=Portal(screen, x_server, y_server, l)
        objects_server[flag_server].append(portal)
        portal.draw()
        if flag_server <= 1:
            flag_server = 2
        if flag_server == 2:
            flag_server += 1
            x_server = width*5/8
            y_server = height/2
            portal=Portal(screen, x_server, y_server, l)
            objects_server[flag_server].append(portal)
            portal.draw()
        elif flag_server == 3:
            flag_server += 1
            x_server = width*7/8
            y_server = height/2
            portal=Portal(screen, x_server, y_server, l)
            objects_server[flag_server].append(portal)
            portal.draw()
        elif flag_server == 4:
            flag_server += 1
            x_server = width*5/8
            y_server = height*5/6
            portal=Portal(screen, x_server, y_server, l)
            objects_server[flag_server].append(portal)
            portal.draw()
        elif flag_server == 5:
            flag_server = 2
            x_server = width*7/8
            y_server = height*5/6
            portal=Portal(screen, x_server, y_server, l)
            objects_server[flag_server].append(portal)
            portal.draw()
    elif str(data_object) == 'E':
        armory=Armory(screen, x_server, y_server, l)
        objects_server[flag_server].append(armory)
        armory.draw()
    elif str(data_object) == 'N':
        exp=Explored_square(screen, x_server, y_server, l)
        objects_server[flag_server].append(exp)
        exp.draw()
    elif str(data_object) == 'M':
        minotaur=Minotaur(screen, x_server, y_server, l)
        objects_server[flag_server].append(minotaur)
        minotaur.draw()
        flag_server = 1
        x_server = width*7/8
        y_server = height/6
        revival=Revival(screen, x_server, y_server, l)
        objects_server[flag_server].append(revival)
        revival.draw()
          
    another_player=Another_Player(screen, x_server, y_server, l)
    another_player.draw()

    for i in range(0,6,1):
        for obj in objects_client[i]:
            obj.draw()

    player=Player(screen, x_client, y_client, l)
    player.draw()

    boundaries = Boundaries(screen, width, height)
    boundaries.draw()

    pygame.display.update()

    return screen, flag_server, objects_server, objects_client, x_server, y_server

        
        
