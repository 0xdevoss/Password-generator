import random

#This is a variable for generate password
character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-_+="
pass_length = int(input("Enter password length (4-20): "))
password = ""

#Chose password length
while pass_length < 4 or pass_length > 20:
    print("Invalid length. Please enter a number between 4 and 20.")
    pass_length = int(input("Enter password length (4-20): "))

#Generate password
while len(password) < pass_length:
    char = random.choice(character)
    password += char
#Show password
print("Your password: ", password)