import secrets
import string
from time import sleep

def get_yes_no(question):
    while True:
        answer = input(question).strip().upper()

        if answer in ("Y", "N"):
            return answer == "Y"

        print("Invalid input! Please enter Y or N.")


def generate_password(length, characters, include_uppercase,include_numbers, include_special):
    password_characters = []

    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

    if include_uppercase:
        password_characters.append(secrets.choice(uppercase))

    if include_numbers:
        password_characters.append(secrets.choice(numbers))

    if include_special:
        password_characters.append(secrets.choice(special_characters))

    for _ in range(length - len(password_characters)):
        password_characters.append(secrets.choice(characters))

    return "".join(password_characters)


while True:
    try:
        pass_length = int(input("Enter the password length (8-128): "))

        if not 8 <= pass_length <= 128:
            print("Password length must be between 8 and 128.")
            continue

    except ValueError:
        print("Please enter a valid integer.")
        continue

    pass_string = string.ascii_lowercase

    include_uppercase =  get_yes_no("Include uppercase letters? (Y/N): ")
 
    include_numbers = get_yes_no("Include numbers? (Y/N): ")

    include_special = get_yes_no("Include special characters? (Y/N): ")

    print("\nGenerating password...")
    sleep(1)

    password = generate_password(pass_length, pass_string, include_uppercase, include_numbers, include_special)

    print("Generated password:", password)

    if not get_yes_no("\nGenerate another password? (Y/N): "):
        print("Thank you for using the password generator!")
        break
