#Problema 2.7

print("Programa para saber el acomodado de mayor a menor de 3 números")

A = int(input("Dame un número: "))
B = int(input("Dame un número: "))
C = int(input("Dame un número: "))

if A > C :
    if B > C:
        if B > A:
            print(f"Número de mayor a menor son {B}, {A} y {C}")

        else:
            print(f"Número de mayor a menor son {A}, {B} y {C}")

    else:
        print(f"Número de mayor a menor son {A}, {C} y {B}")

elif B > A:
    if B > C:
        print(f"Número de mayor a menor son {B}, {C} y {A}")

    else:
        print(f"Número de mayor a menor son {C}, {B} y {A}")

else:
    print(f"Número de mayor a menor son {C}, {A} y {B}")

print("Fin del programa :3/")
