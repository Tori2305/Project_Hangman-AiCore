import random

class Hangman:

  def __init__(self, word_list, num_lives):
    self.word_list= word_list
    self.num_lives = 5
    self.word = list(random.choice(self.word_list).lower())
    self.list_letter=[]
    self.word_guessed= [" "] * len(self.word)
    self.num_letters = len(set(self.word))