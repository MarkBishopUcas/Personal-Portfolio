# this is for myself so i can easily run it in the web browser version of vs code python3 /workspaces/CP2-PROJECTS/MorseCodeTranslator/main.py
#this is what i was doing before, but then i read on the assignment that it requires lists instead of dictionaries. i spent forever making the dictionaries just to realise they are useless T-T im leaving them here since i at least want my hard work to be seen. 
'''
dict_char_to_morse = { 
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
    "0" : "-----",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "," : "--..--",
    "." : ".-.-.-",
    "-" : "-....-",
    "=" : "-...-",
    "!" : "-.-.--",
    "@" : ".--.-.",
    "'" : ".----.",
    '"' : ".-..-.",
    "/" : "-..-.",
    "?" : "..--..",
    "&" : ".-...",
    "(" : "-.--.",
    ")" : "-.--.-",
    "+" : ".-.-.",
    ":" : "---.",
    ";" : "-.-.-.",
    "," : "--..--",
    " " : "/"
}

dict_morse_to_char = {
    ".-" : "a",
    "-..." : "b",
    "-.-." : "c",
    "-.." : "d",
    "." : "e",
    "..-." : "f",
    "--." : "g",
    "...." : "h",
    ".." : "i",
    ".---" : "j",
    "-.-" : "k",
    ".-.." : "l",
    "--" : "m",
    "-." : "n",
    "---" : "o",
    ".--." : "p",
    "--.-" : "q",
    ".-." : "r",
    "..." : "s",
    "-" : "t",
    "..-" : "u",
    "...-" : "v",
    ".--" : "w",
    "-..-" : "x",
    "-.--" : "y",
    "--.." : "z",
    "-----" : "0",
    ".----" : "1",
    "..---" : "2",
    "...--" : "3",
    "....-" : "4",
    "....." : "5",
    "-...." : "6",
    "--..." : "7",
    "---.." : "8",
    "----." : "9",
    "--..--" : ",",
    ".-.-.-" : ".",
    "-....-" : "-",
    "-...-" : "=",
    "-.-.--" : "!",
    ".--.-." : "@",
    ".----." : "'",
    ".-..-." : '"',
    "-..-." : "/",
    "..--.." : "?",
    ".-..." : "&",
    "-.--." : "(",
    "-.--.-" : ")",
    ".-.-." : "+",
    "---..." : ":",
    "-.-.-." : ";",
    "/": " "
}
'''
#this is the method required for the assignment
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", ".", "-", "=", "!", "@", "'", '"', "/", "?", "&", "(", ")", "+", ":", ";", " "]
morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "--..--", ".-.-.-", "-....-", "-...-", "-.-.--", ".--.-.", ".----.", ".-..-.", "-..-.", "..--..", ".-...", "-.--.", "-.--.-", ".-.-.", "---...", "-.-.-.", "/"]

#morse code to english translator. 
def morse_to_english():
    #this gets the morse code from the user, i initially tried input,  but that dosent work since input is already used for getting inputs 
    #this text was inspired by a morse code translator website. it is pretty varied, so it shouldent count as plajorism, especially since im giving credit here https://morsecode.world/international/translator.html
    inp = input("Please enter the morse code. input the morse code with '.' and '-', do not use '_' use spaces between characters, and / between words: ")
    #this splits the input into a list, each charecter is an object in the list
    translate = inp.split(" ")
    #this is initialising the list before using it, because im pretty sure you cant use append on a list if it dosent exist
    translated = []
    #this is initialising the not reconised booleen because if an object isnt reconised it prints # and cheks if not reconised is true. 
    not_recognized = False
    #this is for objects in translate, so for each charecter that is in your input 
    for i in range(len(translate)):
            #checks if the object can be translated to, if not replaces it with hastag
        try: 
            #it appends the item from characters that matches the number of the item in morse codes
            translated.append(characters[morse_codes.index(translate[i])])
        except:
            #makes the charecter a # if it isnt reconised. 
            if translate[i] not in morse_codes:
                translate[i] = "#"
                translated.append(f" {translate[i]} ")
                not_recognized = True
    #outp is the outpt. "".join joins all characters with no space. 
    outp = "".join(translated)
    if not_recognized:
        print("\nWe saw some unreconised characters in your inputed text, we have replaced them with #'s.")
    print(f"\nhere is your translated text:\n\n{outp}")
    #im clearing the lists just in case it messes with the thing if you go back through. 
    translated.clear()
    translate.clear()

#function that translates english to morse code 
#this function is the exact same as the toe
def english_to_morse():
    inp = input("\nPlease enter the English text to be translated to morse code: ").lower()

    translate = list(inp)
    translated = []
    not_recognized = False
    for i in range(len(translate)):
        try:
            translated.append(morse_codes[characters.index(translate[i])])
        except:
            if translate[i] not in characters:
                translate[i] = "#"
                translated.append(f" {translate[i]} ")
                not_recognized = True
    outp = " ".join(translated)
    if not_recognized:
        print("\nWe saw some unreconised characters in your inputed text, we have replaced them with #'s.")
    print(f"\nhere is your translated text:\n\n{outp}")
    #im clearing the lists just in case it messes with the thing if you go back through. 
    translated.clear()
    translate.clear()

#main function
def main():
    #ui loop
    while True:
        #makes sure that the user only inputs 1,2, or 3
        try:
            selection = int(input("\nSelect an option below:\n\n(1) Convert English to Morse Code\n\n(2) Convert Morse Code to English\n\n(3) Exit Program\n\nType the number corresponding to your selection: "))
            if selection == 1:
                english_to_morse()
            elif selection == 2:
                morse_to_english()
            elif selection == 3:
                print("\nThanks for using our translator!\nOr, you could say\n- .... .- -. -.- ... / ..-. --- .-. / ..- ... .. -. --. / --- ..- .-. / - .-. .- -. ... .-.. .- - --- .-. -.-.--")
                break
            else:
                print("\nPlease only enter 1, 2, or 3.")
        except:
            print("\nPlease only enter a whole number.")

#runs the main function
if __name__ == "__main__":
    main()
