# Jorge Vales
# 2 de Mayo de 2023
# Calcula el IMC e indica el tipo de peso

print("Programa que calcula el IMC e indica el tipo de peso")
peso = float(input("Escribe tu peso: "))
altura = float(input("Escribe tu altura en metros: "))

IMC = round(peso/altura**2,2)
print(f"Tu IMC es: {IMC}")

if IMC < 18.5:
    print("Bajo Peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Normal")
elif IMC >= 25.0 and IMC <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")