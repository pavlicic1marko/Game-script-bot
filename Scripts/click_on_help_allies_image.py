import time
import pyautogui
from Commands.click_on_image import click_on_image
from images_location import get_image_folder_path


def help_allies():
    number_of_clicks = 0
    while True:
        try:
            click_on_image('images\\hellp_allies_button.png')
            number_of_clicks += 1
            print("clicked: " + str(number_of_clicks))
        except pyautogui.ImageNotFoundException:
            print("image not found")

        time.sleep(60)


if __name__ == "__main__":
    help_allies()
