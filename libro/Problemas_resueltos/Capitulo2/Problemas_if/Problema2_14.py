#Problema 2.14

#De que trata el problema
print("Programa para saber que tanto gastarían por medicinas")

#Dialogos con instrucciones para el usuario

ENF = int(input("Dime tu enfermedad(tienes tos(1), fiebre(2), escalofrío(3), vomito(4)): "))
EDAD = int(input("Dime tu edad: "))
DIAS = int(input("Dime cuantos días te quedaste en el Hospital: "))

#Palabras a declarar

ENF == 0
COSTO = 0
COSTOT = 0

#Comienza el programa

if (ENF == 1):
    COSTO = DIAS*25
    
    if 22 >= EDAD >= 14:
        COSTOT = (COSTO*1.10)
        print(f"{COSTOT}")
    else:
        print(f"{COSTO}")

elif (ENF == 2):
    COSTO = DIAS*16
    if 22 >= EDAD >= 14:
        COSTOT = (COSTO*1.10)
        print(f"{COSTOT}")
    else:
        print(f"{COSTO}")

elif ENF == 3:
    COSTO = DIAS*20
    if 22 >= EDAD >= 14:
        COSTOT = (COSTO*1.10)
        print(f"{COSTOT}")
    else:
        print(f"{COSTO}")

elif ENF == 4:
    COSTO = DIAS*32
    if 22 >= EDAD >= 14:
        COSTOT = (COSTO*1.10)
        print(f"{COSTOT}")
    else:
        print(f"{COSTO}")
        
print("Fin del programa")
