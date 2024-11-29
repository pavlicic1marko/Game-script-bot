import os
import sys
from funcy import print_durations

import cv2
import easyocr
import numpy as np

from Scripts.logging_commands import log_info

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

@print_durations()

def analize_using_easyocr():
    # Create an OCR reader object
    reader = easyocr.Reader(['en'])

    img = cv2.imread(resource_path('images\\full_screen\\screenshot.png'))
    result = reader.readtext(img)
    # Read text from an image
    #result = reader.readtext(resource_path('images\\full_screen\\screenshot.png'))

    # Print the extracted text
    for detection in result:
        print(detection[1])
        log_info("time in screenshot is: " + detection[1])

if __name__ == "__main__":

    analize_using_easyocr()