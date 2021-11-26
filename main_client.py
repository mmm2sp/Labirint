from visualisation import *
import pygame

data_client = 'NN'
data_server = 'NN'
width = 1200
height = 800 
objects_client = [[]*1]*6
objects_server = [[]*1]*6
flag_client = 0
flag_server = 0
x_client = width/8
y_client = height/6
x_server = width*5/8
y_server = height/6
Return_server = []
Return_client = []
pygame.init()
screen = pygame.display.set_mode((width,height))
screen.fill((255,255,255))
pygame.display.update()
finished = False

while not finished:
    data_client = str(input( 'data_client:    ' ))#пока что данные вводятся с клавиатуры, в дальнейшем будут получаться от сервера, в первый раз нужно передать 'NN'
    Return_client = visual_client(screen, width, height, flag_client, data_client, objects_client, objects_server, x_client, y_client, x_server, y_server)
    screen = Return_client[0]
    flag_client = Return_client[1]
    objects_client = Return_client[2]
    objects_server = Return_client[3]
    x_client = Return_client[4]
    y_client = Return_client[5]
    
    data_server = str(input( 'data_server:    ' ))#пока что данные вводятся с клавиатуры, в дальнейшем будут получаться от сервера, в первый раз нужно передать 'NN'
    Return_server = visual_server(screen, width, height, flag_server, data_server, objects_server, objects_client, x_server, y_server, x_client, y_client)
    screen = Return_server[0]
    flag_server = Return_server[1]
    objects_server = Return_server[2]
    objects_client = Return_server[3]
    x_server = Return_server[4]
    y_server = Return_server[5]
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        
    
    

pygame.quit()
