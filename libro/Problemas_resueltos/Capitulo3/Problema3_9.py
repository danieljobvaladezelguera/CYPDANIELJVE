#Programa 3.9

print("Diagrama de flujo que lea un numero entero N y calcule la suma de una serie")

SERIE = 0

N = int(input("Dame un numero"))

I = 1

for i in range (1,N + 1):

    if I <= N:
        SERIE = SERIE + I**I
        I = I + 1

print(SERIE)
