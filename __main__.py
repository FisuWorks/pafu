
import sys
import pygame.freetype
from pygame import Surface
from pygame.freetype import Font
from pygame.locals import *

import tween

pygame.init()
DISPLAY_SURF: Surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Best game")

FPS = 60
clock = pygame.time.Clock()

text: Font = Font("assets/fonts/Chunkfive/Chunkfive.otf", 32)
textSurface, textRect = text.render("Hello there", Color(120, 0, 120))
textRect.center = (100, 100)

tw = tween.Tween(textRect, 800)
tw.set_attr("centery", 100, 200)
tw.set_attr("centerx", 100, 200)
tw.set_pingpong()
tw.start()

while True:
    delta = clock.tick_busy_loop(FPS)
    tw.update(delta)
    DISPLAY_SURF.fill(WHITE)
    DISPLAY_SURF.blit(textSurface, textRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
