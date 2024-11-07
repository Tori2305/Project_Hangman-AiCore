import random
fruit_list = ["apple", "banana", "orange", "grape", "watermelon"]


class Hangman:
  def __init__ (self, word_list,num_lives):
    self.word_list = fruit_list
    self.num_lives=5
    self.word= random.choice(self.word_list)
    self.word_guessed=[" _ " * len(self.word)]
    self.num_letters=set(self.word)
    self.list_of_guesses=[]

  def check_guess(self,guess):
    guess=guess.lower()
    if guess in self.word:
      print(f"Good guess! {guess} is in the word")
      for guess in self.word:
        if guess in word_guessed:
          index = [i for i, l in enumerate(self.word)if l == guess]
          for i in index:
            word_guessed = word_guessed[:i] + guess + word_guessed[i+1:]
      num_letters-=1
    else:
      num_lives -=1
      print(f"Sorry, {guess} is not in the word")
      print(f"You have {num_lives} lives left")

  
  def ask_for_input(self):
    while True:
      guess=str(input("Please guess a single alphabetical letter: "))
      if guess != 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character: ")
      elif guess in list_of_guesses:
        print("You've already tried that letter!")
      else:
        list_of_guesses=list_of_guesses.append(guess)
        self.check_guess(guess)