import random
import string

def generate_password(length):
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + symbols

    # Ensure password includes at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Generate the rest of the password
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure random order
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired length for the password (minimum 4 characters): "))
            if length < 4:
                print("Password length should be at least 4 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
