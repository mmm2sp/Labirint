import pygame
import socket

'''
Модуль клиента
Описаны функции для клиента, реализующие взаимодействие между клиентом и сервером
'''


def connection(IP, Port):
    '''
    Подключается к серверу
    :param IP: адрес сервера, к которому подключаемся
    :param Port: порт, к которому подключаемся
    :return: подключенный сокет
    '''
    sock = socket.socket()
    sock.connect((IP, Port))
    return sock


def ask_server(vector, sock):
    '''
    отправляет запрос на сервер, можно ли сходить в направлении vector
    :param vector: направление, куда хочется сходить wasd
    :return: ответ сервера в виде wasd + буква предмета в клетке, куда пришли
    '''
    sock.send(vector.encode('utf-8'))
    data = sock.recv(1024)
    return data.decode('utf-8')


def catch_server_steps(sock):
    '''
    Ловит инфу от сервера о его ходах
    :param sock: подключенный к серверу сокет
    :return: информацию переданную сервером
    '''
    data = sock.recv(1024)

    return data.decode('utf-8')


def Typing(ip, x, y, event, screen):
    '''
    Функция обрабатывает ввод IP-адреса игроком-клиентом
    Функция возвращает введенный адрес,
    отображает ввод на стартовом экране по координтам x, y центра окошка ввода
    :param ip: адрес сервера
    :param x: координата х середины экрана
    :param y: координата у середины экрана
    :param event: событие paygame
    :param screen: экран pygame
    '''
    f1 = pygame.font.Font(None, 70)
    x = x - 190
    y = y + 45
    s = 0
    if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
        ip += '0'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        ip += '1'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
        ip += '2'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
        ip += '3'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
        ip += '4'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
        ip += '5'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
        ip += '6'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
        ip += '7'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
        ip += '8'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
        ip += '9'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_PERIOD:
        ip += '.'
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
        ip = ip[:(len(ip) - 1)]
        pygame.draw.rect(screen, (200, 200, 200), (x, y + 4, 380, 40))
        screen.blit(f1.render(str(ip), True,
                              (0, 0, 0)), (x, y))
        pygame.display.update()
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        s = 1
    return ip, s


if __name__ == "__main__":
    print("This module is not for direct call!")
