#Problema 3.5

print("Programa para saber los números mayores a 0 y promedios")

#Declarar variables

SUMPOS = 0
CUEPOS = 0
SUMOTR = 0

#Inicio del programa

N = int(input("Dame un numero: "))

I = 1

for I in range (1,N+1):
    NUM = int(input("Dame otro numero "))
    if NUM > 0:
        SUMPOS = SUMPOS + NUM
        CUEPOS = CUEPOS + 1
    else:
        SUMOTR = SUMOTR + NUM
    I = I + 1
else:
    PROGEN = (SUMPOS + SUMOTR)/N
    PROPOS = (SUMPOS/CUEPOS)

    print("La cantidad de numeros positivos son: ", CUEPOS)
    print("El promedio de los numeros son: ", PROGEN)
    print("Los numeros positivos en total son: ", PROPOS)

