import pyautogui
import time
import keyboard as k
from pynput.mouse import Button, Controller
import cv2
import sys
import threading

pyautogui.PAUSE = 0.01

mouse = Controller()
width, height = pyautogui.size()
print(width, height)
print(pyautogui.FAILSAFE)

"""
#lil script for piano tiles from this website https://lagged.com/en/g/piano-tiles-3
#clicks start then waits a second
pyautogui.click(420, 500) 
time.sleep(1)
##
while True:
        if k.is_pressed('q'):
             sys.exit()
        #couldnt use the pyautogui click, think the website had a defense against it 
        #used pynput which is lower level, does the trick
        #basically just clicks if the tiles appear, meant to be used while in a side window
        if pyautogui.pixelMatchesColor(329, 650, (17,40,81), tolerance=20):
            print("1")
            mouse.position = (329, 650)
            mouse.press(Button.left)
        if pyautogui.pixelMatchesColor(420, 650,(17,40,81) , tolerance=20):
            print("2")
            mouse.position = (420, 650)
            mouse.press(Button.left)
        if pyautogui.pixelMatchesColor(533, 650, (17,40,81), tolerance=20):
            print("3")
            mouse.position = (533, 650)
            mouse.press(Button.left)
        if pyautogui.pixelMatchesColor(621, 650, (17,40,81), tolerance=20):
            print("4")
            mouse.position = (621, 650)
            mouse.press(Button.left)
"""

startX =1010
startY=850
timer = 10000
upgrades = 5
pyautogui.useImageNotFoundException()
imagePath='goldencookie.png'

def goldenCookieClick():
    goldenCookiesClicked = 0
    while True:
        try:  
            
            location = pyautogui.locateCenterOnScreen(imagePath, confidence=0.5)  # adjust confidence
            if location:
                goldenCookiesClicked+=1
                print(goldenCookiesClicked)
                pyautogui.click(location)
                
        except pyautogui.ImageNotFoundException:
             pass
        time.sleep(0.1)

threading.Thread(target=goldenCookieClick, daemon=True).start()
while True:
        if k.is_pressed('q'):
             sys.exit()
        #pyautogui.mouseInfo()
        timer-=1
        if timer == 0:
            for x in range(upgrades):
             pyautogui.click(startX, startY)
             startY -= 60
            timer = 10000
            startY = 850
        
        
            
        if pyautogui.pixelMatchesColor(991,216,(7,21,30),tolerance=10):
            pyautogui.click(983,235)
        else:
            pyautogui.click(196,661)
            