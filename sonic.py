import pygame

class Sonic:
    spreadsheet = ""

    def __init__(self, spreadsheet):
        self.spreadsheet = spreadsheet

    def drawIdleSprite(self, i, window):
        size = 90

        x = (i % 16) * size + 32 * (round(i / 16) + 1)
        y = round(i / 16) * size * 1.5 + 64

        rect = pygame.Rect((x,y), (size,size * 1.5))

        window.blit(self.spreadsheet, (100,100), rect)

    def drawSonicSprite(self, i, window):
        if i < 19:
            self.drawIdleSprite(i, window)
