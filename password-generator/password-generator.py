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

    with open("Password.txt", "a") as f:
        f.write(password + "\n")
        
    with open("password.txt") as f:
        print(f.read())
        
    f.close()
except ValueError as e:
    print("Invalid parameter!")

