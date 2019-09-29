import random

# Name
# project1.py


# Function welcome() accepts no arguments and returns no values
def welcome():
    str_welcome = "WELCOME TO THE GUESS MASTER!"
    str_welcome_centered = str_welcome.center(40)

    # Display a greeting and description of program's purpose
    print(str_welcome_centered)
    print("This game allows 10 tries to guess a world.")
    print("===========================================")

    # Prompt user to press the ENTER key continue
    input("Press ENTER to start the game:\n")


# Function pick() accepts no arguments and returns a String containing randomly selected word from words.txt file
def pick():
    # Initialize list to hold words.txt Strings
    words_list = []

    print("Selecting a word from my vocabulary...\n")

    # Opens the words.txt data file
    f = open("words.txt", "r")

    # Reads the words from the file (ignoring blank/whitespace lines)
    for line in f:
        # Iterates only through words in words.txt; Skips blank/whitespace lines
        if len(line.strip()) != 0:
            # Add each line in words.txt that contains 4-6 letter word to list
            words_list.append(line.strip())

    # Closes the words.txt data file
    f.close()

    # Returns the chosen word
    return random.choice(words_list)


# Function named guess() accepts three arguments (a guessed character, the secret word and the placeholder) and returns the updated placeholder String
def guess(guessed_letter, secret_word, placeholder):
    # Initialize list to hold placeholder String. Makes it easier when replacing guessed letter at specified index
    list_placeholder = list(placeholder)

    # Defines a loop repeating the length of the secret word
    for index, letter in enumerate(secret_word):
        # If character at secret word's current index matches the character guessed, replace the current placeholder String's character with the guess
        if guessed_letter.upper() == letter:
            list_placeholder[index] = letter

    # Convert above list_placeholder back to a String
    updated_placeholder = "".join(list_placeholder)

    # Return the updated placeholder String
    return updated_placeholder


# Function named play() accepts one argument (the secret word) and returns either True or False
def play(secret_word):
    # Initialize placeholder String
    placeholder = ""

    # Loop until length of the secret_word for placeholder String
    for i in range(0, len(secret_word)):
        placeholder = placeholder + "_"

    for i in range(1,11):
        # If all the character in the word have been guessed correctly, return True
        if placeholder == secret_word:
            # Display the selected word after winning
            print("The word was: %s" % secret_word)
            return True

        # Display placeholder String
        print(" ".join(placeholder))

        # Prompt the player for a letter to guess
        guessed_letter = input("Enter a letter for guess #%i: " % i)
        print()

        # If guess is a single character, call the guess() function
        if len(guessed_letter) == 1:
            updated_placeholder = guess(guessed_letter, secret_word, placeholder)
            placeholder = updated_placeholder

        # If the guess is > 1 character display the following message
        else:
            print("Single characters only...\n")

    # Display the selected word after losing
    print("The word was: %s" % secret_word)

    # Return False after loop completes
    return False


# Function main() accepts no arguments and returns no values
def main():
    # Call the welcome() function to display the message
    welcome()

    # Call the pick() function to select a word from the data file. Store the returned String into variable randomly_selected_word
    randomly_selected_word = pick()

    # Call the play() function to start the game. Store the returned boolean of play() into variable win_or_lose
    win_or_lose = play(randomly_selected_word)

    # Depending on the results of the game, display the appropriate message
    if win_or_lose:
        print("You guessed the word - congrats!")
    else:
        print("Sorry - better luck next time.")


if __name__ == "__main__":
    main()
