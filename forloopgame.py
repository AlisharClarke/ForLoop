from random import *

#Generates a random integer.
# aRandomNumber = randint(1, 20)
aRandomNumber = 3
# For Testing: print(aRandomNumber)

tries = 0
for tries in range(3):
	guess = input("Guess a number between 1 and 20 (inclusive): ")
	if not guess.isnumeric(): # checks if a string is only digits 0 to 9
		print("That's not a positive whole number, try again!")
	else:
		guess = int(guess) # converts a string to an integer
	if (guess) == aRandomNumber:
		print("Good job")
		break
	elif guess > 20:
		print("You need to make your number smaller ):")
	else:
		print("try again")
	tries += 1
	print("tries = ", tries)
	# tries = tries + 1

# while (guess) == randint:
#   print (i)
