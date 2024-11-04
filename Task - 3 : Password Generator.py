import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
        
    if length < 1:
        return "Error: Password length must be at least 1"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator 🔑")
    
    try:
        length = int(input("Enter the desired password length: "))
        
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        print("\nGenerated Passwords 🔑:")
        for i in range(5):
            password = generate_password(length, use_uppercase, use_digits, use_special)
            print(f"{i+1}. {password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
