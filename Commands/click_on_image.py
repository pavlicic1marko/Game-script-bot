from Commands.Click import *

top = 0
left = 655
height = 1079
wight = 609
region = (left, top, wight, height)  # game screen dimensions

def click_on_image(image_name):
    image_cordinates = pyautogui.locateOnScreen('C:/Users/MP/PycharmProjects/LastWarautomation/images/'+ image_name,
    region=region, confidence=0.8, grayscale=True)
    x,y = pyautogui.center(image_cordinates)
    click_with_random_sleep_and_cordinate_variation([x,y])


def click_on_exact_image(image_name):
    image_cordinates = pyautogui.locateOnScreen('C:/Users/MP/PycharmProjects/LastWarautomation/images/' + image_name,                                               region=region, confidence=1, grayscale=True)
    click_with_random_sleep(image_cordinates)

