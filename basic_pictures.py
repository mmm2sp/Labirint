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
        door = Wall(self.screen, self.x, self.y, self.l, door.color, door.orientation)

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
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//2, self.y-self.l//2, self.l, self.l))
        pygame.draw.line(self.screen, (210, 210, 0), (self.x, self.y+self.l*2//5), (self.x, self.y-self.l*2//5), width = self.l//10)
        pygame.draw.circle(self.screen, (210, 210, 0), (self.x,self.y+self.l*2//5), self.l//4)
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
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//2, self.y-self.l//2, self.l, self.l))
        pygame.draw.polygon(self.screen, (120, 50, 0), [(self.x,self.y+self.l*2//5),(self.x-self.l*3//10,self.y-self.l//20*7),(self.x+self.l//20*6,self.y-self.l//20*7)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x-self.l//20*5,self.y-self.l//20*7),(self.x-self.l//20*4,self.y-self.l//20*9),(self.x-self.l//20*4,self.y-self.l//20*7)])
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.x+self.l//20*5,self.y-self.l//20*7),(self.x+self.l//20*4,self.y-self.l//20*9),(self.x+self.l//20*4,self.y-self.l//20*7)])
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x-self.l//20*2,self.y-self.l//20*2), self.l//20*1)
        pygame.draw.circle(self.screen, (255, 255, 255), (self.x+self.l//20*2,self.y-self.l//20*2), self.l//20*1)
        
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
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//2, self.y-self.l//2, self.l, self.l))
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
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//2, self.y-self.l//2, self.l, self.l))

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
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//2, self.y-self.l//2, self.l, self.l))
        pygame.draw.circle(self.screen, (190, 100, 250), (self.x, self.y), self.l//20*9)
        
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
        pygame.draw.rect(self.screen, (0, 200, 0), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//20*18, self.l//20*18), width = self.l//20*3)
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
        pygame.draw.rect(self.screen, (0, 0, 200), (self.x-self.l//20*9, self.y-self.l//20*9, self.l//20*18, self.l//20*18), width = self.l//20*3)

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
        pygame.draw.rect(self.screen, (230, 230, 230), (self.x-self.l//2, self.y-self.l//2, self.l, self.l))
        pygame.draw.line(self.screen, (120, 50, 0), (self.x-self.l//20*8, self.y+self.l//20*8), (self.x-self.l//20*7, self.y+self.l//20*7) , width = self.l//20*3)
        pygame.draw.polygon(self.screen, (160, 160, 160), [(self.x-self.l//20*6,self.y+self.l//20*8),(self.x-self.l//20*8,self.y+self.l//20*6),(self.x+self.l//20*8,self.y-self.l//20*8)])

class Boundaries:
    def __init__ (self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 0), (self.width/2, 0), (self.width/2, self.height), width = 10)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width/4, 0), (self.width/4, self.height), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (self.width*3/4, 0), (self.width*3/4, self.height), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height/3), (self.width, self.height/3), width = 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height*2/3), (self.width, self.height*2/3), width = 5)
        



