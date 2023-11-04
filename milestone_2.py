import random

word_list = ['apple', 'orange', 'pear', 'cherry', 'strawberry']
word = random.choice(word_list)

while True:
  guess = input('Please provide a single letter: ')
  if len(guess) == 1 and guess.isalpha():
    if guess in word:
      print(f'Good guess, {guess} is in the word.')
      break
    else:
      print(f'Sorry, {guess} is not in the word. Try again')
  else:
    print('Invalid letter. Please, enter a single alphabetical character.')  

print(word)

