import pygame

class Wall:
    '''
    По координатам центра клетки x и y ставим стену с размером клеточки l,
    параметр orientation отвечает за расположение стены относительно клеточки:
    w - стена сверху
    a - стена слева
    s - стена снизу
    d - стена справа
    '''
    def __init__(self, screen, x, y, l, color, orientation):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.l = l
        self.orientation = str(orientation)
        
    def draw(self):
        '''
        Стена сверху:
        '''
        if self.orientation == 'w':
            pygame.draw.line(self.screen, self.color, (self.x-self.l//2,self.y-self.l//2), (self.x+self.l//2,self.y-self.l//2), width=self.l*3//20)
        '''
        Стена снизу:
        '''
        if self.orientation == 's':
            pygame.draw.line(self.screen, self.color, (self.x-self.l//2,self.y+self.l//2), (self.x+self.l//2,self.y+self.l//2), width=self.l*3//20)
        '''
        Стена слева:
        '''
        if self.orientation == 'a':
            pygame.draw.line(self.screen, self.color, (self.x-self.l//2,self.y-self.l//2), (self.x-self.l//2,self.y+self.l//2), width=self.l*3//20)
        '''
        Стена справа:
        '''
        if self.orientation == 'd':
            pygame.draw.line(self.screen, self.color, (self.x+self.l//2,self.y-self.l//2), (self.x+self.l//2,self.y+self.l//2), width=self.l*3//20)
        
class Door(Wall):
    '''
    Рисует дверь по координатам центра клетки
    '''
    def draw_door(self):
        door = Wall(self.screen, self.x, self.y, self.l, (155, 0, 0), door.orientation)

class Key:
    '''
    Рисует ключ по координатам центра клетки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//10*9, self.l//10*9))
        pygame.draw.line(self.screen, (210, 210, 0), (self.x, self.y+self.l*2//5), (self.x, self.y-self.l*2//5), width = self.l//10)
        pygame.draw.circle(self.screen, (210, 210, 0), (self.x,self.y+self.l//5), self.l*2//9.5)
        pygame.draw.rect(self.screen, (210, 210, 0), (self.x, self.y-self.l*2//5,self.l*3//20, self.l//5))

class Getted_key:
    '''
    Рисует ключ по координатам его "центра"
    этот нужен для информации о наличии ключа
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.line(self.screen, (210, 210, 0), (self.x, self.y+self.l*2//5), (self.x, self.y-self.l*2//5), width = self.l//10)
        pygame.draw.circle(self.screen, (210, 210, 0), (self.x,self.y+self.l//5), self.l*2//9.5)
        pygame.draw.rect(self.screen, (210, 210, 0), (self.x, self.y-self.l*2//5,self.l*3//20, self.l//5))   

class Minotaur:
    '''
    Рисует минотавра по координатам центра клетки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//10*9, self.l//10*9))
        pygame.draw.polygon(self.screen, (120, 50, 0), [(self.x,self.y+self.l*2//5),(self.x-self.l*3//10,self.y-self.l//20*7),(self.x+self.l//20*6,self.y-self.l//20*7)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x-self.l//20*5,self.y-self.l//20*7),(self.x-self.l//20*4,self.y-self.l//20*9),(self.x-self.l//20*4,self.y-self.l//20*7)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x+self.l//20*5,self.y-self.l//20*7),(self.x+self.l//20*4,self.y-self.l//20*9),(self.x+self.l//20*4,self.y-self.l//20*7)])
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x-self.l//20*2,self.y-self.l//20*2), self.l//20*1)
        pygame.draw.circle(self.screen, (255, 0, 0), (self.x+self.l//20*2,self.y-self.l//20*2), self.l//20*1)

class Dead_minotaur:
    '''
    Рисует убитого минотавра по координатам центра клетки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//10*9, self.l//10*9))
        pygame.draw.polygon(self.screen, (120, 50, 0), [(self.x - self.l//20*9, self.y + self.l//20*9), (self.x + self.l//20*9, self.y + self.l//20*9), (self.x + self.l//20*2, self.y)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x + self.l//20*4, self.y + self.l//20), (self.x + self.l//20*6, self.y + self.l//20),
                                                     (self.x + self.l//20*5, self.y + self.l//20*2)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x + self.l//20*7, self.y + self.l//20*7), (self.x + self.l//20*8, self.y + self.l//20*8),
                                                     (self.x + self.l//20*9, self.y + self.l//20*7)])
        pygame.draw.polygon(self.screen, (0, 0, 0), (self.x + self.l//20, self.y + self.l//20*3), self.l//20*2)
        pygame.draw.polygon(self.screen, (0, 0, 0), (self.x + self.l//20*3, self.y + self.l//20*7), self.l//20*2)
        
class Revival:
    '''
    Рисует место возрождения после смерти по координатам центра клетки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//10*9, self.l//10*9))
        pygame.draw.line(self.screen, (255,0,0), (self.x, self.y-self.l//20*8), (self.x, self.y+self.l//20*8), width = self.l//20*8)
        pygame.draw.line(self.screen, (255,0,0), (self.x-self.l//20*8, self.y), (self.x+self.l//20*8, self.y), width = self.l//20*8)

class Explored_square:
    '''
    Рисует исследованную клетку по координатам её центра
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//10*9, self.l//10*9))

class Portal:
    '''
    Рисует портал по координатам центра клетки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//10*9, self.l//10*9))
        pygame.draw.circle(self.screen, (190, 100, 250), (self.x, self.y), self.l//20*8)
        
class Player:
    '''
    Рисует игрока по координатам центра клетки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (0, 200, 0), (self.x-self.l//20*8, self.y-self.l//20*8, self.l//20*16, self.l//20*16), width = self.l//10)
        
class Another_Player:
    '''
    Рисует противника по координатам центра клетки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (100, 100, 255), (self.x-self.l//20*8, self.y-self.l//20*8, self.l//20*16, self.l//20*16), width = self.l//10)

class Armory:
    '''
    Рисует арсенал по координатам центра клетки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//10*9, self.l//10*9))
        pygame.draw.line(self.screen, (120, 50, 0), (self.x-self.l//20*9, self.y+self.l//20*9), (self.x-self.l//20*5, self.y+self.l//20*5) , width = self.l//20*3)
        pygame.draw.polygon(self.screen, (160, 160, 160), [(self.x-self.l//20*8,self.y+self.l//20*3),(self.x-self.l//20*3,self.y+self.l//20*8),(self.x+self.l//20*8,self.y-self.l//20*8)])

class Knife:
    '''
    Рисует кинжал по координатам его "центра"
    нужно для информации о наличии оружия
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.line(self.screen, (120, 50, 0), (self.x-self.l//20*9, self.y+self.l//20*9), (self.x-self.l//20*5, self.y+self.l//20*5) , width = self.l//20*3)
        pygame.draw.polygon(self.screen, (160, 160, 160), [(self.x-self.l//20*8,self.y+self.l//20*3),(self.x-self.l//20*3,self.y+self.l//20*8),(self.x+self.l//20*8,self.y-self.l//20*8)])    

class Boundaries:
    '''
    Рисует границы игровых полей по размерам экрана
    '''
    def __init__ (self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 0), (self.width/2, 0), (self.width/2, self.height), width = 10)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height/3), (self.width, self.height/3), width = 5)


class Arrow_botton:
    '''
    Рисует кнопки переключения фрагментов
    '''
    def __init__(self, screen, width, height, x):
        self.screen = screen
        self.width = width
        self.height = height
        self.x = x
    def draw(self):
        pygame.draw.rect(self.screen, (100, 150, 200),
                         (self.x, 7/60 * self.height, 1/30 * self.width, 1/20 * self.height))

        pygame.draw.rect(self.screen, (100, 150, 200),
                         (self.x + 210/480 * self.width, 7/60 * self.height, 1 / 30 * self.width, 1 / 20 * self.height))

class Opened_door:
    '''
    Рисует открытую дверь по координатам верхнего левого угла дверной коробки
    Нужно для меню
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (200, 200, 0), (self.x, self.y, self.l, 2*self.l))
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y), (self.x+self.l, self.y), width = self.l//20)
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y), (self.x, self.y+2*self.l), width = self.l//20)
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y+2*self.l), (self.x+self.l//10, self.y+2*self.l), width = self.l//20)
        pygame.draw.polygon(self.screen, (155, 0, 0), [(self.x+self.l, self.y),(self.x+self.l//10, self.y+self.l//3),(self.x+self.l//10, self.y+self.l*2.33),(self.x+self.l, self.y+2*self.l)])

class Button:
    '''
    Рисуем кнопку создания лабиринта на стартовом экране игрока-сервера по координатам x, y
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (200, 200, 200), (self.x - 200, self.y - 100, 400, 200))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x - 200, self.y - 100, 400, 200), width = 10) 
        f1 = pygame.font.Font(None, 80)
        text1 = f1.render('Создать', True, (0, 0, 0))
        text2 = f1.render('лабиринт', True, (0, 0, 0))
        text3 = f1.render('и сервер', True, (0, 0, 0))
        self.screen.blit(text1,(self.x-190,self.y-90))
        self.screen.blit(text2,(self.x-150,self.y - 30))
        self.screen.blit(text3,(self.x-70,self.y+30))

class Typing_window:
    '''
    Рисуем окошко ввода IP-адреса на стартовом экране игрока-клиента по координатам x, y
    '''
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
    def draw(self):
        pygame.draw.rect(self.screen, (200, 200, 200), (self.x - 200, self.y - 100, 400, 200))
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x - 200, self.y - 100, 400, 200), width = 10)
        pygame.draw.line(self.screen, (100, 100, 100), (self.x - 190, self.y + 90), (self.x + 190, self.y + 90), width = 3)
        f1 = pygame.font.Font(None, 80)
        text1 = f1.render('Введите', True, (0, 0, 0))
        text2 = f1.render('IP-адрес', True, (0, 0, 0))
        text3 = f1.render('сервера:', True, (0, 0, 0))
        self.screen.blit(text1,(self.x - 190,self.y - 95))
        self.screen.blit(text2,(self.x - 150,self.y - 48))
        self.screen.blit(text3,(self.x - 70,self.y-3))

class Men:
    '''
    Рисует человечка с квадратной башкой для кат-сцен победы и поражения
    по координатам центра головы
    '''
    def __init__(self, screen, x, y, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
    def draw_body(self):
        pygame.draw.rect(self.screen, self.color, (self.x-75, self.y - 75, 150, 150))
        pygame.draw.line(self.screen, self.color, (self.x, self.y + 75), (self.x, self.y + 375), width = 10)
        pygame.draw.line(self.screen, self.color, (self.x, self.y + 125), (self.x+100, self.y + 275), width = 10)
        pygame.draw.line(self.screen, self.color, (self.x, self.y + 125), (self.x-100, self.y + 275), width = 10)
    def draw_legs_stand(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y + 375), (self.x + 125, self.y + 500), width = 10)
        pygame.draw.line(self.screen, self.color, (self.x, self.y + 375), (self.x - 125, self.y + 500), width = 10)
    def draw_legs_sit(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y + 375), (self.x - 175, self.y + 400), width = 10)
        pygame.draw.line(self.screen, self.color, (self.x, self.y + 375), (self.x - 125, self.y + 450), width = 10)


class Closed_door:
    '''
    Рисует закрытую дверь для кат сцены по координатам верхнего левого угла дверной коробки
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (155, 0, 0), (self.x, self.y, self.l, 2*self.l))
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y), (self.x+self.l, self.y), width = self.l//20)
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y), (self.x, self.y+2*self.l), width = self.l//20)
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y+2*self.l), (self.x+self.l, self.y+2*self.l), width = self.l//20)

class Fully_opened_door:
    '''
    Рисует полностью открытую дверь по координатам верхнего левого угла дверной коробки
    Нужно для кат сцены
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.rect(self.screen, (200, 200, 0), (self.x, self.y, self.l, 2*self.l))
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y), (self.x+self.l, self.y), width = self.l//20)
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y), (self.x, self.y+2*self.l), width = self.l//20)
        pygame.draw.line(self.screen, (155, 0, 0), (self.x, self.y+2*self.l), (self.x+self.l, self.y+2*self.l), width = self.l//20)
        pygame.draw.polygon(self.screen, (155, 0, 0), [(self.x+self.l, self.y),(self.x+self.l//10*19, self.y+self.l//3),
                                                       (self.x+self.l//10*19, self.y+self.l*2.33),(self.x+self.l, self.y+2*self.l)])

class Corner:
    '''
    Рисует угол в лабиринте по размерам экрана, нужно для кат-сцены
    '''
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.polygon(self.screen, (200, 200, 200), [(self.width//2, self.height//5), (self.width, self.height//5*2), (self.width, self.height), (self.width//2, self.height//5*4)])
        pygame.draw.polygon(self.screen, (200, 200, 200), [(self.width//2, self.height//5), (0, self.height//5*2), (0, self.height), (self.width//2, self.height//5*4)])
        pygame.draw.line(self.screen, (0, 0, 0), (self.width//2, self.height//5), (self.width//2, self.height//5*4), width = 10)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width//2, self.height//5), (self.width, self.height//5*2), width = 10)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width//2, self.height//5), (0, self.height//5*2), width = 10)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width//2, self.height//5*4), (self.width, self.height), width = 10)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width//2, self.height//5*4), (0, self.height), width = 10)

class Web:
    '''
    Рисует паутину размера l по координатам ее центра x,y
    Нужно для кат-сцены
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        l = self.l
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), l//3, width = 5)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), l//3*2, width = 5)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x, self.y), l, width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x - l, self.y + l), (self.x + l, self.y - l), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x - l, self.y - l), (self.x + l, self.y + l), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y + l), (self.x, self.y - l), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.x - l, self.y), (self.x + l, self.y), width = 5)
        
class Skull:
    '''
    Рисует глаза и рот черепа проигравшего игрока в кат-сцене
    Размера l, по координтам центра головы
    '''
    def __init__(self, screen, x, y, l):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x - self.l//4, self.y - self.l//4), self.l//15)
        pygame.draw.circle(self.screen, (0, 0, 0), (self.x + self.l//4, self.y - self.l//4), self.l//15)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x - self.l//4, self.y + self.l//4, self.l//2, self.l//10))

class Flag:
    '''
    Рисует флаг, обозначающий ход
    по координатам верхнего конца флагштока
    длина флагштока l
    '''
    def __init__(self, screen, x, y, l, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.l = l
        self.color = color
    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + self.l))
        pygame.draw.polygon(self.screen, self.color, [(self.x, self.y),(self.x + self.l, self.y),
                                                      (self.x + self.l//2, self.y + self.l//4),
                                                      (self.x + self.l, self.y + self.l//2),
                                                      (self.x, self.y + self.l//2)])
    
