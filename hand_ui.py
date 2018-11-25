import pygame
import operations

pygame.init()
pygame.font.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
blue = (0,0,255)

def hand_ui(button, screen, parameter):

    # parameter = thumb_fsr, index_fsr, middle_fsr, index_bend, middle_bend
    #line thickness => min=0 max=30
    #circle radius => min=0 max=30

    global black,white,red,blue

    text_pos = (35, 545)

    thumb_fsr_pos = (90,300)
    index_fsr_pos = (210,80)
    middle_fsr_pos = (310,30)

    index_bend_start_pos = (210,80)
    index_bend_end_pos = (260,280)
    middle_bend_start_pos = (310,30)
    middle_bend_end_pos = (330,260)

    hand = pygame.image.load("hand.jpg")

    font = pygame.font.SysFont("Arial", 23)
    text = font.render("switch screen", True, black)

    screen.fill(white)
    screen.blit(hand,(0,0))

    pygame.draw.line(screen, blue, index_bend_start_pos, index_bend_end_pos, parameter[3])
    pygame.draw.line(screen, blue, middle_bend_start_pos, middle_bend_end_pos, parameter[4])

    pygame.draw.rect(screen, black, button, 2)  # text box
    pygame.draw.circle(screen, red, thumb_fsr_pos, parameter[0])
    pygame.draw.circle(screen, red, index_fsr_pos, parameter[1])
    pygame.draw.circle(screen, red, middle_fsr_pos, parameter[2])

    screen.blit(text, text_pos)

    pygame.display.flip()