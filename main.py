import random
print("Olá, eu me chamo Kauê")
name = input("Digite seu nome para começarmos a converter:")
aleat = random.randint(0, 200)
binary = bin(aleat)
res = binary[2:]
print(res)
