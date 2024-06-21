import pygame
from pygame.locals import*

pygame.init()
pygame.font.init()

display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("My First Game")

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT or (
                event.type == KEYDOWN and (
                event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()
    pygame.display.update()
