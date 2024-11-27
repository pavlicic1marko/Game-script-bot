import pyautogui

from Commands.click_on_image import click_on_image, resource_path, image_folder_maximize


def remove_stale_user():
    click_on_image('secretary_of_strategy.png')
    image_cordinates = pyautogui.locateOnScreen(resource_path(image_folder_maximize + 'time_in_office_text.png'))
    print(image_cordinates)


if __name__ == "__main__":
    remove_stale_user()