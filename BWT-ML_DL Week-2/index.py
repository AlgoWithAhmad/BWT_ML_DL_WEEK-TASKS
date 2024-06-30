import re

def get_user_input():
    # Prompt the user for their details
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    favorite_number = input("Enter your favorite number: ")

    # Store the inputs in a dictionary
    user_info = {
        "name": name,
        "age": age,
        "email": email,
        "favorite_number": favorite_number
    }

    return user_info

def validate_email(email):
    # Check if the email contains "@" and "."
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def display_message(user_info):
    # Format and display the message
    print(f"Hello {user_info['name']}, you are {user_info['age']} years old, your email is {user_info['email']}, and your favorite number is {user_info['favorite_number']}.")

def main():
    user_info = get_user_input()
    while not validate_email(user_info["email"]):
        print("Invalid email format. Please enter a valid email.")
        user_info["email"] = input("Enter your email: ")

    display_message(user_info)

if __name__ == "__main__":
    main()
