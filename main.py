import pygame
from pygame.locals import *
import random
import sonic

pygame.init()

def load_img(name):
    return pygame.image.load("./assets/"+name+".png").convert_alpha()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Le reve de Robotnik")

background = load_img("background")
ground = load_img("ground")

tree1 = load_img("tree1")
tree2 = load_img("tree2")
sunflower = load_img("sunflower")
totem = load_img("totem")

sonic = sonic.Sonic(load_img("sonic"))

i = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            i += 1

    window.blit(background, (0,0))

    window.blit(tree1, (32, 140))
    window.blit(tree1, (149, 125))

    window.blit(tree2, (485, 100))

    window.blit(sunflower, (349, 260))
    window.blit(sunflower, (224, 260))

    sonic.drawSonicSprite(i, window)

    window.blit(ground, (0, 380))

    pygame.display.flip()
