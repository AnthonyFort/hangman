import random

word_list = ['apple', 'orange', 'pear', 'cherry', 'strawberry']
word = random.choice(word_list)

while True:
  guess = input('Please provide a single letter: ')
  if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
    break
  else:
    print('Invalid letter. Please, enter a single alphabetical character.')  



