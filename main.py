import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("Le reve de Robotnik")

background = pygame.image.load("./assets/background.png").convert()

running = True
while running:
    for event in pygame.event.get():
            if event.type == QUIT:
                running = False

    window.blit(background, (0,0))
    pygame.display.flip()
