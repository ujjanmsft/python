import random

# Create a dictionary to map choices to emojis
emojis = {
    'r': '🪨',
    'p': '📄',
    's': '✂️'
}

# create a tuple with the choices
choices = ('r', 'p', 's')

def get_user_choice():
    while True:
        # Get user input
        user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()

        # Check if the user input is valid
        if user_choice in choices:
            return user_choice
        else:
            print("invalid choice!")
       

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

# Determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif(
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 'p' and computer_choice == 'r') or 
        (user_choice == 's' and computer_choice == 'p')):
        print("You win!")
    else:
        print("You lose!")



def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

play_game()