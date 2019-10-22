#Problema 3.3

print("Programa para una sucesion de numeros")

#Variables a declarar

N = int(input("Dame el numero final denominador de la serie: "))

SERIE = 0
BAND = 'T'
I = 1

if I <= N:
    
    for I in range (1,N,1):
        
        
        if BAND == 'T':
            
            SERIE = SERIE + 1/I
            BAND = 'F'

        else:
            
            SERIE = SERIE -1/I
            BAND = 'T'
        I = I + 1

    
print("El valor de SERIE es de:", SERIE)

print("Fin")




