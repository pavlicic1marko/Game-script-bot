import pyautogui
import time
import re
import pytesseract
import cv2
import numpy as np

from Commands.Click import click_with_random_sleep_and_cordinate_variation
from POM.server_user_roles_page import *


# Start script on server's position selection screen.
# NOTE: if conquerors buff is enabled, scroll down before running.

# Function to convert HH:mm:ss to total minutes
def time_to_minutes(time_str):
    hours, minutes, _ = map(int, time_str.split(':'))
    return hours * 60 + minutes


def text_sanitization(time_str):
    print("timme:" + time_str)

    if not time_str:
        return ''
    if time_str[:3].isdigit():
        time_str = time_str[1:]  # Remove extra leading digit
    parts = time_str.split(':')
    if len(parts[2]) > 2:
        parts[2] = parts[2][:2]  # Remove extra trailing digit
    return ':'.join(parts)


def remove_stale_roles(left, top, message, role_ico_cordinates):
    x,y =role_ico_cordinates[0],role_ico_cordinates[1]
    # Define the region to capture (left, top)
    width = 85
    height = 25
    region = (left, top, width, height)
    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(message + " screenshot.png")  # save screenshot for debugging purpose
    # Convert the screenshot to a format suitable for pytesseract
    screenshot_rgb = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2RGB)

    # Define OCR configuration options
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789:'

    # Extract text with custom configuration
    text = text_sanitization(pytesseract.image_to_string(screenshot_rgb, config=custom_config))
    # Use regular expression to find time strings in HH:mm:ss format
    pattern = r'\b\d{2}:\d{2}:\d{2}\b'
    matches = re.findall(pattern, text)
    # Threshold in minutes
    threshold_minutes = 6
    if matches is None:
        print("{message} Screenshot returned NULL list.")
    elif not matches:
        print(f"{message} Screenshot returned no matches. Text: {text} ")
    else:
        # Threshold in minutes
        total_minutes = time_to_minutes(matches[0])
        if total_minutes >= threshold_minutes:
            print(f"{matches[0]} {message} is greater than {threshold_minutes} minutes.")

            # click given role
            click_with_random_sleep_and_cordinate_variation([x,y])

            # click dismiss
            click_with_random_sleep_and_cordinate_variation(dismiss_role_button)

            # click Confirm
            click_with_random_sleep_and_cordinate_variation(confirm_button)

            # exit position card to server screen
            click_with_random_sleep_and_cordinate_variation(close_applicant_list_button)
            click_with_random_sleep_and_cordinate_variation(close_applicant_list_button)
        else:
            print(f"{message} is less than {threshold_minutes} minutes.")


def remove_all_stale_roles():
    # Conquerors Buff includes two additional position cards. Set to False if conquerors buff is disabled.
    conquerorsBuff = False
    # list of coordinates for each position card, ordered Mil Cmdr to Sec Interior top left to bottom right
    if conquerorsBuff:

        staleRoleCoordinatess = [
            (2078, 485, 104, 25, 'Military Commander', 2109, 441),
            (2184, 718, 104, 25, 'Secretary of Strategy', 2212, 677),
            (2366, 718, 104, 25, 'Secretary of Security', 2396, 636),
            (2002, 951, 104, 25, 'Secretary of Development', 2053, 973),
            (2184, 951, 104, 25, 'Secretary of Science', 2209, 850)
        ]
    else:
        for role in staleRoleCoordinates:
            top,left,message,role_ico_cordinates = role
            remove_stale_roles(top, left, message, role_ico_cordinates)


    time.sleep(5)  # giving time to get screen ready


if __name__ == "__main__":
    remove_all_stale_roles()
