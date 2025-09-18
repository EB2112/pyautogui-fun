import pytesseract
import pyautogui
import keyboard
import cv2
import numpy as np
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#enb\Projects\python\mouselnfoScreensh pyautogui.mouseInfo()


region = (28,562, 797, 187 )
#region for https://humanbenchmark.com/tests/typing
#region = (153,393, 981, 181 )
screenshot = pyautogui.screenshot(region=region)
screenshot.save('form_filled.png')
time.sleep(3)
# Convert the screenshot to a numpy array
screenshot_np = np.array(screenshot)
# Convert to grayscale
gray_screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
#Extract text
text = pytesseract.image_to_string(gray_screenshot)
text.split(" ")
print("Detected text:")
print(text.replace('\n', " ").replace('[|'," "))
print(text.split(" "))

for word in text.replace("\n", " ").replace('[|',"").split(" "):
    if word == "|":
        pyautogui.typewrite("I ")
    else:
        pyautogui.typewrite(word + " ")
        time.sleep(0.1)
