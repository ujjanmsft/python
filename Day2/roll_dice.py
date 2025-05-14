import random

# Initialize a Counter
roll_count = 0

# Print welcome message
print("Welcome to the Dice Roller!")

# Loop

while True:
# Ask: roll the dice?
    choice = input("Do you want to roll the dice? (y/n): ").lower()
# If user enters y
    if choice == 'y':
#    Increment the roll count
        roll_count += 1
#    Generate a random number between 1 and 6
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
#    Print numbers
        print(f"{die1}, {die2}")
# If user enters n
    elif choice == 'n':
#    Print thank you message with "Goodbye"
        print("Thank you for playing!")
        print(f"You rolled the dice {roll_count} times.")
        print("Goodbye!")
#    Break the loop
        break
#    Terminate the program
    else:
#    Print invalid choice
        print("Invalid choice! Please enter 'y' or 'n'.")