import pyautogui
from time import *

sleep(7)

for i in range(0,100):
    pyautogui.write('Hey Mohosin Bhai!', interval=0.25)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.write('How are you?', interval=0.25)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.write("i'm fine thank you ! what about you?", interval=0.25)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.write("That's nice to hear! Ok bye see You ", interval=0.25) 
    pyautogui.press('enter')
