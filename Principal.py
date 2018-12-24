import sys
import os
import pyautogui
import time

//pyautogui.FAILSAFE = False
os.startfile('"C:\Program Files\CCleaner\CCleaner64.exe"')

#x, y = pyautogui.position()
#print("Posição atual do mouse")
#print ("x = "+str(x)+" y = "+str(y))

#print ("")

#pyautogui.moveTo(827, 673)

time.sleep(5)
pyautogui.click(x=895, y=672)
time.sleep(5)
pyautogui.click(x=827, y=673)

#895 672
##1095 585