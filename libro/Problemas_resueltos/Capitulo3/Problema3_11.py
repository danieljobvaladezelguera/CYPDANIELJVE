#Problema 3.11

print("Programa que usa el INE para conteo de votos")

#Variables a declarar

CAN1 = 0
CAN2 = 0
CAN3 = 0
CAN4 = 0

#Inicio del programa

print("El candidato 1 es igual a 1")
print("El candidato 2 es igual a 2")
print("El candidato 3 es igual a 3")
print("El candidato 4 es igual a 4")
VOTO = int(input("Deme el numero del candidato: "))

while 0 < VOTO <= 4:
    if VOTO == 1:
        CAN1 = CAN1 + 1
    elif VOTO == 2:
        CAN2 = CAN2 + 1
    elif VOTO == 3:
        CAN3 = CAN3 + 1
    elif VOTO == 4:
        CAN4 = CAN4 + 1

    VOTO = int(input("Deme el numero del candidato: "))

else:
        SUMV = CAN1 + CAN2 + CAN3+ CAN4
        POR1 = (CAN1/SUMV)*(100)
        POR2 = (CAN2/SUMV)*(100)
        POR3 = (CAN2/SUMV)*(100)
        POR4 = (CAN2/SUMV)*(100)

print(f"El primer candidato tuvo {POR1} con un total de {CAN1} de votos")
print(f"El segundo candidato tuvo {POR2} con un total de {CAN2} de votos")
print(f"El tercer candidato tuvo {POR3} con un total de {CAN3} de votos")
print(f"El cuarto candidato tuvo {POR4} con un total de {CAN4} de votos")

print("FIN")
