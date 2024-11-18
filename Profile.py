import time
from random import randint
import pyautogui

# open and close profile page in LastWar game
# Randomize time delay
# Randomize click pixel offset

# UI locations
profile_button_location = [700, 50]
profile_button_close_pop_up_location = [1215, 120]

# Variables
default_sleep_time = 0.8  # in seconds
random_sleep_time_mix = 10  # in ms
random_sleep_time_max = 1000  # in ms
pixel_click_range_positive = 2  # pixels
pixel_click_range_negative = -2  # pixels


def click_with_random_sleep_and_cordinate_variation(ui_location):
    ui_location[0] += randint(pixel_click_range_negative, pixel_click_range_positive)
    ui_location[1] += randint(pixel_click_range_negative, pixel_click_range_positive)
    pyautogui.click(tuple(ui_location))
    time.sleep(default_sleep_time + randint(random_sleep_time_mix, random_sleep_time_max) / 1000)


click_with_random_sleep_and_cordinate_variation(profile_button_location)
time.sleep(default_sleep_time + randint(random_sleep_time_mix, random_sleep_time_max) / 1000)
click_with_random_sleep_and_cordinate_variation(profile_button_close_pop_up_location)
