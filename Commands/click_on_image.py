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
        base_path = sys._MEIPASS2  # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


image_folder_full_screen = "images\\full_screen\\"
image_folder_maximize = "images\\maximise_screen\\"


def click_on_image_if_visible(image_name, comment_if_image_not_visible):
    confidence = 0.8
    try:
        try_to_click_on_immage_and_on_smaller_resolution(image_name,confidence)
    except pyautogui.ImageNotFoundException:
        logging_commands.log_info(comment_if_image_not_visible)



def try_to_click_on_immage_and_on_smaller_resolution(image_name, confidence: [int, float]):
    try:
        image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_full_screen + image_name),
                                                    region=region, confidence=confidence, grayscale=True)
        x, y = pyautogui.center(image_cordinates)
        click_with_random_sleep_and_cordinate_variation([x, y])
    except pyautogui.ImageNotFoundException:
        logging_commands.log_info('try with different resolution')
        image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize + image_name),
                                                    region=region, confidence=confidence, grayscale=True)
        x, y = pyautogui.center(image_cordinates)
        click_with_random_sleep_and_cordinate_variation([x, y])


def click_on_exact_image(image_name):
    confidence = 1
    try_to_click_on_immage_and_on_smaller_resolution(image_name, confidence)


def click_on_image_with_Very_high_confidence(image_name):
    confidence = 0.95
    try_to_click_on_immage_and_on_smaller_resolution(image_name, confidence)


def click_on_image_with_high_confidence(image_name):
    confidence = 0.90
    try_to_click_on_immage_and_on_smaller_resolution(image_name, confidence)


def click_on_image_with_confidence(image_name):
    confidence = 0.85
    try_to_click_on_immage_and_on_smaller_resolution(image_name, confidence)


def click_on_image_with_low_confidence(image_name):
    confidence = 0.80
    try_to_click_on_immage_and_on_smaller_resolution(image_name, confidence)


def click_on_image_with_very_low_confidence(image_name):
    confidence = 0.85
    try_to_click_on_immage_and_on_smaller_resolution(image_name, confidence)


def click_on_image_with_extreme_low_confidence(image_name):
    confidence = 0.75
    try_to_click_on_immage_and_on_smaller_resolution(image_name, confidence)


def find_image_on_screen(image_name, confidence):
    try:
        image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_full_screen + image_name),
                                                    region=region, confidence=confidence, grayscale=True)

        return image_cordinates

    except pyautogui.ImageNotFoundException:
        image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize + image_name),
                                                    region=region, confidence=confidence, grayscale=True)

        return image_cordinates
