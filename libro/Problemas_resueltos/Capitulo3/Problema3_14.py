#Problema 3.14

#Variables a declarar 
AP1 = 0
AP2 = 0
AP3 = 0
AP4 = 0
AP5 = 0
RECAU = 0
PRE = 0


P1 = int(input("Dame el primer dato: "))
P2 = int(input("Dame el segundo dato: "))
P3 = int(input("Dame el tercer dato: "))
P4 = int(input("Dame el cuarto dato: "))
P5 = int(input("Dame el quinto dato: "))

CLAVE = int(input("Dame la clave: "))

CANT = int(input("Dime cuanto tiempo llamarás: "))

while CLAVE > 0 and CANT > 0:

        if CLAVE == 1:
            PRE = P1*CANT
            AP1 = AP1 + CANT

        elif CLAVE == 2:
            PRE = P2*CANT
            AP2 = AP2 + CANT
        elif CLAVE == 3:
            PRE = P3*CANT
            AP3 = AP3 + CANT
        elif CLAVE == 4:
            PRE = P4*CANT
            AP4 = AP4 + CANT
        elif CLAVE == 5:
            PRE = P5*CANT
            AP5 = AP5 + CANT

        print(CLAVE)
        print(CANT)
        print(PRE)

        RECAU = RECAU + PRE

        CLAVE = int(input("Dame de nuevo la clave: "))
        CANT = int(input("Dame cuanto tiempo llamaras: "))

print("La cantidad de boletos tipo 1 es: ", AP1)
print("La cantidad de boletos tipo 1 es: ", AP2)
print("La cantidad de boletos tipo 1 es: ", AP3)
print("La cantidad de boletos tipo 1 es: ", AP4)
print("Recaudacion del estado es: ", RECAU)
