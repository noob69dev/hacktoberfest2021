import random
passwdlen = int(input("Enter the length of the password :-"))
x="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pass = "".join(random.sample(x,passwdlen ))
print(pass)
