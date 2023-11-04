import random

class Hangman():

  '''
  This class records and updates the player's progress.

  The attributes track how the player is doing while the methods update the state.
  '''

  def __init__(self, word_list, num_lives=5):
    '''
    'word' is the word from word_list which has been randomly selected by Python.
    'word_guessed' tracks the player's progress.
    'num_of_letters' tracks the number of unique, undiscovered letters still remaining in 'word'.
    'num_of_lives' tracks the number of lives the player has remaining (starting with 5).
    'word_list' is the list of words from which Python selected a random word.
    'list_of_guesses' records the guesses that the player has already made.
    '''
    self.word = random.choice(word_list)
    self.word_guessed = list(map(lambda x: '_', list(self.word)))
    self.num_of_letters = len(set(self.word))
    self.num_of_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []

  '''
  This method checks to see if a given guess matches with any letters in the chosen word.
  If it does, blank spaces in the word_guessed list whose index matches instances of that letter in the word 
  are replaced with that letter.
  If there is a match num_of_letters is updated.
  If there is not a match, the num_of_lives attribute is updated.
  '''
  def check_guess(self, guess):
      guess = guess.lower()
      if guess in self.word:
        print(f'Good guess! {guess} is in the word')
        for letter in self.word:
          if guess == letter:
            position = self.word.index(letter)
            self.word_guessed[position] = guess 
        self.num_of_letters -= 1  
      else:
        self.num_of_lives -= 1
        print(f'Sorry, {guess} is not in the word.')
        print(f'You have {self.num_of_lives} lives left.')  

  def ask_for_input(self):
    '''
    This method asks the player to make a guess
    and checks whether or not the guess is valid.
    '''
    guess = input('Please guess a letter: ')
    if len(guess) != 1 or not guess.isalpha():  
      print('Invalid letter. Please, enter a single alphabetical character.')  
    elif guess in self.list_of_guesses:
      print('You already tried that letter!')
    else:
      self.check_guess(guess)  
    self.list_of_guesses.append(guess)  

word_list = ['apple', 'orange', 'pear', 'cherry', 'strawberry']

def play_game(word_list):
  
  num_of_lives = 5
  game = Hangman(word_list, num_of_lives)

  while True:
    if game.num_of_lives == 0:
      print('You lost!')
      break
    if game.num_of_letters > 0:
      game.ask_for_input()
    if game.num_of_lives != 0 and game.num_of_letters == 0:
      print('Congratulations! You won the game!')  
      break


play_game(word_list)
