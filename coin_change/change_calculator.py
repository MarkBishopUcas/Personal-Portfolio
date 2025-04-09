import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helper_funcs')))

from helper_funcs.helper import menu_select


from .coin_utils import run_coin_program

def main():
    """Main menu that allows users to start the coin program or exit."""
    while True:
        selection = menu_select("Main Menu", "Start Coin Program", "Exit")

        if selection == 1:
            run_coin_program()
        elif selection == 2:
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
