#Problema 3.6

print("Programa para ver que numero es mayor o menor")

#Variables a declarar

MAY = -100000
MEN =  100000

N = int(input("Dame un numero: "))

I = 1

for i in range (1,N+1):
    NUM = int(input("Dame otro numero: "))
    if NUM > MAY:
        MAY = NUM

    if NUM < MAY:
        MEN = NUM

    I = I + 1
print(MAY)
print(MEN)
