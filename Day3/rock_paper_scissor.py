import random

# Create a dictionary to map choices to emojis
emojis = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}

# create a tuple with the choices
choices = ('r', 'p', 's')

# Get user input
while True:
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

    # Check if the user input is valid
    if user_choice not in choices:
        print("invalid choice!")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'You chose {emojis[computer_choice]}')

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 'p' and computer_choice == 'r') or 
        (user_choice == 's' and computer_choice == 'p')):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break