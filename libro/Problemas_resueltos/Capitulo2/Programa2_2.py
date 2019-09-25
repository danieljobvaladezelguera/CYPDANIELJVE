#Ejercicio 2
SUE = float(input("Escribe el salario que gana: "))

if SUE < 1000:
    AUM = SUE * .15
    MSUE = SUE + AUM
    print(f"El nuevo sueldo es {MSUE}")
    print(f"El aumendo fue de {AUM}")
print("Fin del programa")
