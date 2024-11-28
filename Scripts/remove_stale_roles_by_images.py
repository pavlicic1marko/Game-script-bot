import os
import re
import sys

import PIL
import easyocr
import numpy
import numpy as np
import pyautogui

from Commands.click_on_image import click_on_image, region

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

def remove_stale_user():
    click_on_image('secretary_of_strategy.png')
    image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize + 'time_in_office_text.png'),
    region=region, confidence=0.8, grayscale=True)
    print(image_cordinates)

    region2 = (int(image_cordinates.left)+image_cordinates.width, int(image_cordinates.top), image_cordinates.width, image_cordinates.height)

    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region2)
    # read text from immage

    result = reader.readtext(np.array(screenshot))[0][1]

    # save screenshot for debugging purpose
    screenshot.save( " screenshot.png")

    # Use regular expression to find time strings in HH:mm:ss format
    #pattern = r'\b\d{2}.\d{2}.\d{2}\b'
    #matches = re.findall(pattern, result)





    threshold_minutes = 6
    print(result)
    if not result:

        print("the bot did not find the time")


    else:
        pass
        #i f time > 6
        minutes = time_to_minutes(result)
        print(minutes)



if __name__ == "__main__":
    remove_stale_user()