from random import randint
secret = randint(1,10)
print("welcome!")
guess = 0
print secret
while guess != secret:
	g = input ("Guess the number: ")
	guess = int(g)
	if guess == secret:
		print("You win!")
	elif guess < secret:
		print("Too low!")
	else: 
		print("Too high!")
print("Game over")	