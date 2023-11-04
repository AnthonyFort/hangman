import random

# Defines a list of words from which Python will select one at random. 
word_list = ['apple', 'orange', 'pear', 'cherry', 'strawberry']
word = random.choice(word_list)

def ask_for_input():
  guess = input('Please provide a single letter: ')
  if len(guess) == 1 and guess.isalpha():
    check_guess(guess)
  else:
    print('Invalid letter. Please, enter a single alphabetical character.') 

def check_guess(guess):
    if guess in word:
      print(f'Good guess, {guess} is in the word.')
    else:
      print(f'Sorry, {guess} is not in the word. Try again')
  
ask_for_input()
  

print(word)


