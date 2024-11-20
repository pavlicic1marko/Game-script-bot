import time
from random import randint
import pyautogui

# open and close profile page in LastWar game
# Randomize time delay
# Randomize click pixel offset

# Variables
default_sleep_time = 0.8  # in seconds
random_sleep_time_mix = 10  # in ms
random_sleep_time_max = 1000  # in ms
pixel_click_range_positive = 2  # pixels
pixel_click_range_negative = -2  # pixels


def click_with_random_sleep_and_cordinate_variation(ui_location):
    """click on a coordinate
    with a random time delay and a variation of a few pixels
    """
    ui_location[0] += randint(pixel_click_range_negative, pixel_click_range_positive)
    ui_location[1] += randint(pixel_click_range_negative, pixel_click_range_positive)
    pyautogui.click(tuple(ui_location))
    time.sleep(default_sleep_time + randint(random_sleep_time_mix, random_sleep_time_max) / 1000)


def click_with_random_sleep(ui_location):
    """click on a coordinate
    with a random time sleep
    """
    pyautogui.click(ui_location)
    time.sleep(default_sleep_time + randint(random_sleep_time_mix, random_sleep_time_max) / 1000)
