otra =  bool(int(input("Hay más alumnos??(0 no, 1 si): ")))
suma = 0.0
cont = 0

while(otra == True): #
    cal = float(input("Calificacion: "))
    cont += 1
    suma += cal
    otra = bool(int(input("Hay más alumnos??(0 no, 1 si): ")))

print("Suma:",suma)
print("promedio: ",suma/cont)
print("Fin del programa")

