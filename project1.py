import os
import random

# Enter your name here
# project1.py


def welcome():
    str_welcome = "WELCOME TO THE GUESS MASTER!"
    #print(len(str_welcome))
    str_welcome_centered = str_welcome.center(40)
    print(str_welcome_centered)
    print("This game allows 10 tries to guess a world.")
    print("===========================================")
    print("Press ENTER to start the game:\n")


def pick():
    print("Selecting a word from my vocabulary...")
    # defaults to C:\Users\YourWindowsUserName
    #print(os.listdir())
    #f = open("Desktop\Python-Guessing-Game\words.txt", "r")
    f = open("words.txt", "r")
    #line = f.readline()
    count = 1
    words_list = []

    for line in f:
        # prints only lines with words in words.txt; skips whitespace lines
        if len(line.strip()) != 0:
            words_list.append(line.strip())
            #print("%s count: %i" % (line.strip(),count))
            count = count + 1
    f.close()

    #print(len(words_list))
    #print(words_list)
    #print(random.choice(words_list))

    return random.choice(words_list)


def guess(guessed_letter, secret_word, placeholder):
    updated_placeholder = ""
    list_placeholder = list(placeholder)
    print(list_placeholder)

    for index, letter in enumerate(secret_word):
        if(guessed_letter == letter):
            updated_placeholder = placeholder + guessed_letter
        else:
            updated_placeholder = updated_placeholder + placeholder
        print(letter + " ", end = "")
    print("\n")

    return updated_placeholder

def play(secret_word):
    placeholder = ""

    for i in range(0, len(secret_word)):
        placeholder = placeholder + "_"

    print(" ".join(placeholder))

    guess("A", secret_word,placeholder)

    #for val in placeholder:
    #    print(val + " ", end = '')
    #print("\n")

    # loop repeats 10 times
    for i in range(1,11):
        print("Enter a letter for guess #%i:" % i)


def main():
    welcome()
    randomly_selected_word = pick()
    #guess("A", randomly_selected_word,"_")
    play(randomly_selected_word)

if __name__ == "__main__":
    main()


#welcome()
#secret_word = pick()
#print(secret_word)
#guess("R",secret_word,len(secret_word))
#play(secret_word)
