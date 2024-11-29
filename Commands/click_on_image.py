from Commands.Click import *
from Scripts import logging_commands
import os
import sys

top = 0
left = 655
height = 1079
wight = 609
region = (left, top, wight, height)  # game screen dimensions

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

image_folder_full_screen="images\\full_screen\\"
image_folder_maximize="images\\maximise_screen\\"

def click_on_image(image_name):
    try:
        image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_full_screen +  image_name),
        region=region, confidence=0.95, grayscale=True)
        x,y = pyautogui.center(image_cordinates)
        click_with_random_sleep_and_cordinate_variation([x,y])
    except pyautogui.ImageNotFoundException:
        logging_commands.log_info('try with different resolution')
        image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize +  image_name),
        region=region, confidence=0.90, grayscale=True)
        x,y = pyautogui.center(image_cordinates)
        click_with_random_sleep_and_cordinate_variation([x,y])


def click_on_exact_image(image_name):
    image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize + image_name) ,
    region=region, confidence=1, grayscale=True)
    click_with_random_sleep(image_cordinates)

def click_on_image_if_visible(image_name):
    try:
        image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize +  image_name),
        region=region, confidence=0.8, grayscale=True)
        x, y = pyautogui.center(image_cordinates)
        click_with_random_sleep_and_cordinate_variation([x, y])
    except pyautogui.ImageNotFoundException:
        logging_commands.log_info('no one to approve')


