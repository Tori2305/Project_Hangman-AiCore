import random 

fruit_list=["Apple", "Banana", "Orange", "Cherry","Watermelon"]

random_fruit = random.choice(fruit_list)


def check_guess(guess):
    guess=guess.lower()
    if guess in random_fruit:
        print(f"Good guess! {guess} is in the word")
    else: 
        print(f"Sorry {guess} not in the word")

def ask_for_input(): 
    while True:
        guess = str(input("Please place your guess here: "))
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character: ")
        else: 
           break
    check_guess(guess)

        
ask_for_input()