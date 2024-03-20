import pygame
from pygame.draw import *

def lghost_make(x, y, s):
    #основа
    polygon(screen, (225, 225, 225, 128), ((400 - x, y), (400 - (x + s * 20), y - s * 45), (400 - (x + s * 55), y - s * 45), (400 -(x + s * 55), y - s * 40), (400 -(x + s * 100), y + s * 5)))
    #формирование
    circle(screen, (0, 0, 0), (400 - (x + s * 80), y + s * 25), s * 30)
    circle(screen, (0, 0, 0), (400 - (x + s * 40), y + s * 15), s * 20)
    circle(screen, (0, 0, 0), (400 - (x + s * 12), y + s * 5), s * 10)
    #скругление
    circle(screen, (225, 225, 225), (400 - (x + s * 60), s * y), s * 5)
    circle(screen, (225, 225, 225), (400 - (x + s * 25), y - s * 2), s * 5)
    circle(screen, (225, 225, 225), (400 - (x + s * 2), s * y), s * 2)
    circle(screen, (225, 225, 225), (400 - (x + s * 24), y - s * 45), s * 2)
    #голова
    circle(screen, (225, 225, 225), (400 - (x + s * 44), y - s * 50), s * 20)
    #глазные яблоки
    circle(screen, (0, 191, 225), (400 - (x + s * 40), y - s * 50), s * 5)
    circle(screen, (0, 191, 225), (400 - (x + s * 55), y - s * 50), s * 5)
    #зрачки
    circle(screen, (0, 0, 0), (400 - (x + s * 42), y - s * 50), s * 2)
    circle(screen, (0, 0, 0), (400 - (x + s * 57), y - s * 50), s * 2)
    #блики
    line(screen, (225, 225, 225), (400 - (x + s * 35), y - s * 51), (400 - (x + s * 40), y - s * 50), s)
    line(screen, (225, 225, 225), (400 - (x + s * 50), y - s * 51), (400 - (x + s * 55), y - s * 50), s)


pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (85, 85, 85), (0, 0, 400, 160))
circle(screen, (225, 225, 225), (360, 35), 35)
ellipse(screen, (17, 17, 17), (200, 95, 230, 25))
rect(screen, (52, 59, 41), (25, 90, 205, 220))
rect(screen, (76, 47, 39), (25, 90, 205, 70))
ellipse(screen, (68, 68, 68), (222, 68, 356, 20))
polygon(screen, (0, 0, 0), ((0, 95), (40, 73), (215, 73), (255, 95)))
rect(screen, (34, 34, 34), (150, 50, 5, 23))
rect(screen, (34, 34, 34), (55, 45, 7, 39))
ellipse(screen, (15, 15, 15), (20, 40, 310, 28))
rect(screen, (34, 34, 34), (66, 40, 14, 44))
rect(screen, (34, 34, 34), (194, 50, 7, 34))
ellipse(screen, (68, 68, 68), (178, 20, 230, 25))
rect(screen, (151,123,128), (40, 95, 20, 63))
rect(screen, (151,123,128), (80, 95, 20, 63))
rect(screen, (151,123,128), (130, 95, 20, 63))
rect(screen, (151,123,128), (170, 95, 20, 63))
rect(screen, (77, 34, 14), (40, 245, 50, 40))
rect(screen, (77, 34, 14), (105, 245, 50, 40))
rect(screen, (225, 255, 0), (170, 245, 50, 40))
rect(screen, (51, 51, 51), (0, 158, 255, 20))
rect(screen, (51, 51, 51), (20, 133, 215, 10))
rect(screen, (51, 51, 51), (10, 143, 10, 15))
rect(screen, (51, 51, 51), (235, 143, 10, 15))
rect(screen, (51, 51, 51), (50, 143, 10, 15))
rect(screen, (51, 51, 51), (90, 143, 10, 15))
rect(screen, (51, 51, 51), (130, 143, 10, 15))
rect(screen, (51, 51, 51), (170, 143, 10, 15))
rect(screen, (51, 51, 51), (210, 143, 10, 15))

lghost_make(25, 350, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
