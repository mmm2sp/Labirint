import socket
import pygame
from client import *

IP = '192.168.0.104'
Port = 9090
sock = connection(IP, Port)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

flag = 1  # флаг хода игрока-сервера, нужно будет согласовать флаг с сервером

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        # наш ход
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if flag == 0:
                    info = ask_server('W', sock)
                    # рисование в зависимости от info
                    flag = 1
            # if event.key == pygame.K_DOWN:...

    # ход соперника
    if flag == 1:

        server_step = catch_server_steps(sock)
        # в зависимости, что за ответ, рисуем новое положение клиента-сервера(соперника)
        flag = 0

pygame.quit()
sock.close()