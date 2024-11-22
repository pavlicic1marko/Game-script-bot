import time
from POM.server_user_roles_page import *
from Commands.Click import click_with_random_sleep_and_cordinate_variation


# Start script on server's position selection screen.
# NOTE: if conquerors buff is enabled, scroll down before running.

def approve_applicant(coordinates):
    # Click the position card from given coordinates.
    # click the approve button location a few times. Then exit out of the position card.

    # click on role
    click_with_random_sleep_and_cordinate_variation(coordinates)

    # click list button
    click_with_random_sleep_and_cordinate_variation(applicants_list_button)

    # click approve in list
    for i in range(3):
        click_with_random_sleep_and_cordinate_variation(approve_applicant_button)

    # exit position card to server screen
    click_with_random_sleep_and_cordinate_variation(close_applicant_list_button)
    click_with_random_sleep_and_cordinate_variation(close_applicant_list_button)
    time.sleep(2)  # giving operator time to stop the script


def approve_all_users():
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


    else:

        time.sleep(2)  # giving operator time to stop the script
        #  approve all 5
        approve_applicant(Secretary_of_Strategy_icon)
        approve_applicant(Secretary_of_Security_icon)
        approve_applicant(Secretary_of_development_icon)
        approve_applicant(Secretary_of_science_icon)
        approve_applicant(Secretary_of_interior_icon)


if __name__ == "__main__":
    approve_all_users()
