# Hangman

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Description](#description)
- [Learnings](#learnings)
- [Usage](#usage)
- [Contributions](#contributions)
- [File Structure](#filing)
- [License](#license)
- [FullCode](#FullCode)
   

## Introduction 
This project is part of the AI Core curriculum and aims to build a Hangman game. Users can guess letters to figure out a randomly selected word from a list of words.


## Features 
- Randomly select a word from a list of words
- Allow users to guess letters
- Display the current state of the word with correctly guessed letters
- Track the number of lives remaining
- Provide feedback on whether the guessed letter is in the word
- End the game when the user either guesses the word or runs out

## Description
The aim of the project is to test the skills learned so far throughout my AiCore training course. Including; all data types, while,for and if loops, error handling and object orientation programming to name but a few. 

## Learnings
1. Python Programming - Ability to write and understand Python code, including the use of classes, functions, and control structures.
2. Object Orientation Programming - Understand OOP principals including encapsulation, inheritance, and the use of docstrings & comments.
3. Problem-Solving - Logically thinking about checking user input, updating the game state and handling game logic.
4. Code refactoring - Improving the readability and structure of my code, making it more maintainable and easier to understand.
5. User Input Handling - Effectively handling user input, including validation and feedback, which is essential for creating interactive applications.
6. Randomisation - Ability to use Python random module demonstrating ability to work with external libraries.
7. Documentation - Using clear and concise dostrings and comments helping others to understand purpse and use of my code.

## Usage

Initialise the game:

      import random

      class Hangman:
        """
        A class to represent the game Hangman
        """
        
        def __init__ (self, word_list,num_lives):
         """
         Constructs all the necessary attributes for the class object.
             
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

Play the game:

        if __name__ =="__main__":
        fruit_list = ["apple", "banana", "orange", "grape", "watermelon"]
        play_game(fruit_list)



**Play as it is, or if you'd like to change parts of the game, you can amend the following:**
- **Change the number of tries** a user has: see *line 122*.
- **Change the words in the list**: On *line 138*, change `fruit_list` to whatever list you'd like. When you play the game, be sure to change this to the new name of your list.

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Filing
All the workings within the project are saved in [this folder](hangman_workings)
The code for the game is also saved [here](Hangman_game.py)

## License information
This project is licensed under the MIT License. See the LICENSE file for details.
