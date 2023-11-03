import random

word_list = ['apple', 'orange', 'pear', 'cherry', 'strawberry']
word = random.choice(word_list)
guess = input('Please provide a single letter: ')

if len(guess) == 1 and guess.isalpha():
  print('Good guess!')
else:
  print('Oops! That is not a valid input.')  



