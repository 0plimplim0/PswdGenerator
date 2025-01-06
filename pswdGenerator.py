import random

print("Password Generator")

while True:
    try:
        num = int(input("Number of characters: "))
        if num <= 0:
            raise ValueError("The number must be more than 0")
        break
    except ValueError as e:
        print(f"Invalid entry: {e}")

char = input("Enter the characters for the password (e.g: a,b,c) or click enter: ")
if not char.strip():
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
else:
    char = char.split(",")

pswd = "".join(random.choice(char) for i in range(num))

print(f"Your password is {pswd}")