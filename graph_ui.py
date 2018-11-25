import pygame
import sys
import operations

pygame.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
blue = (0,0,255)

def graph_ui(button, screen, parameter):

    #parameter = thumb_fsr, index_fsr, middle_fsr, index_bend, middle_bend

    global white
    global black
    global red
    global blue

    start_pos = [55,450]
    end_pos = [550,450]
    text_pos = (35, 545)
    thumb_pos = (100,450)
    index_pos = (280,450)
    middle_pos = (450,450)

    thumb_fsr_pos = (115,450-parameter[0],30,parameter[0])
    index_fsr_pos = (270,450-parameter[1],30,parameter[1])
    middle_fsr_pos = (450,450-parameter[2],30,parameter[2])

    index_bend_pos = (300,450-parameter[3],30,parameter[3])
    middle_bend_pos = (480,450-parameter[4],30,parameter[4])

    thumb_fsr = pygame.Rect(thumb_fsr_pos)
    index_fsr = pygame.Rect(index_fsr_pos)
    middle_fsr = pygame.Rect(middle_fsr_pos)

    index_bend = pygame.Rect(index_bend_pos)
    middle_bend = pygame.Rect(middle_bend_pos)

    font = pygame.font.SysFont("Arial", 23)
    text = font.render("switch screen", True, black)
    thumb = font.render("Thumb", True, black)
    index = font.render("Index ", True, black)
    middle = font.render("Middle", True, black)

    screen.fill(white)
    pygame.draw.line(screen,black,start_pos,end_pos,1)
    pygame.draw.rect(screen, black, button, 2)
    pygame.draw.rect(screen, red, thumb_fsr)
    pygame.draw.rect(screen, red, index_fsr)
    pygame.draw.rect(screen, red, middle_fsr)
    pygame.draw.rect(screen, blue, index_bend)
    pygame.draw.rect(screen, blue, middle_bend)

    screen.blit(text,text_pos)
    screen.blit(thumb,thumb_pos)
    screen.blit(index, index_pos)
    screen.blit(middle, middle_pos)

    pygame.display.flip()