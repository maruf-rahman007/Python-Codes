import pyautogui

numOFline = int(input())
line_length = 1

for i in range(numOFline):
    line = "#" * line_length
    pyautogui.typewrite(line + "\n", interval=0.1)
    line_length += 1