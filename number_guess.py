import random

# Generate a random number between 1 and 100
num_to_guess = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Let the user guess the number
guess = int(input("Take a guess: "))

if guess == num_to_guess:
    print("Congratulations! You guessed it!")
else:
    print(f"Sorry, the number I was thinking of was {num_to_guess}.")