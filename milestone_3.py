import random 

fruit_list=["Apple", "Banana", "Orange", "Cherry","Watermelon"]

random_fruit = random.choice(fruit_list)
while True:
    guess=input("Enter a single character here: ")
    if guess.isalpha() and len(guess)==1:
        break
    else: 
        print("Invalid letter. Please, enter a single alphabetical character: ")

for fruit in random_fruit:
    if guess in fruit:
        print(f"Good guess! {guess} is in the word")
    else: 
        print(f"Sorry {guess} not in the word")
        break

print(random_fruit)
