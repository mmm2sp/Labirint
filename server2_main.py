import pygame
import socket
from server2 import *

IP = '192.168.0.104'
Port = 9090
conn = connection(IP, Port)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

flag = 1  # флаг хода игрока-сервера, нужно согласовать флаг с клиентом

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            # наш ход
            if event.key == pygame.K_UP:
                if flag == 1:
                    info = check('W', labirint)  # написать эту функцию
                    # рисование в зависимости от info
                    flag = 0
                    # обновление лабиринта (переписывание координат клиента - сервера)
                    say_to_client_about_serv_step(info[0], info[1], conn)
            # if event.key == pygame.K_DOWN:...
    # ход соперника
    if flag == 0:

        ans = answer_to_client_step(labirint, conn)  # только здесь читаем данные от клиента
        # в зависимости, что за ответ, меняем лабиринт (записываем перемещение удаленного клиента)
        # в зависимости, что за ответ, рисуем новое положение удаленного клиента
        flag = 1

pygame.quit()
conn.close()