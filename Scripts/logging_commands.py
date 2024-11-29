import os
import sys
import logging
logger = logging.getLogger(__name__)
log_to_file = True

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2 # or 2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

logging.basicConfig(filename=resource_path('logs\\myapp.log'), level=logging.INFO)

def log_info(message:str):
    if log_to_file:
        logger.info(message)
    else:
        print(message)