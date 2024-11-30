import os
import random
import re
import sys
import time
import easyocr
import numpy as np
import pyautogui
from Commands.click_on_image import click_on_image_with_Very_high_confidence, region, click_on_image_if_visible, \
    find_image_on_screen, try_find_image_on_screen
from Scripts.go_to_screen import try_to_go_to_3_main_screens
from Scripts.logging_commands import log_info

threshold_minutes = 6

image_folder_full_screen = "images\\full_screen\\"
image_folder_maximize = "images\\maximise_screen\\"

reader = easyocr.Reader(['en'])


def time_to_minutes(time_str):
    hours, minutes, _ = map(int, time_str.split(':'))
    return hours * 60 + minutes


def clean_up_ocr_text(time_on_screen):
    time_on_screen = time_on_screen.replace(".", ":")
    time_on_screen = time_on_screen.replace(",", ":")
    time_on_screen = time_on_screen.replace(";", ":")
    time_on_screen = time_on_screen.replace("'", ":")

    return time_on_screen


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2  # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def is_role_vacant():
    return try_find_image_on_screen('vacant.png', 0.8)


def is_time_valid(time_string):
    if any(char not in '0123456789:' for char in time_string):
        return False
    else:
        return True


print(is_time_valid('123,123'))


def remove_stale_user(role_image):
    click_on_image_with_Very_high_confidence(role_image)
    time.sleep(1)
    pyautogui.screenshot('time_in_role_screenshot.png')

    # find location of the image on screen
    # image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_full_screen + 'time_in_office_text.png'),
    # region=region, confidence=0.8, grayscale=True)
    if is_role_vacant():
        log_info('role is vacant')
        matches = ''
    else:
        image_cordinates = find_image_on_screen('time_in_office_text.png', 0.8)
        # region 2 is the image of the time user is in a role, next to the image time_in_office_text.png
        region2 = (
            int(image_cordinates.left) + image_cordinates.width, int(image_cordinates.top), image_cordinates.width,
            image_cordinates.height)

        # Capture the screen region
        screenshot = pyautogui.screenshot(region=region2)

        try:
            # read text from immage using easyocr
            time_on_screen = reader.readtext(np.array(screenshot))[0][1]
        except IndexError:
            # if unable to find time close pop-up in next step, if matches will evaluate to false
            time_on_screen = ""

        #  easy ocr  can make a mistake with ':' character
        time_on_screen = clean_up_ocr_text(time_on_screen)

        # test if the paatern is found
        # check if time is valid
        if (is_time_valid(time_on_screen)):
            print('time is valid')
        else:
            time_on_screen = ''

    # test if the paatern is found
    pattern = r'\b\d{2}:\d{2}:\d{2}\b'
    matches = re.findall(pattern, time_on_screen)

    if time_on_screen and matches:
        minutes = time_to_minutes(time_on_screen)
        print("the number of minutes is: " + str(minutes))

        if minutes > threshold_minutes:
            print("time is more than 6 minutes")
            #  click on dismiss
            #  click on confirm
            #  click on close
            #  click on close
            time.sleep(1)

        else:
            print("time is less than 6 minutes")
        click_on_image_with_Very_high_confidence('close.PNG')

    else:
        print("the bot did not find the time")
        click_on_image_with_Very_high_confidence('close.PNG')


if __name__ == "__main__":
    i = 0
    number_of_exceptions = 0
    while True:
        try:
            i += 1
            remove_stale_user('secretary_of_strategy.png')
            remove_stale_user('secretary_of_security.png')
            remove_stale_user('secretary_of_development.png')
            remove_stale_user('secretary_of_science.png')
            remove_stale_user('secretary_of_interior.png')
            print(i)
            time.sleep(5)
        except pyautogui.ImageNotFoundException:
            pyautogui.screenshot('first_screenshot.png')

            number_of_exceptions += 1
            print("there was an exception trying to go back to server screen, the exception number is: ",
                  number_of_exceptions)
            # go_back_to_server_screen()
            pyautogui.screenshot(str(number_of_exceptions) + 'screenshot.png')

            try_to_go_to_3_main_screens()

            if number_of_exceptions > 3:
                break

pyautogui.screenshot('last_screenshot.png')
