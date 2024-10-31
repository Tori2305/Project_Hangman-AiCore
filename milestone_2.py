import random
fruit_list=["Apple", "Banana", "Orange", "Cherry","Watermelon"]

random_fruit = random.choice(fruit_list)

user_guess = str(input("Please enter a single letter: "))

if ((user_guess >= "a" and user_guess <="z")) or ((user_guess>="A" and user_guess<="Z")) and len(user_guess) == 1:
    print("Good guess!")
else: 
    print("Oops!That is not a valid input.")

