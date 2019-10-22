#Programa 3.1

#Programa que sume una serie que tiene un aumento de 2 y 3

print("Programa que sume una serie que tiene un aumento de 2 y 3")

#Variables a declarar

BAND = 'T'

SUMSER = 0

I = 2

#Inicia el programa

for i in range (1,1800,1):
     
    if I <= 1800:

        print("imprime el valor de i =", I)
        
        SUMSER = SUMSER + 1 
        
     
        if BAND == 'T':
            BAND = 'F'
            I = I + 3
     
        else:
            BAND = 'T'
            I = I + 2
    else:
        
print("Fin")
