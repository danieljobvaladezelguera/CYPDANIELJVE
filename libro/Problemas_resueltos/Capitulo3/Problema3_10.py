#Problema 3.10

print("Sucesión de Fibonacci hasta el # 180")

#Variables a declarar

PRI = 0
SEG = 1
I = 3

for i in range (3,180):
    if I <= 180:
        SIG = PRI + SEG
        PRI = SEG
        SEG = SIG
        I = I + 1
        print("Un numero de la serie es ", SIG)

print("Fin")

