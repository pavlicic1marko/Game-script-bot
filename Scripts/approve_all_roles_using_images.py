import os
import sys
import time
import pyautogui
from Commands.click_on_image import click_on_image_with_Very_high_confidence, click_on_image_if_visible
from Scripts import logging_commands
from Scripts.go_to_screen import try_to_go_to_3_main_screens, find_screen_name, go_to_base_screen_from_world_screen, \
    go_to_server_screen_from_base_screen
from Scripts.logging_commands import log_screen_shoot, log_info


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
    log_info('approve user with role: ' + role_name)
    click_on_image_with_Very_high_confidence(role_name)
    click_on_image_with_Very_high_confidence('list_button.png')
    click_on_image_if_visible('Approve_from_list_button.png','no one to approve')
    click_on_image_with_Very_high_confidence('close.PNG')
    pyautogui.moveTo(400, 400) # TODO add comment
    click_on_image_with_Very_high_confidence('close.png')


if __name__ == "__main__":
    i = 0
    number_of_exceptions = 0
    while True:
        try:
            approve_all_5_roles()
            i +=1
            log_info('loop number: ' + str(i))
        except pyautogui.ImageNotFoundException:
            log_screen_shoot('first_screenshot.png')

            try_to_go_to_3_main_screens()
            if find_screen_name() == 'world':
                go_to_base_screen_from_world_screen()
                go_to_server_screen_from_base_screen()
            if find_screen_name() == 'base':
                go_to_server_screen_from_base_screen()

            if number_of_exceptions > 100:
                break



log_screen_shoot('last_screenshot')