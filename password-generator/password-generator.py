import random
import string

def password_generator(length):
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

try:
    password_length = int(input("Enter password length: "))
    if password_length<=0:
        raise ValueError

    password = password_generator(password_length)
    print("Proposed password: ", password)

    file = open("password.txt", "a")
    file.write(password)
    file.write("\n")
    with open("password.txt") as f:
        print(f.read())
    file.close()
except ValueError as e:
    print("Invalid parameter!")

