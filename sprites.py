import pygame
from pygame import Rect, Surface

class Spritesheet:

    def __init__(self, imagepath: str):
        self.baseimage: Surface = pygame.image.load(imagepath).convert()

    def image_at(self, rect: Rect, colorkey: pygame.Color=None):
        subimage: Surface = Surface((rect.width, rect.height))
        subimage.blit(self.baseimage, (0, 0), rect)
        if colorkey is not None:
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        return subimage
