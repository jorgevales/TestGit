# Jorge Vales
# 2 de Mayo de 2023
# Primer programa (Cálculo de propinas) Curso de Python

print("Bienvenido a la calculadora de propinas")

# ENTRADAS
cuenta = float(input("¿Cuál es monto a pagar?"))
porcentaje = float(input("¿Cuánto porcentaje desea dar?: "))
comensales = int(input("¿Entre cuántas personas se dividirá la cuenta?"))

# PROCESOS (CÁLCULOS)
porcentaje_decimal = porcentaje/100
propina = cuenta * porcentaje_decimal
total_de_cuenta = cuenta + propina
pago_por_persona = total_de_cuenta / comensales
pago_total = round(total_de_cuenta, 2)

# SALIDA
print(f"\nEl total de la cuenta es: ${total_de_cuenta}\n\
Cada persona deberá pagar: ${pago_por_persona}\n\
(Se agregó una propina del {int(porcentaje)}% por persona)\n")