import random

class Hangman:
  """
  A class to represent the game Hangman
  """
  def __init__ (self, word_list,num_lives):
    """Constructs all the necessary attributes for the class object.
    
    Parameters
    ----------
      word_list : list
        list of words which the computer can randomly select from.
      num_lives : int
        number of lives that the user has to guess the right word.
      """
    self.word_list = word_list
    self.num_lives = num_lives
    self.word = random.choice(self.word_list)
    self.word_guessed = [" _ "] * len(self.word)
    self.num_letters = len(set(self.word))
    self.list_of_guesses = []

  def check_guess(self,guess):
    """
    Checks whether the user's guess is in the word. 
    If it's a new correctly guessed letter, it is added to the 
    output which showcases which letters are missing
    
    Parameters
    ---------- 
    guess : str 
      The letter guessed by the user.
    """
    if guess in self.word:
        print(f"Good guess! {guess} is in the word")
        for index,char in enumerate(self.word):
           if char == guess:
              self.word_guessed[index] = guess
        self.num_letters -= 1
        print(" ".join(self.word_guessed))
    else:
      self.num_lives -= 1
      print(f"Sorry, {guess} is not in the word")
      print(f"You have {self.num_lives} lives left")

  def ask_for_input(self):
    """ 
      Asks the user for their input to start the game. 
      It also checks to see if the user has already guessed 
      that letter and if it's a repeated letter, asks for another input.
      If the letter is correct and not been guessed before, it then 
      runs check_guess().
    """
    while True:
      guess=input("Please guess a single alphabetical letter: ").lower()
      if len(guess) != 1 or not guess.isalpha():
        print("Invalid letter. Please, enter a single alphabetical character: ")
      elif guess in self.list_of_guesses:
        print("You've already tried that letter!")
      else:
        self.list_of_guesses.append(guess)
        self.check_guess(guess)
        #Not necessary but for a sanity check - print word guessed so far
        print(self.word_guessed)
        break
        
def play_game(word_list):
  """
  Plays the game. 
  States the number of lives the player has and provides 
  feedback as to when the user has won/lost the game. 
  They can win if all the letters are guessed correctly 
  or lose if they run out of lives. 
  
  Parameters 
  ---------- 
  word_list : list 
    List of words from which the computer can randomly select.
  """
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

