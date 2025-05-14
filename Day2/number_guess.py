import random

# Print welcome message
print("Welcome to the Number Guessing Game!")

# Initialize a Counter
attempts = 0

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

#Loop
while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        # Check if the guess is within the valid range
        if guess < 1 or guess > 100:
            print("Invalid guess! Please enter a number between 1 and 100.")
            continue

        # Compare the guess with the number to guess

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number!")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")