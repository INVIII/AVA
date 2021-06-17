import time

import pygame

pygame.init()
pygame.joystick.init()

stick = pygame.joystick.Joystick(0)


while True:
    time.sleep(2)
    pygame.event.pump()
    stick.init()
    axis_0 = stick.get_axis(0)
    axis_1 = stick.get_axis(4)
    axis_2 = stick.get_axis(2)
    axis_3 = stick.get_axis(5)



    print(f"{axis_0} {axis_1} {axis_2} {axis_3} ")

