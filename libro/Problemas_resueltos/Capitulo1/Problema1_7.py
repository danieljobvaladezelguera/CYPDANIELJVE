#Problema 1.7
print ("Programa para calcular el area de un triangulo con 3 lados")

L1 = float(input("Dame el lado #1: "))
L2 = float(input("Dame el lado #2: "))
L3 = float(input("Dame el lado #3: "))

S = (L1 + L2 + L3)/2
AREA = (S * (S - L1) * (S - L2) * (S - L3) ) **0.5

print (f"El valor del area es de { AREA } u^2")
