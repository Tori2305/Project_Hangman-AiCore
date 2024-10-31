import random
fruit_list=["Apple", "Banana", "Orange", "Cherry","Watermelon"]

random_fruit = random.choice(fruit_list)

User_guess = str(input("Please enter a single letter: "))

if ((User_guess >= "a" and User_guess <="z")) or ((User_guess>="A" and User_guess<="Z")) and len(User_guess) == 1:
    print("Good guess!")
else: 
    print("Oops!That is not a valid input.")

