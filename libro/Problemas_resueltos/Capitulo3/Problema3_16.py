#Problema 3.16

print("Problema de bodegas")

#Declaracion de variables

TIPO1 = 0
TIPO2 = 0
TIPO3 = 0
TIPO4 = 0
TIPO5 = 0
MCTIPO2 = 0

N = int(input("Dame un numero del vino: "))

I = I + 1

for i in range (0,N):
    if I <= N:
        J = 1
        TOTVIN = 0

        while J <= 5:
            V = int(input("Que tipo de vino es??: "))
            TOTVIN = TOTVIN + V

            if J == 1:
                TIPO1 = TIPO1 + 1
            elif J == 2:
                TIPO2 = TIPO2 + 1

                if V > MCTIPO2:
                    MCTIPO2 = V
                    AÑO = 1

            if J == 3:

                if V == 0:
                    print(f"El año {AÑO
