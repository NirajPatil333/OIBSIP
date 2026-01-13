import string 
import random 


def password_generator(length):

    character = string.ascii_letters + string.digits + string.punctuation

    password =''

    for _ in range(length):
        password += random.choice(character)

    return password


#  Main program 

print("==== password generator ====")

length = int(input("Enter the password length (e.g. 8,4,7) :" ))

if length  < 0:
    print("Enter the valid number")
else :
    pwd = password_generator(length)
    print("Youe generator Password is =",pwd)
