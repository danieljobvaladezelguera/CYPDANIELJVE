#Problema 3.12

print("Obtener el numero de empleados")
print("el sueldo del trabajador")
print("y escribir el mayor de este empleados")

#Variables a declarar

MASUE = 0

#Inicio del programa

N = int(input("Dame el numero de empleados de la empresa: "))

I = 1

while I <= N:
    NUMEMP = int(input("Dame tu numero de empleado: "))
    SUE = int(input("Dame tu sueldo: "))

    if SUE > MASUE:
        MASUE = SUE
        MANUM = NUMEMP
        I = I + 1

    else:
        I = I + 1

print(f"El empleado {NUMEMP} es el de mayor suelo con {MASUE}")
