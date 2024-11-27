import pyautogui

from Commands.click_on_image import click_on_image, click_on_image_if_visible


def approve_all_5_roles():
    approve_role('secretary_of_strategy.PNG')
    approve_role('secretary_of_security.PNG')
    approve_role('secretary_of_development.PNG')
    approve_role('secretary_of_science.PNG')
    approve_role('secretary_of_interior.PNG')


def approve_role(role_name):
    click_on_image('images\\' + role_name)
    click_on_image('images\\list_button.PNG')
    click_on_image_if_visible('images\\Approve_from_list_button.PNG')
    click_on_image('images\\close.PNG')
    pyautogui.moveTo(400, 400)
    click_on_image('images\\close.PNG')


if __name__ == "__main__":
    while True:
        approve_all_5_roles()