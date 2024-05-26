import random 
import string 
longitug = input("Enter the length of the password: ")
while not longitug.isdigit():
    print("The length must be a numeric value")
    longitug = input("Enter the length of the password: ")

longitug = int(longitug)

def password_generator(longitug):
    if longitug < 8:
        print("The password must be at least 8 characters long")
    elif longitug > longitug:
        return
    caracters = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(random.choice(caracters) for i in range(longitug))
    return key

print(password_generator(longitug))
