import random
from time import sleep

pass_string = "abcdefghijklmnopqrstuvwxyz"
password = ""

while True:
    password = ""
    pass_string = "abcdefghijklmnopqrstuvwxyz"
    try:
        pass_length = int(input("Enter the length of the password :"))

        uppercase = input("Do you want to include uppercase letters? (Y/N): ").strip().upper()
        if uppercase not in ['Y', 'N']:
            print("Invalid input! Please enter Y or N.")
            continue
        pass_string += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if uppercase == 'Y' else ""

        numbers = input("Do you want to include numbers? (Y/N): ").strip().upper()
        if numbers not in ['Y', 'N']:
            print("Invalid input! Please enter Y or N.")
            continue
        pass_string += "0123456789" if numbers == 'Y' else ""

        special_characters = input("Do you want to include special characters? (Y/N): ").strip().upper()
        if special_characters not in ['Y', 'N']:
            print("Invalid input! Please enter Y or N.")
            continue    
        pass_string += "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" if special_characters == 'Y' else ""

        if pass_length < 8 or pass_length > 128:
            print("Please enter a valid integer for the password length (between 8 and 128).")
            continue

        print("Generating password...")
        sleep(3) 

    except ValueError:
        print("Please enter a valid integer for the password length.")
        continue

    for i in range(pass_length):
        random_character = random.choice(pass_string)
        password += random_character

    print("Generated Password:", password)


    while True:
        new_password = input("Do you want to generate another password? (Y/N): ").strip().upper()

        if new_password not in ['Y', 'N']:
            print("Invalid input! Please enter Y or N.")
            continue

        break

    if new_password == 'N':
        break
