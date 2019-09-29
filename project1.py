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
    #updated_placeholder = ""

    #print("Placeholder input to guess: ")
    # no spaces on this placeholder
    #print(placeholder)
    list_placeholder = list(placeholder)


    for index, letter in enumerate(secret_word):
        if guessed_letter == letter:
            list_placeholder[index] = letter

    print(list_placeholder)

    # add spaces to new placeholder
    updated_placeholder = "".join(list_placeholder)
    #print(updated_placeholder)

    return updated_placeholder


def play(secret_word):
    placeholder = ""
    updated_placeholder = ""

    for i in range(0, len(secret_word)):
        placeholder = placeholder + "_"

    # placeholder W/O spaces
    #print(placeholder)

    #for val in placeholder:
    #    print(val + " ", end = '')
    #print("\n")

    # loop repeats 10 times
    for i in range(1,11):
        print("starting loop")
        if placeholder == secret_word:
            print("The word was: %s" % secret_word)
            return True
        print(" ".join(placeholder))
        guessed_letter = input("Enter a letter for guess #%i: " % i)
        if len(guessed_letter) == 1:
            updated_placeholder = guess(guessed_letter, secret_word, placeholder)
        else:
            print("Single characters only")
        placeholder = updated_placeholder
        #print(updated_placeholder)

    print("The word was: %s" % secret_word)
    return False


def main():
    welcome()
    randomly_selected_word = pick()
    print("Randomly selected word is: %s" % randomly_selected_word)
    #guess("A", randomly_selected_word,"_")
    win_or_lose = play(randomly_selected_word)
    if win_or_lose:
        print("You guessed the word - congrats!")
    else:
        print("Sorry - better luck next time.")

if __name__ == "__main__":
    main()


#welcome()
#secret_word = pick()
#print(secret_word)
#guess("R",secret_word,len(secret_word))
#play(secret_word)
