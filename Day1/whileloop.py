# Loop as long as user_input is true

user_input = ""

while user_input.lower() != "yes":
    user_input = input("Do you want to continue: ")
    print(f"You typed: {user_input}")

print("Great, you typed 'yes'!")