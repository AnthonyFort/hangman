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
      print(guess)
      if guess in self.word:
        print(f'Good guess! {guess} is in the word')


  def update_progress(self, guess):
    for letter in self.word:
      if guess == letter:
        position = self.word.index(letter)
        self.word_guessed[position] = guess 

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

hang.check_guess('e')
