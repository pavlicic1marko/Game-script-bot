import os
import re
import sys
import time
import PIL
import easyocr
import numpy
import numpy as np
import pyautogui
from Commands.click_on_image import click_on_image, region

threshold_minutes = 6

image_folder_full_screen="images\\full_screen\\"
image_folder_maximize="images\\maximise_screen\\"

reader = easyocr.Reader(['en'])

def time_to_minutes(time_str):
    hours, minutes, _ = map(int, time_str.split('.'))
    return hours * 60 + minutes

def text_sanitization(time_str):
    print("timme:" + time_str)

    if not time_str:
        return ''
    if time_str[:3].isdigit():
        time_str = time_str[1:]  # Remove extra leading digit
    parts = time_str.split(':')
    if len(parts[2]) > 2:
        parts[2] = parts[2][:2]  # Remove extra trailing digit
    return ':'.join(parts)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def remove_stale_user(role_image):
    click_on_image(role_image)
    image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize + 'time_in_office_text.png'),
    region=region, confidence=0.8, grayscale=True)
    print(image_cordinates)

    region2 = (int(image_cordinates.left)+image_cordinates.width, int(image_cordinates.top), image_cordinates.width, image_cordinates.height)

    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region2)
    # read text from immage

    time_on_screen = reader.readtext(np.array(screenshot))[0][1]
    time_on_screen = time_on_screen.replace(":",".")
    time_on_screen = time_on_screen.replace(",",".")
    time_on_screen = time_on_screen.replace(";",".")
    time_on_screen = time_on_screen.replace("'",".")




    # save screenshot for debugging purpose
    screenshot.save( " screenshot.png")






    print(time_on_screen)
    if not time_on_screen:
        print("the bot did not find the time")

    else:
        minutes = time_to_minutes(time_on_screen)
        print("the number of minutes is: " + str(minutes))

        if minutes > threshold_minutes:
            print("time is more than 6 minutes")
        else:
            print("time is less than 6 minutes")
        click_on_image('close.PNG')



if __name__ == "__main__":
    while True:
        remove_stale_user('secretary_of_strategy.png')
        remove_stale_user('secretary_of_security.png')
        remove_stale_user('secretary_of_development.png')
        remove_stale_user('secretary_of_science.png')
        remove_stale_user('secretary_of_interior.png')
        time.sleep(5)

