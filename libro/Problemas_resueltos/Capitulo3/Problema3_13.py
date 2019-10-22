#Programa 3.13

print("Promedios mensuales del clima en Argentina")

#Variables a declarar

ARSU = 0
ARNO = 0
MERSU = 50000
ARCE = 0
I = 1
MES = 0 
PRORCE = 0

for i in range (1,3):
    RNO = int(input("Dame el # de lluvia en el norte: "))
    RCE = int(input("Dame el # de lluvia en el centro: "))
    RSU = int(input("Dame el # de lluvia en el sur: "))

    ARNO = ARNO + RNO
    ARCE = ARCE + RCE
    ARSU = ARSU + RSU

    if RSU < MERSU:
        MERSU = RSU
        MES = I
    else:
        I = I + 1

PORCE = ARCE / 12

print("Promedio region centro: ", PRORCE)
print("Mes con menor lluvia Reg sur: ", MES)
print("Registro del mes: ", MERSU)

if ARNO > ARCE :
    if ARNO > ARSU:
        print("La region con mayor lluvia es el norte")

    else:
        print("La region con mayor lluvia es el sur")

else:

    if ARCE > ARSU:
        print("La region con mayor lluvia es la region centro")

    else:
        print("La region con mayor lluvia es la region sur")
        
