#Ejercicio 2.3

print("Programa para saber raices de un trinomio cuadrado")

A = float(input("Dame el valor que está en X^2: "))

B = float(input("Dame el valor que está en X: "))

C = float(input("Dame el valor de la constante: "))

DIS = 0 
X = 0
Y = 0

if A > 0:
    DIS = B**2 - 4*A*C
    if DIS >=0:
            X = ((- B) + (DIS)**0.5)/(2*A)
            Y = ((- B) - (DIS)**0.5)/(2*A)
            print(f"Valor de X1 es {X}, y de X2 es {Y}")
    else:
        print("El valor de la discriminante es menor a 0")

else:
    print("No se puede realizar la operación")


