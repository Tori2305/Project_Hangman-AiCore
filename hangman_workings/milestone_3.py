import random 

fruit_list=["Apple", "Banana", "Orange", "Cherry","Watermelon"]

random_fruit = random.choice(fruit_list).lower()


def check_guess(user_guess):
    user_guess=user_guess.lower()
    if user_guess in random_fruit:
        print(f"Good guess! {user_guess} is in the word")
    else: 
        print(f"Sorry {user_guess} not in the word")

def ask_for_input(): 
    while True:
        user_guess = str(input("Please place your guess here: "))
        if len(user_guess)!=1 or not user_guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character: ")
        else: 
           break
    check_guess(user_guess)

        
ask_for_input()