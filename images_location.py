import os


def get_image_folder_path():
    base_path = os.path.dirname(os.path.abspath(__file__))
    return base_path
