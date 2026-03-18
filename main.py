print("Hello, GitHub from Python!")

import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print("Welcome to Guess the Number Game!")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed it right!")
        break