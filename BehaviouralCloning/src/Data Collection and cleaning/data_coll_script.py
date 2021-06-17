import time
import pyautogui
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image
import pygame
import h5py

pygame.init()
pygame.joystick.init()
stick = pygame.joystick.Joystick(0)


print(pygame.joystick.get_count())

fps = 20
time.sleep(5)
capture = 5000

print('\a')

ls = []
images = []

for i in range(capture):
    start = time.time()

    pygame.joystick.Joystick(0).init()
    pygame.event.pump()
    stick.init()

    screen = pyautogui.screenshot(region=(400, 475, 1920 - 400, 1080 - 800))

    
    axis_0 = round(pygame.joystick.Joystick(0).get_axis(0), 4)
    axis_5 = round(pygame.joystick.Joystick(0).get_axis(5), 4)
    axis_4 = round(pygame.joystick.Joystick(0).get_axis(4), 4)
    
    ls.append((axis_0, axis_5, axis_4))
    images.append(screen)

    time.sleep(max(1./fps - (time.time() - start), 0))


    
def process(img):
    img = np.array(img)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.resize(img, (400, 250))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img,125,200)
    return img    
    
img = list(map(process, images))

data = []
for i in range(capture):
    data.append((img[i], ls[i][0], ls[i][1], ls[i][2]))
    
df = pd.DataFrame(data, columns=['images', 'steering_anle', 'throttle', "brakes"])

df.to_hdf("data.h5", "df")

print('\a')
