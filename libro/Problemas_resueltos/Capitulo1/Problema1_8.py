# Programa que calcule la distancia de 2 puntos en el plano cartesiano

print("Programa para calcular la distancia de 2 puntos cartecianos")

X1 = float(input("Deme el valor de X1 :"))
Y1 = float(input("Deme el valor de Y1 :"))
X2 = float(input("Deme el valor de X2 :"))
Y2 = float(input("Deme el valor de Y2 :"))

D = ( (X2 - X1)**2 + (Y2 - Y1)**2 )**0.5

print (f"La Distancia es de { D } U ")

