import random

randN = random.randint(1, 101)
print(randN)
#guess = int(input('Enter an integer number between (1 - 100): \n>>> '))

while True:
	guess = int(input('Enter an integer number between (1 - 100): \n>>> '))
	if guess == randN:
		print('You guessed it right!!!')
		break 
	elif guess > randN:
		print('Guess is too high')
	elif guess < randN:
		print('Guess is too low')