import os
import sys
import time
import pyautogui
from Commands.click_on_image import click_on_image
from Scripts import logging_commands


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



def help_allies():
    number_of_clicks = 0
    while True:
        try:
            logging_commands.log_info('Started help_allies script')
            click_on_image('help_allies_button.png')
            number_of_clicks += 1
            print("clicked: " + str(number_of_clicks))
        except pyautogui.ImageNotFoundException:
            print("image not found")

        time.sleep(60)


if __name__ == "__main__":
    help_allies()
