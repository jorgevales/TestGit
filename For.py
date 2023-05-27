import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '&', '*', '?', '+']

tot_letras = int(input("Ingresa el total de letras en tu contraseña: "))
tot_numeros= int(input("Ingresa el total de números en tu contraseña: "))
tot_simbolos = int(input("Ingresa el total de símbolos en tu contraseña: "))

password = []

for i in range(tot_letras):
    password.append(random.choice(letras))

for i in range(tot_numeros):
    password.append(random.choice(numeros))

for i in range(tot_simbolos):
    password.append(random.choice(simbolos))

random.shuffle(password)

finalpassword = ''.join(password)

print(f"Tucontraseña final es: " {finalpassword})
