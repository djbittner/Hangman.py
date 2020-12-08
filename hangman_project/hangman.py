"""
Author:  Derek Bittner
Program: final_project_hangman.py
"""
import random
from hangman_project.game_words import words
import string


def get_capital(words):
    word = random.choice(words)
    while '-' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_capital(words)
    letters = set(word)
    alphabet = set(string.ascii_lowercase)
    your_letters = set()
    attempts = 7

    while len(letters) > 0 and attempts > 0:
        print("You have ", attempts, "tries left, your letters are: ", " ".join(your_letters))

        word_list = [letter if letter in your_letters else "*" for letter in word]
        print("State Capital:  ", " ".join(word_list))

        user_guess = input("Guess a letter:  ").lower()
        if user_guess in alphabet - your_letters:
            your_letters.add(user_guess)
            if user_guess in letters:
                letters.remove(user_guess)

            else:
                attempts = attempts - 1
                print("Letter not in this State Capital.")

        elif user_guess in your_letters:
            print("Try again, letter has already been guessed!")

        else:
            print("Invalid letter, try again!")

    if attempts == 0:
        print("Sorry, the State Capital is: ", word)

    else:
        print("Correct, ", word, "was the correct State Capital!!")


hangman()

