from helper_funcs import helper
from battle_simulator import battle_simulator
from coin_change import change_calculator
from morse_code_translator import morse_code
from personal_library_program import personal_library
from random_password_generator import password_generator
from to_do_list import to_do_list

def main(): #i had to use run instead of main because it wouldnt let me use main because all my imports had main as their runner function. 
    while True:
        select = helper.inq_select(
        "Welcome to my personal portfolio!\nPlease feel free to look around, using the arrow keys for navigation.\n",
        "Battle simulator",
        "Change calculator",
        "Morse code translator",
        "Personal library program",
        "Random password generator",
        "To do list",
        "Exit")

        if select == 1:
            print("Battle simulator:\n"
              "What the project does: Simulates a turn-based PVE battle system where players can control different characters and use abilities.\n"
              "How you found the programming process: It was challenging to manage the game logic, especially ensuring smooth gameplay and interactions between characters.\n"
              "What you learned: I learned how to design and implement Python libraries, as well as work with random number generation to determine outcomes.")
            run_program = helper.inq_select("Would you like to run this?","Yes","No")
            if run_program == 1:
                battle_simulator.main_menu()
            else:
                continue

        elif select == 2:
            print("Change calculator:\n"
              "What the project does: Calculates the minimum number of coins needed to make change for a given amount of money.\n"
              "How you found the programming process: The logic was straightforward, but testing edge cases like large amounts and small coin denominations required a bit more effort.\n"
              "What you learned: I gained a deeper understanding of algorithms, specifically greedy algorithms, and how they apply to real-world problems like making change.")
            run_program = helper.inq_select("Would you like to run this?","Yes","No")
            if run_program == 1:
                change_calculator.main()
            else:
                continue

        elif select == 3:
            print("Morse code translator:\n"
              "What the project does: Converts text into Morse code and vice versa, allowing for communication in this traditional coding system.\n"
              "How you found the programming process: This was a fun project, it was a simple lookup system for Morse code translations from lists.\n"
              "What you learned: I learned how to build lookup lists, that functioned similarly to if you just had one dictionary, and how to handle string encoding and decoding, making the process of translating smooth and efficient.")
            run_program = helper.inq_select("Would you like to run this?","Yes","No")
            if run_program == 1:
                morse_code.main()
            else:
                continue

        elif select == 4:
            print("Personal library program:\n"
              "What the project does: Organizes a list of books, allowing the user to add, remove, and search for books in their collection.\n"
              "How you found the programming process: It was a great way to practice working with data structures, especially lists and dictionaries. UI design was also a challenge.\n"
              "What you learned: I learned how to manage user input and output effectively in Python.")
            run_program = helper.inq_select("Would you like to run this?","Yes","No")
            if run_program == 1:
                personal_library.main()
            else:
                continue

        elif select == 5:
            print("Random password generator:\n"
              "What the project does: Generates strong, random passwords for the user with customizable length and character types.\n"
              "How you found the programming process: The hardest part was ensuring the password was both secure and user-friendly, with a good mix of characters.\n"
              "What you learned: I learned how to use Python’s `random` library to generate secure passwords and the importance of using a variety of character types to strengthen security.")
            run_program = helper.inq_select("Would you like to run this?","Yes","No")
            if run_program == 1:
                password_generator.main()
            else:
                continue

        elif select == 6:
            print("To do list:\n"
              "What the project does: A simple to-do list application that allows users to add, remove, and mark tasks as complete.\n"
              "How you found the programming process: This was a straightforward project that helped me improve my understanding of file handling and user interfaces.\n"
              "What you learned: I learned how to create a persistent to-do list that saves user data, and I got better at working with file I/O and list management.")
            run_program = helper.inq_select("Would you like to run this?","Yes","No")
            if run_program == 1:
                to_do_list.main()
            else:
                continue

        elif select == 7:
            break

main()
