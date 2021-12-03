#curPos
#Filip Rokita
#www.filiprokita.com

import pyautogui
import keyboard
import time

key = input("KEY: ").lower()

while True:
    if keyboard.is_pressed(key):
        print(tuple(pyautogui.position()))
        time.sleep(0.5)