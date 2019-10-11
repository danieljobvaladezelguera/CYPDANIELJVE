#Programa 2.4
CAL = 0
print("Programa para sacar calificaciones")

CUENTA = int(input("Deme el # de cuenta: "))

C1 = float(input("Deme la cal #1: "))
C2 = float(input("Deme la cal #2: "))
C3 = float(input("Deme la cal #3: "))
C4 = float(input("Deme la cal #4: "))
C5 = float(input("Deme la cal #5: "))

CAL = (C1 + C2 + C3 + C4 + C5)/5

if CAL >=6:
    print(f"El alumno {CUENTA} tiene de promedio {CAL}, siendo aprobado")

else:
    print(f"El alumno {CUENTA} tiene de promedio {CAL}, siendo reprobado")
    
