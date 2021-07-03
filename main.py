from PIL import ImageGrab
import cv2
import numpy as np
from playsound import playsound
from time import sleep

print("\n\n")

template = cv2.imread('./screens/req.png', 0)
 
while 1:
 
    base_screen = ImageGrab.grab(bbox=(1700, 820, 1880, 980))
    base_screen.save('./screens/base_screen.png')
 
    img_rgb = cv2.imread('./screens/base_screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
 
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.8)
 
    if loc[0] != []:
        playsound('notify.mp3')
        t = 60
        print("6/6!")
    else:
        print("Не 6/6")
        t = 5
 
    sleep(t)