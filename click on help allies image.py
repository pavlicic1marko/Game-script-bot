import time
import pyautogui

#game screen region
top = 0
left = 655
height = 1079
wight = 609
region = (left, top, wight, height)

startButton = pyautogui.locateOnScreen('C:/Users/MP/PycharmProjects/LastWarautomation/hellp_allies_button.png', region=region, confidence=0.8, grayscale = True)
print(startButton)
pyautogui.click(startButton)
#time.sleep(0.2)
#pyautogui.click(startButton)
