import os
import sys
import time
import pyautogui
from Commands.click_on_image import click_on_image_with_Very_high_confidence, click_on_image_if_visible
from Scripts import logging_commands
from Scripts.logging_commands import log_screen_shoot


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



def approve_all_5_roles():
    logging_commands.log_info('Started role approval for all 5 users')
    approve_role('secretary_of_strategy.png')
    approve_role('secretary_of_security.png')
    approve_role('secretary_of_development.png')
    approve_role('secretary_of_science.png')
    approve_role('secretary_of_interior.png')
    time.sleep(5)


def approve_role(role_name):
    click_on_image_with_Very_high_confidence(role_name)
    click_on_image_with_Very_high_confidence('list_button.png')
    click_on_image_if_visible('Approve_from_list_button.png','no one to approve')
    click_on_image_with_Very_high_confidence('close.PNG')
    pyautogui.moveTo(400, 400)
    click_on_image_with_Very_high_confidence('close.png')


if __name__ == "__main__":
    i = 0
    while True:
        approve_all_5_roles()
        i +=1
        logging_commands.log_info('loop number: ' + str(i))

log_screen_shoot('last_screenshot')