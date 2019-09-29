import os
import random

# Enter your name here
# project1.py

def welcome():
    str_welcome = "WELCOME TO THE GUESS MASTER!"
    print(len(str_welcome))
    str_welcome_centered = str_welcome.center(40)
    print(str_welcome_centered)
    print("This game allows 10 tries to guess a world.")
    print("===========================================")
    print("Press ENTER to start the game:")

def pick():
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

    print(len(words_list))
    print(words_list)
    print(random.choice(words_list))


    
welcome()
pick()
