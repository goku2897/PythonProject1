#Python program to check the validity of password input by users.

username = input("Please enter your username: ")
password = input("Please enter your password: ")


def check_password(username, password):
    # Check if username matches password
    if password == username:
        raise ValueError("Username should not match the password.")

    # Check for password length (between 3 and 8 characters)
    if len(password) < 3 or len(password) > 8:
        raise ValueError("Password should contain between 3 to 8 characters.")

    # Additional checks for password (optional)
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")

    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")

    if not any(char in "!@#$%^&*()" for char in password):
        raise ValueError("Password must contain at least one special character (!@#$%^&*()).")

    print("Password is valid.")


# Validate the password
try:
    check_password(username, password)
except ValueError as e:
    print(e)

