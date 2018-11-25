from hand_ui import *
from graph_ui import *
import operations
import sys
import serial

screen_state = "hand"
screen_size = (600, 600)
white = (255, 255, 255)
black = (0, 0, 0)

button_pos = (30, 530, 120, 60)
exit_pos = (530,30,120,60)

button = pygame.Rect(button_pos)
exit_button = pygame.Rect(exit_pos)

screen = pygame.display.set_mode(screen_size)

ser = serial.Serial('/dev/ttyACM0',9600,8,'N',1,timeout=5)

while ser.readline():

    parameter = ser.readline().decode('utf-8')

    if screen_state == "hand":
        hand_ui(button, screen, parameter)
        if operations.mouse_click(button):
            screen_state = "graph"
        if operations.mouse_click(exit_button):
            sys.exit()
    elif screen_state == "graph":
        graph_ui(button, screen, parameter)
        if operations.mouse_click(button):
            screen_state = "hand"
        if operations.mouse_click(exit):
            sys.exit()

    else:
        sys.exit()