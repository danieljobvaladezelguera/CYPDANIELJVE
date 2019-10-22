#Programa 3.7

print("Programa para saber tipos de venta")

#Variables a declarar

GRAN = 0
MED = 0
CHIC = 0

#Inicio del programa

N = int(input("Cuantas ventas has tenido??: "))

I = 1

for i in range (1,N+1):

    if I <= N:
        V = int(input("Dime el precio de la venta: "))

        if V <= 200:
            CHIC = CHIC + 1
        else:

            if V < 400:
                MED = MED + 1
            else:
                GRAN = GRAN + 1

        I = I + 1

print("Los pagos mayores son de: ", GRAN)
print("Los pagos medianos son de: ", MED)
print("Los pagos chicos son de: ", CHIC)
        
