import random

# Loop

while True:
# Ask: roll the dice?
    choice = input("Do you want to roll the dice? (y/n): ").lower()
# If user enters y
    if choice == 'y':
        random.randint(1, 6)
#    Generate a random number between 1 and 6
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
#    Print numbers
        print(f"{die1}, {die2}")
# If user enters n
    elif choice == 'n':
#    Print thank you message with "Goodbye"
        print("Thank you for playing! Goodbye!")
#    Terminate the program
    else:
#    Print invalid choice
        print("Invalid choice. Please enter 'y' or 'n'.")