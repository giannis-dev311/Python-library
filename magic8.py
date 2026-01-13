# Write code below 💖

import random
question = input('Question:   ')
random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'yes'
elif random_number == 2:
  answer = 'no'
elif random_number == 3:
  answer = 'maybe'
elif random_number == 4:
  answer = 'doubtful'
elif random_number == 5:
  answer = 'try again'
elif random_number == 6:
  answer = 'cant answer'
elif random_number == 7:
  answer = 'no doubt'
elif random_number == 8:
  answer = 'ask someone else'
elif random_number == 9:
  answer = 'not now'
else: 
  answer = 'error'

print('Magic 8 Ball:  ' + answer)
