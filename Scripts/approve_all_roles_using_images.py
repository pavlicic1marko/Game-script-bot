import time
import pyautogui
from Commands.click_on_image import click_on_image, click_on_image_if_visible


def approve_all_5_roles():
    approve_role('secretary_of_strategy.png')
    approve_role('secretary_of_security.png')
    approve_role('secretary_of_development.png')
    approve_role('secretary_of_science.png')
    approve_role('secretary_of_interior.png')
    time.sleep(5)


def approve_role(role_name):
    click_on_image('images\\maximise_screen\\' + role_name)
    click_on_image('images\\maximise_screen\\list_button.png')
    click_on_image_if_visible('images\\maximise_screen\\Approve_from_list_button.png')
    click_on_image('images\\maximise_screen\\close.PNG')
    pyautogui.moveTo(400, 400)
    click_on_image('images\\maximise_screen\\close.png')


if __name__ == "__main__":
    i = 0
    while True:
        approve_all_5_roles()
        i +=1
        print(i)