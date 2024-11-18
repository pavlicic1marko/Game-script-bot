import pyautogui
import time
import re
import pytesseract
from PIL import Image
import cv2
import numpy as np

# Start script on server's position selection screen.
# NOTE: if conquerors buff is enabled, scroll down before running.

# Function to convert HH:mm:ss to total minutes
def time_to_minutes(time_str):
    hours, minutes, _ = map(int, time_str.split(':'))
    return hours * 60 + minutes


def text_sanitization(time_str):
    if not time_str:
        return ''
    if time_str[:3].isdigit():
        time_str = time_str[1:]  # Remove extra leading digit
    parts = time_str.split(':')
    if len(parts[2]) > 2:
        parts[2] = parts[2][:2]  # Remove extra trailing digit
    return ':'.join(parts)



def approve_applicant_list(x, y):
    # Click the position card from given coordinates.
    # click the approve button location a few times. Then exit out of the position card.
    clickSeconds1 = .65
    clickSeconds2 = .35

    # click position card
    pyautogui.click(x, y)
    time.sleep(clickSeconds1)
    # click list button
    listX = 1179
    listY = 907
    pyautogui.click(listX, listY)
    time.sleep(clickSeconds1)
    # click approve
    approveX = 1099
    approveY = 252
    for i in range(3):
        pyautogui.click(approveX, approveY)
        time.sleep(clickSeconds2)
    # exit position card
    exitX = 1208
    exitY = 112
    pyautogui.click(exitX, exitY)
    time.sleep(clickSeconds2)
    pyautogui.click(exitX, exitY)
    time.sleep(clickSeconds1)
    time.sleep(4)  # giving operator time to stop the script
    return True


def main():
    # Conquerors Buff includes two additional position cards. Set to False if conquerors buff is disabled.
    conquerorsBuff = False
    # list of coordinates for each position card, ordered Mil Cmdr to Sec Interior top left to bottom right
    if conquerorsBuff:
        coordinates = [
            (2109, 441),  # Military Commander
            (2316, 425),  # Administration Commander
            (2212, 677),  # Secretary of Strategy...
            (2396, 636),
            (2053, 973),
            (2209, 850),
            # Note, a player liking the bot's profile makes a permanent screen appear. This may be exited via the "Awesome" button.
            (2383, 955)
        ]

        staleRoleCoordinates = [
            (2078, 485, 104, 25, 'Military Commander', 2109, 441),
            (2184, 718, 104, 25, 'Secretary of Strategy', 2212, 677),
            (2366, 718, 104, 25, 'Secretary of Security', 2396, 636),
            (2002, 951, 104, 25, 'Secretary of Development', 2053, 973),
            (2184, 951, 104, 25, 'Secretary of Science', 2209, 850)
        ]
    else:
        coordinates = [
            (956, 507),  # Secretary of Strategy...
            (1124, 500),  # Security
            (774, 724),  # development
            (963, 730),  # science
            # Note, a player liking the bot's profile makes a permanent screen appear. This may be exited via the 'Awesome' button.
            (1144, 724)   # Interior
        ]
        staleRoleCoordinates = [
            (2359, 627, 104, 40, 'Secretary of Security', 2397, 545),
            (2175, 629, 104, 40, 'Secretary of Strategy', 2212, 535)
        ]
    time.sleep(5)  # giving time to get screen ready
    i = 9
    while True:
        i = i + 1
        # Iterate through the positions and approve all
        for x, y in coordinates:
            approve_applicant_list(x, y)
            time.sleep(4)  # giving operator time to stop the script

        time.sleep(4)  # giving operator time to stop the script


if __name__ == "__main__":
    main()