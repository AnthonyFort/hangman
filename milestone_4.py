import random

class Hangman():

  def __init__(self, word_list, num_lives=5):
    self.word = random.choice(word_list)
    self.word_guessed = list(map(lambda x: '_', list(self.word)))
    self.num_letters = len(set(self.word))
    self.num_of_lives = num_lives
    self.word_list = word_list
    self.list_of_guesses = []

  def check_guess(self, guess):
      guess = guess.lower()
      if guess in self.word:
        print(f'Good guess! {guess} is in the word')
        for letter in self.word:
          if guess == letter:
            position = self.word.index(letter)
            self.word_guessed[position] = guess 
        self.num_letters -= 1  
      else:
        self.num_of_lives -= 1
        print(f'Sorry, {guess} is not in the word.')
        print(f'You have {self.num_of_lives} lives left.')  

  def ask_for_input(self):
    while True:
      guess = input('Please guess a letter: ')
      if len(guess) != 1 or not guess.isalpha():  
        print('Invalid letter. Please, enter a single alphabetical character.')  
      elif guess in self.list_of_guesses:
        print('You already tried that letter!')
      else:
        self.check_guess(guess)  
      self.list_of_guesses.append(guess)  

  @staticmethod  
  def calc_unique_letters_count(word, word_guessed):  
    print('hey')


word_list = ['apple', 'orange', 'pear', 'cherry', 'strawberry']

hang = Hangman(word_list)

# print(hang.word)
# print(hang.word_guessed)
# hang.update_progress('e')
# print(hang.word_guessed)
# print(hang.num_letters)

hang.ask_for_input()

