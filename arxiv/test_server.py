'''
Тесовый вариант сервера
Позволяет рисовать круги двум игрокам на экране хоста
'''

import socket
import pygame
import pygame.draw as dr


def server_step(x, y):
        dr.circle(screen, (100, 200, 150), (x + 10, y + 10), 20)
        pygame.display.update()
        print('ход сделан, ход соперника')
        conn.send(str.encode('ваш ход'))


def client_step(x, y):
        data = conn.recv(1024)
        if data.decode('utf-8') == 'W':
            dr.circle(screen, (100, 200, 150), (x + 10, y + 10), 20)
            pygame.display.update()
            conn.send(str.encode('ход сделан, ход соперника'))
            print('ваш ход')
            return 1
        else:
            return 0


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.0.104', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

flag = 1
x = 50
y = 50
x1 = 100
y1 = 100

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if flag % 2 == 1:
                    server_step(x, y)
                    flag = 0
                    x += 10
                    y += 10
    if flag % 2 == 0:
        n = client_step(x1, y1)
        x1 += 10
        y1 += 10
        flag += n

pygame.quit()
conn.close()