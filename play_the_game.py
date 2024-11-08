import random


class Hangman:
  def __init__ (self, word_list,num_lives):
    self.word_list = word_list
    self.num_lives= num_lives
    self.word= random.choice(self.word_list)
    self.word_guessed=[" _ "] * len(self.word)
    self.num_letters=len(set(self.word))
    self.list_of_guesses=[]

  def check_guess(self,guess):
    if guess in self.word:
        print(f"Good guess! {guess} is in the word")
        for index,char in enumerate(self.word):
           if self.word[index]==guess:
              self.word_guessed[index] = guess
        self.num_letters -= 1
        print(" ".join(self.word_guessed))
    else:
      self.num_lives -= 1
      print(f"Sorry, {guess} is not in the word")
      print(f"You have {self.num_lives} lives left")

  def ask_for_input(self):
    while True:
      guess=input("Please guess a single alphabetical letter: ")
      guess=guess.lower()
      if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character: ")
      elif guess in self.list_of_guesses:
        print("You've already tried that letter!")
      else:
        self.list_of_guesses.append(guess)
        self.check_guess(guess)
        print(self.word_guessed)
        break
        
def play_game(word_list):
  num_lives=5
  game=Hangman(word_list, num_lives)
  while True:
    if game.num_lives == 0:
      print("You've lost!")
      print(f"The word was {game.word}")
      break
    elif game.num_letters > 0:
      game.ask_for_input()
    else:
      print("Congratulations. You won the game!")
      break

if __name__ =="__main__":
  fruit_list = ["apple", "banana", "orange", "grape", "watermelon"]
  play_game(fruit_list)

