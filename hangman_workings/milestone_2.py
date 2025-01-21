# milestone_2.py
import random

def guess_fruit():
    fruit_list = ["Apple", "Banana", "Orange", "Cherry", "Watermelon"]
    random_fruit = random.choice(fruit_list)
    user_guess = str(input("Please enter a single letter: "))

    if user_guess.isalpha() and len(user_guess) == 1:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
