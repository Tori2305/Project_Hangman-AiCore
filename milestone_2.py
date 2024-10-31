import random
word_list=["Apple", "Banana", "Orange", "Cherry","Watermelon"]
word = random.choice(word_list)

guess = str(input("Please enter a single letter: "))

if ((guess >= "a" and guess <="z")) or ((guess>="A" and guess<="Z")) and len(guess) == 1:
    print("Good guess!")
else: 
    print("Oops!That is not a valid input.")

