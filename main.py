import random

c = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

l = int(input("specificare lunghezza password"))
password = ""

for i in range(l):
    password += random.choice(c)

print("la tua password sarà", password)
