import secrets
import string

def generate_password(length=12):
    # Define a set of characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Create an empty string to store the password
    password = ""

    # Generate a random password of the specified length
    for _ in range(length):
        password += secrets.choice(characters)

    return password
print(generate_password())