
import random

karakterler = (
    "+-/*!&$#?=@"
    "abcdefghijklnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "1234567890"
)

uzunluk = int(input("Şifrenizin uzunluğunu giriniz: "))

sifre = []

for i in range(uzunluk):
    karakter = random.choice(karakterler)
    sifre.append(karakter)

sifre = "".join(sifre)

print("---------------------")
print(sifre)
print("Şifreniz bu.")
