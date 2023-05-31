import pyautogui
nl=int(input())
for num1 in range(0,nl):
   line=""
   for num2 in range(0,num1+1):
       line+="#"
   pyautogui.typewrite(line)
   pyautogui.typewrite("\n")
