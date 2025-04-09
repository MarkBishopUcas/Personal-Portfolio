# this is for myself so i can easily run it in the web browser version of vs code python3 /workspaces/CP2-PROJECTS/RandomPasswordGenerator/main.py
import random

#password generator function. the reason i only used one function this whole time, is that really nothing needed to be repeated, and the stuff that was repeated needed to be done in loops
def req_getter_func():

    #the method i use for making sure the user only inputs one of the selected options needs the variables to be initialised beforhand 
    uppercase = 0
    number = 0
    spec_char = 0
    length = 0

    while length < 1:
        try:
            length = int(input("\nHow many characters long does your password need to be? "))
            if length < 1:
                print("Your password must be at least 1 charecter long")
        except:
            print("\nPlease only enter in a whole number.")

    #this is initialising the lists for later use
    uppsers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    spec_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "|", ";", ":", ",", "\\", '"', "'", "<", ".", ">", "/", "?", "`", "~", "}", "]"]

    while uppercase > 3 or uppercase < 1:
        try:
            uppercase = int(input("\nDoes your password need to have uppercase letters?\n\n(1) Only lowercase letters\n\n(2) Lowercase and uppercase letters\n\n(3) Only uppercase letters\n\nPlease type the number of your option: "))
            if uppercase > 3 or uppercase < 1:
                print("\nPlease select only 1, 2, or 3\n")
        except:
            print("\nPlease only enter a whole number.")

    while number > 2 or number < 1:
        try:
            number = int(input("\nDoes your password need to have numbers?\n\n(1) Yes\n\n(2) No\n\nPlease type the number of your option: "))
            if number > 2 or number < 1:
                print("\nPlease select only 1 or 2\n")
        except:
            print("\nPlease only enter a whole number.")

    while spec_char > 2 or spec_char < 1:
        try:
            spec_char = int(input("\nDoes your password need to have special characters?\n\n(1) Yes\n\n(2) No\n\nPlease type the number of your option: "))
            if spec_char > 2 or spec_char < 1:
                print("\nPlease select only 1 or 2\n")
        except:
            print("\nPlease only enter a whole number.")

    # Generate 4 passwords
    for i in range(4):
        password = []  # Reset the password list for each iteration
        while len(password) < length:
            selection = random.randint(1, 4)
            if selection == 1:  # Letters
                #if upercase is 1, there is only lowercase 
                if uppercase == 1:
                    password.append(random.choice(letters))
                #if upercase is 2 there is both upercase and lowercase
                elif uppercase == 2:
                    password.append(random.choice(letters + uppsers))
                    #and fi its 3 its only upers
                elif uppercase == 3:
                    password.append(random.choice(uppsers))
            elif selection == 2:  # Numbers
                if number == 1:
                    password.append(random.choice(numbers))
            elif selection == 3:  # Special Characters
                if spec_char == 1:
                    password.append(random.choice(spec_chars))
        #this prints the passwords once complete
        print(f"Password {i + 1}/4: {''.join(password)}")

#main function
def main():
    while True:
        req_getter_func()
        if int(input("would you like to generate any more passwords?\n\n(1) Yes\n\n(2) No\n\nPlease select the number corrosponding to your option: ")) == 2:
            print("\nThank you for using our Random Password Generator!")
            break

#i read while importing code it can acidentally run if you dont have this, so i put this for running my code because its probably good practice for futer programs that could need it. 
if __name__ == "__main__":
    main()