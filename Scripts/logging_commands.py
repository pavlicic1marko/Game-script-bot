import os
import sys
import logging

import pyautogui

logger = logging.getLogger(__name__)
log_to_file = False  # if False print on screen


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2  # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


logging.basicConfig(filename=resource_path('logs\\myapp.log'), level=logging.INFO)


def log_info(message: str):
    if log_to_file:
        logger.info(message)
    else:
        print(message)


def log_screen_shoot(screen_shot_name):
    pyautogui.screenshot(resource_path('logs\\' + screen_shot_name + '.png'))
