karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

import random

sifre = ""

sayi= int(input("Kaç karakterli bir şifre istersin \n"))

for i in range (sayi):
    sifre += random.choice(karakterler)

print(sifre)
