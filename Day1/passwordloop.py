attempts = 0
while True:
    password = input("Enter your password: ")
    attempts += 1
    if password == "python123":
        print("Access granted!")
        break
    elif attempts >= 4:
        print("Too many attempts. Access denied.")
        break
    else:
        print("Incorrect password. Try again.")
