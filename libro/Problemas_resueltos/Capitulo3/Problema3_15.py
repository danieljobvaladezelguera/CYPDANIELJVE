#Problema 3.15

print("programa para saber que tanto hay que pagar por una llamada")

print()
print()

print("Las llamdas internacionales tienen costo de los primeros 3 min a $7.59")
print("Cada minuto adicional tendrá un costo adicional de $3.03")
print()
print("Las llamadas nacionales tienen un costo de los primeros 3 min a $1.20")
print("Cada minuto adicional tendrá un costo adicional de $0.48")

#Declaracion de las variables

Cl = 0
CUENTA = 0
L = 0
N = 0
I = 0
COSTO = 0

#Comienzo del programa

print("Llamadas nacionales (1), llamadas internacionales (0)")
TIPO = str(input("Dame a donde quieres llamar, N, I o L: "))
DURA = int(input("Dime cuantos minutos quieres hablar: "))

while TIPO != 'T' and DURA != -1:

    if TIPO == 'I':
        if DURA > 3:
            COSTO = (7.59) + ((DURA)-3)*3.03
            print(COSTO)
        else:   
            COSTO = 7.59
            print(COSTO)

    if TIPO == 'L':
        Cl = Cl + 1
        if Cl > 50:
            COSTO = 0.60
            print(COSTO)
        else:
            COSTO = 0
            print(COSTO)

    elif TIPO == 'N':
        if DURA > 3:
            COSTO = (1.20) + ((DURA)*3)*0.48
            print(COSTO)
        else:
            COSTO = 1.20
            print(COSTO)
    
    CUENTA = CUENTA + COSTO

    print("Llamadas nacionales (1), llamadas internacionales (0)")
    TIPO = str(input("Dame a donde quieres llamar, N o I: "))
    DURA = int(input("Dime cuantos minutos quieres hablar: "))

else:
        print(f"El costo total es de ", CUENTA)
