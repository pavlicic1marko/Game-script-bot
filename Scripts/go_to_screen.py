import pyautogui

from Commands.click_on_image import *
from Scripts.logging_commands import log_info


def find_screen_name():
    if try_find_image_on_screen('secretary_of_strategy.png', 0.95):
        return 'server'

    if try_find_image_on_screen('world_button.png', 0.95):
        return 'base'

    if try_find_image_on_screen('base_button.png', 0.95):
        return 'world'

    return ''  # screeen not found


def try_to_go_to_3_main_screens():
    log_info("user is on screen:" + find_screen_name())
    for i in range(1, 4):
        image_list = ['back_button_blue.PNG', 'back_button_blue.png', 'back_button_gray.PNG',
                      'back_button_see_through.PNG', 'close_profile_button.PNG', 'awesome.png',
                      'base_button_zoom_out.png','hero_pop_up_addvertisment.png']

        if not (find_screen_name()): # if not(iuser on 3 main screens), if not try to get to these screens
            for image in image_list:
                if not (find_screen_name()):
                    click_on_image_if_visible(image, image)

        if not (find_screen_name()): # if not(iuser on 3 main screens), if not try to get to these screens, if user clicked on a base or a monster
            click_on_image_if_visible('mall_button.png','mall_button.png')
            click_on_image_if_visible('back_button_see_through.png','mall_button.png')



    log_info("user is on screen:" + find_screen_name())

    # move mouse to random coordinates in case mause is over button
    move_mouse_to_random_cordinates()


def go_to_server_screen_from_base_screen():
    profile_cordinates = find_profile_button_location()
    if (profile_cordinates == False):
        return False
    click_with_random_sleep_and_cordinate_variation(profile_cordinates)

    time.sleep(1) # sometimes server pop-up loads slow
    try:
        try_to_click_on_immage_and_on_smaller_resolution('server_button.png', 0.8)
    except pyautogui.ImageNotFoundException:
        return False


def go_to_base_screen_from_world_screen():
    try_to_click_on_immage_and_on_smaller_resolution('base_button.png',0.9)

def find_profile_button_location():
    image_cordinates_mall = try_find_image_on_screen('mall_button.png', 0.9)
    image_cordinates_heros = try_find_image_on_screen('heros_label.png', 0.9)

    #if cordinates for one of the images is not found return None
    if (image_cordinates_heros == False or image_cordinates_mall == False):
        return False

    image_cordinates_mall_center_height = image_cordinates_mall[1] + image_cordinates_mall[3] / 2
    image_cordinates_heros_center_with = image_cordinates_heros[0] + image_cordinates_heros[2] / 2
    return [image_cordinates_heros_center_with, image_cordinates_mall_center_height]


