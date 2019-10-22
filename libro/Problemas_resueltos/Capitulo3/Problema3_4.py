#Calculo de aumento de sueldo para un grupo de empleados de una empresateniendo en cuenta varios criterios

print("Programa para saber el sueldo y la nómina")

#VARIABLES A DECLARAR

NOM = 0
NSUE = 0

#Inicio del programa

print("hola")

SUE = int(input("Dame tu sueldo: "))

while SUE != -1:
    if SUE < 1000:
        NSUE = SUE*1.15
    else:
        NSUE = SUE*1.12
        NOM = NOM + NSUE
        print("El nuevo sueldo será de",NSUE)
        SUE = int(input("Dame un nuevo sueldo: "))
else:
    print("Fin del programa")
    print(NOM)
