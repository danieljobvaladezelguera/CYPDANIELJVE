#Arreglo de 

#Variables a declarar

LLUVIAS_NORTE =[80,60,120,100,70,150,100,47,95,70,100,130]

for indice in range(1,12,1):
    print(f" mes  { indice +1 } en region norte={ LLUVIAS_NORTE[indice] } ")

print(LLUVIAS_NORTE[4])


sueldos = []
for indice in range(7):
    sueldos.append(int(input("Dame el sueldo: ")))

print(sueldos)

suma = 0

for indice in range(7):
    suma += sueldos[indice]

promedio = suma / 7

for indice in range (7):
    if sueldos[indice] > promedio:
        cont = cont + 1
        print(f"Arriba:", (sueldos[indice]))
