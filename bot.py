import pyautogui
from datetime import datetime
from os import system, name


print('Qual horario você quer bater o print? ex: 22:30')
printTime = str(input())
now = datetime.now()

current_time = now.strftime("%H:%M")
print(current_time )

while (current_time != printTime ):
    print(current_time)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    system('cls')

capturar = pyautogui.screenshot()
capturar.save( printTime +'.png')
print('ótima aula')
