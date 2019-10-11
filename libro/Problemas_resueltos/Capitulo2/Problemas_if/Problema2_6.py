#Programa 2.6

print("Programa para saber si un número es par, impar o nulo")

NUM = int(input("Dame un número: "))

if NUM == 0:
    print("Es nulo el número")

elif (-1)**NUM >0:
    print("El número es par")

else:
    print("El número es impar")
    
