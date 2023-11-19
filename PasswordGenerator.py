import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Get desired password length from user
        length = int(input("Enter the desired length of the password: "))

        # Check if the length is non-negative
        if length <= 0:
            print("Please enter a valid positive length.")
            return

        # Generate and display the password
        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
