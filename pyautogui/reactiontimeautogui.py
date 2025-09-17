import time
import pyautogui
import keyboard as k
import sys

from pynput.mouse import Controller, Button
order = []
mouse = Controller()
lastLocation = None
#remember is a function to go through the box positions and click them
def remember():
    for l in order:
        pyautogui.click(l)
        time.sleep(0.1)
    order.clear()
    
#startButton for memory sequence game
startButton = pyautogui.locateCenterOnScreen('pyautogui/startbuttonmem.png', confidence=0.7, grayscale=True, region=(384,253,494,417))
pyautogui.click(startButton)
while True:
        #failsafe
        if k.is_pressed('q'):
             sys.exit()
       #pyautogui.mouseInfo()
        #reaction time game
        '''
        if pyautogui.pixelMatchesColor(829,204, (75,219,106)):
            pyautogui.click(829,204)

            #target game
        try:
            location = pyautogui.locateCenterOnScreen('pyautogui/target.png', confidence=0.5, grayscale=True)
            
            mouse.position = (location)
            mouse.press(Button.left)
        except:
             pass
              '''
        #sequence game

        #find the location then wait for 0.15 seconds b/c once clicked the square will flash white making them add to order again

        try:
            location = pyautogui.locateCenterOnScreen('pyautogui/whitesquare.png', grayscale=True, region=(384,253,494,417))
            
            time.sleep(0.15)
        
            #helps make sure that locations dont get added twice only adds if the list is empty or the location isnt the previous
            if location is None or location != lastLocation:
               pyautogui.moveTo(location)
               order.append(mouse.position)
               print(order)
               time.sleep(0.2)  
               lastLocation = location
            else:
                 lastLocation = None
           # mouse.press(Button.left)
        except:
              pass
        if k.is_pressed('r'):
            remember()
       