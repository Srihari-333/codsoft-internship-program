import random
import string

def generate_password(length):
    # Define the character sets to generate the password from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice to select from characters
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        password_length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    # Generate the password
    password = generate_password(password_length)
    
    # Display the password
    print("Generated password:", password)

if __name__ == "__main__":
    main()
