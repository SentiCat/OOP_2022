import pygame
from pygame.draw import *

def house_make(x, y):
    #основа
    rect(screen, (52, 59, 41), (x, y, 205, 220))
    rect(screen, (76, 47, 39), (x, y, 205, 70))
    #крыша
    polygon(screen, (0, 0, 0), ((x - 25, y + 5), (x + 15, y - 17), (x + 190, y - 17), (x + 230, y + 5)))
    #трубы
    rect(screen, (34, 34, 34), (x + 125, y - 40, 5, 23))
    rect(screen, (34, 34, 34), (x + 30, y - 45, 7, 39))
    rect(screen, (34, 34, 34), (x + 41, y - 50, 14, 44))
    rect(screen, (34, 34, 34), (x + 171, y - 40, 7, 34))
    #верхние окна
    rect(screen, (151, 123, 128), (x + 15, y + 5, 20, 63))
    rect(screen, (151, 123, 128), (x + 55, y + 5, 20, 63))
    rect(screen, (151, 123, 128), (x + 105, y + 5, 20, 63))
    rect(screen, (151, 123, 128), (x + 145, y + 5, 20, 63))
    #нижние окна
    rect(screen, (77, 34, 14), (x + 15, y + 155, 50, 40))
    rect(screen, (77, 34, 14), (x + 80, y + 155, 50, 40))
    rect(screen, (225, 255, 0), (x + 145, y + 155, 50, 40))
    #подоконник
    rect(screen, (51, 51, 51), (x - 25, y + 68, 255, 20))
    rect(screen, (51, 51, 51), (x - 5, y + 43, 215, 10))
    rect(screen, (51, 51, 51), (x - 15, y + 53, 10, 15))
    rect(screen, (51, 51, 51), (x + 210, y + 53, 10, 15))
    rect(screen, (51, 51, 51), (x + 25, y + 53, 10, 15))
    rect(screen, (51, 51, 51), (x + 65, y + 53, 10, 15))
    rect(screen, (51, 51, 51), (x + 105, y + 53, 10, 15))
    rect(screen, (51, 51, 51), (x + 145, y + 53, 10, 15))
    rect(screen, (51, 51, 51), (x + 185, y + 53, 10, 15))
    return 0;

def rghost_make(x, y, s):
    #основа
    polygon(screen, (225, 225, 225, 128), ((x, y), (x + s * 20, y - s * 45), (x + s * 55, y - s * 45), (x + s * 55, y - s * 40), (x + s * 100, y + s * 5)))
    #формирование
    circle(screen, (0, 0, 0), (x + s * 80, y + s * 25), s * 30)
    circle(screen, (0, 0, 0), (x + s * 40, y + s * 15), s * 20)
    circle(screen, (0, 0, 0), (x + s * 12, y + s * 5), s * 10)
    #скругление
    circle(screen, (225, 225, 225), (x + s * 60, s * y), s * 5)
    circle(screen, (225, 225, 225), (x + s * 25, y - s * 2), s * 5)
    circle(screen, (225, 225, 225), (x + s * 2, s * y), s * 2)
    circle(screen, (225, 225, 225), (x + s * 24, y - s * 45), s * 2)
    #голова
    circle(screen, (225, 225, 225), (x + s * 44, y - s * 50), s * 20)
    #глазные яблоки
    circle(screen, (0, 191, 225), (x + s * 40, y - s * 50), s * 5)
    circle(screen, (0, 191, 225), (x + s * 55, y - s * 50), s * 5)
    #зрачки
    circle(screen, (0, 0, 0), (x + s * 42, y - s * 50), s * 2)
    circle(screen, (0, 0, 0), (x + s * 57, y - s * 50), s * 2)
    #блики
    line(screen, (225, 225, 225), (x + s * 35, y - s * 51), (x + s * 40, y - s * 50), s)
    line(screen, (225, 225, 225), (x + s * 50, y - s * 51), (x + s * 55, y - s * 50), s)

def lghost_make(x, y, s):
    #основа
    polygon(screen, (225, 225, 225, 128), ((1000 - x, y), (1000 - (x + s * 20), y - s * 45), (1000 - (x + s * 55), y - s * 45), (1000 -(x + s * 55), y - s * 40), (1000 -(x + s * 100), y + s * 5)))
    #формирование
    circle(screen, (0, 0, 0), (1000 - (x + s * 80), y + s * 25), s * 30)
    circle(screen, (0, 0, 0), (1000 - (x + s * 40), y + s * 15), s * 20)
    circle(screen, (0, 0, 0), (1000 - (x + s * 12), y + s * 5), s * 10)
    #скругление
    circle(screen, (225, 225, 225), (1000 - (x + s * 60), s * y), s * 5)
    circle(screen, (225, 225, 225), (1000 - (x + s * 25), y - s * 2), s * 5)
    circle(screen, (225, 225, 225), (1000 - (x + s * 2), s * y), s * 2)
    circle(screen, (225, 225, 225), (1000 - (x + s * 24), y - s * 45), s * 2)
    #голова
    circle(screen, (225, 225, 225), (1000 - (x + s * 44), y - s * 50), s * 20)
    #глазные яблоки
    circle(screen, (0, 191, 225), (1000 - (x + s * 40), y - s * 50), s * 5)
    circle(screen, (0, 191, 225), (1000 - (x + s * 55), y - s * 50), s * 5)
    #зрачки
    circle(screen, (0, 0, 0), (1000 - (x + s * 42), y - s * 50), s * 2)
    circle(screen, (0, 0, 0), (1000 - (x + s * 57), y - s * 50), s * 2)
    #блики
    line(screen, (225, 225, 225), (1000 - (x + s * 35), y - s * 51), (1000 - (x + s * 40), y - s * 50), s)
    line(screen, (225, 225, 225), (1000 - (x + s * 50), y - s * 51), (1000 - (x + s * 55), y - s * 50), s)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 650))

#фон
rect(screen, (85, 85, 85), (0, 0, 1000, 250))

#луна
circle(screen, (225, 225, 225), (950, 40), 40)

#домик2
house_make(300, 200)

#облако1
ellipse(screen, (160, 160, 160), (0, 285, 500, 30))

#домики 1 и 3
house_make(25, 275)
house_make(725, 175)

#остальные облака
ellipse(screen, (96, 96, 96), (450, 255, 650, 30))
ellipse(screen, (64, 64, 64), (200, 210, 850, 50))
ellipse(screen, (32, 32, 32), (450, 150, 650, 40))

ellipse(screen, (96, 96, 96), (600, 110, 450, 30))
ellipse(screen, (64, 64, 64), (50, 35, 825, 40))
ellipse(screen, (96, 96, 96), (450, 25, 550, 30))

#призраки
rghost_make(45, 580, 1)
rghost_make(85, 595, 1)

lghost_make(15, 490, 1)
lghost_make(-10, 515, 1)

lghost_make(140, 570, 2)
lghost_make(260, 560, 1)

#rghost_make(240, 355, 1)
#rghost_make(240, 355, 1)
#lghost_make(240, 355, 1)
#rghost_make(240, 355, 2)
#polygon(screen, (225, 225, 225, 128), ((25, 585), (45, 540), (80, 540), (80, 545), (125, 590)))
#circle(screen, (0, 0, 0), (105, 610), 30)
#circle(screen, (0, 0, 0), (65, 600), 20)
#circle(screen, (0, 0, 0), (37, 590), 10)

#circle(screen, (225, 225, 225), (85, 585), 5)
#circle(screen, (225, 225, 225, 128), (50, 583), 5)
#circle(screen, (225, 225, 225), (27, 585), 2)

#circle(screen, (225, 225, 225), (69, 535), 20)
#circle(screen, (225, 225, 225), (49, 540), 2)

#circle(screen, (0, 191, 225), (65, 535), 5)
#circle(screen, (0, 191, 225), (80, 535), 5)
#circle(screen, (0, 0, 0), (67, 535), 2)
#circle(screen, (0, 0, 0), (82, 535), 2)
#line(screen, (225, 225, 225), (60, 534), (65, 535), 2)
#line(screen, (225, 225, 225), (75, 534), (80, 535), 2)

#polygon(screen, (225, 225, 225, 128), ((25, 590), (45, 540), (80, 540), (80, 545), (125, 585)))
#circle(screen, (0, 0, 0), (105, 610), 30)
#circle(screen, (0, 0, 0), (65, 600), 20)
#circle(screen, (0, 0, 0), (37, 590), 10)

#circle(screen, (225, 225, 225), (85, 585), 5)
#circle(screen, (225, 225, 225, 128), (50, 583), 5)
#circle(screen, (225, 225, 225), (27, 585), 2)

#circle(screen, (225, 225, 225), (69, 535), 20)
#circle(screen, (225, 225, 225), (49, 540), 2)

#circle(screen, (0, 191, 225), (65, 535), 5)
#circle(screen, (0, 191, 225), (80, 535), 5)
#circle(screen, (0, 0, 0), (67, 535), 2)
#circle(screen, (0, 0, 0), (82, 535), 2)
#line(screen, (225, 225, 225), (60, 534), (65, 535), 2)
#line(screen, (225, 225, 225), (75, 534), (80, 535), 2)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()