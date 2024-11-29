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
    hours, minutes, _ = map(int, time_str.split(':'))
    return hours * 60 + minutes


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
    time.sleep(1)
    image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize + 'time_in_office_text.png'),
    region=region, confidence=0.7, grayscale=True)
    print(image_cordinates)

    region2 = (int(image_cordinates.left)+image_cordinates.width, int(image_cordinates.top), image_cordinates.width, image_cordinates.height)

    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region2)
    # read text from immage
    try:
        time_on_screen = reader.readtext(np.array(screenshot))[0][1]
    except IndexError:
        click_on_image('close.PNG')


    time_on_screen = time_on_screen.replace(".",":")
    time_on_screen = time_on_screen.replace(",",":")
    time_on_screen = time_on_screen.replace(";",":")
    time_on_screen = time_on_screen.replace("'",":")
    pattern = r'\b\d{2}:\d{2}:\d{2}\b'
    matches = re.findall(pattern, time_on_screen)

    # save screenshot for debugging purpose
    screenshot.save( " screenshot.png")






    print(matches)
    if  matches:
        minutes = time_to_minutes(time_on_screen)
        print("the number of minutes is: " + str(minutes))

        if minutes > threshold_minutes:
            print("time is more than 6 minutes")
        else:
            print("time is less than 6 minutes")
        click_on_image('close.PNG')

    else:
        print("the bot did not find the time")
        click_on_image('close.PNG')






if __name__ == "__main__":
    i=1
    while True:
        i+=1
        remove_stale_user('secretary_of_strategy.png')
        remove_stale_user('secretary_of_security.png')
        remove_stale_user('secretary_of_development.png')
        remove_stale_user('secretary_of_science.png')
        remove_stale_user('secretary_of_interior.png')
        print(i)
        time.sleep(5)

