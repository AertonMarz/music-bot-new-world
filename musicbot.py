
import pyautogui
import time
from pynput.keyboard import Controller

print('Start')
keyb = Controller()
time.sleep(3)
keyb.press('e')
keyb.release('e')

while True:
    x = 0
    while x != 350:
        x +=1
        if pyautogui.pixel(626, 799) == (255, 255, 255) or pyautogui.pixel(623, 799) == (214, 203, 173):
            pyautogui.typewrite('w')
        
        elif pyautogui.pixel(626, 832) == (0, 0, 0) or pyautogui.pixel(623, 832) == (214, 203, 173):
            pyautogui.typewrite('a')
        
        elif pyautogui.pixel(626, 862) == (0, 0, 0) or pyautogui.pixel(623, 862) == (214, 203, 173):
            pyautogui.typewrite('s')

        elif pyautogui.pixel(626, 895) == (0, 0, 0) or pyautogui.pixel(623, 895) == (214, 203, 173):
            pyautogui.typewrite('d')

        elif pyautogui.pixel(626, 923) == (0, 0, 0) or pyautogui.pixel(623, 923) == (214, 203, 173):
            pyautogui.press('space')

    keyb.press('e')
    time.sleep(3)
    keyb.release('e')
    time.sleep(2)
    pyautogui.press('e')
    x = 0
            