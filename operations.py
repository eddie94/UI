import pygame
import sys

pygame.init()
pygame.font.init()

def mouse_click(button):

    for event in pygame.event.get():

        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP and button.collidepoint(pos):
            return True
