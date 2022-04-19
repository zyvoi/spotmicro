import pygame
from pygame.locals import *
from sys import exit

pygame.init()

pygame.display.set_mode((640, 480))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    keys  = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    if ( keys[pygame.K_UP] ):
        print( "up, mouse@ "+str( mouse ), end="     \r" )
    else:
        print( "not up, mouse@ "+str( mouse ), end="     \r" )

    pygame.display.update()

