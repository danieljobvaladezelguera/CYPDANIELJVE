#Problema 4

SUE = float(input("Dame tu sueldo: "))

if SUE < 1000:
    MSUE = SUE * 1.15
    print(f"Nuevo sueldo de {MSUE}")

else:
    NSUE = SUE * 1.12
    print(f"Nuevo sueldo de {NSUE}")
