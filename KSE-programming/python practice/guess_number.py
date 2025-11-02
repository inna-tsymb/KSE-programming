# Simple number guessing game
import random

# Computer picks a number
secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 5

print("I'm thinking of a number between 1 and 10!")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Correct! You got it in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    print(f"Attempts remaining: {max_attempts - attempts}")
else:
    print(f"Game over! The number was {secret_number}")