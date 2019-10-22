#Programa 3.1

print("Programa tal que dado 10 números enteros, obtener la suma de los números impares y el promedio de los números impares")

#Datos a declarar

SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
i = 1

#Empieza el programa

print("Hola")

for i in range(1,11,1):

    NUM = int(input("Dame un número: "))

    if NUM != 0:
        
        if ( (-1) ** (NUM) ) > 0:
            
            SUMPAR = SUMPAR + NUM
            
            CUEPAR = CUEPAR + 1
            
        else:
            
            SUMIMP = SUMIMP + NUM
            
    i = i + 1
    
PROPAR = SUMPAR / CUEPAR

print(f"Promedio de pares es: {PROPAR} y suma de impares: {SUMIMP}")
