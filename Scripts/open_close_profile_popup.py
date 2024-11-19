from POM.player_base_page import *
from Commands.Click import click_with_random_sleep_and_cordinate_variation


def main():
    click_with_random_sleep_and_cordinate_variation(profile_button_location)
    click_with_random_sleep_and_cordinate_variation(profile_button_close_pop_up_location)


if __name__ == "__main__":
    main()
    