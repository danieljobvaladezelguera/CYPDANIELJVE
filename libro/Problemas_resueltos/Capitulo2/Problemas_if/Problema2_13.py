#Problema 2.13

print("Programa para poder determinar si el alumno puede seguir cursando")
MAT = int(input("Escribe la matricula del alumno: "))
SEM = int(input("Dime el semestre en donde estas: "))
CARR = int(input("Dime que carrera cursas: Economia(1), Computacion(2), Administracion(3) o Contabilidad(4): "))
PROM = float(input("Dime tu promedio: "))

#Variables a declarar

"""
Economía = 1
Computación = 2
Administacion = 3
Contabilidad = 4
"""

#Inicia programa

if (CARR == 1):
    if (SEM >= 6 and PROM >= 8.8):
        print(f"Aceptado el alumno {MAT} en la carrera {CARR} con promedio {PROM}")
        
else:
    if(CARR == 2):
        if (SEM > 6 and PROM > 8.5):
            print(f"Aceptado el alumno {MAT} en la carrera {CARR} con promedio {PROM}")

    else:
        if (CARR == 3):
            if (SEM > 5 and PROM > 8.5):
                print(f"Aceptado el alumno {MAT} en la carrera {CARR} con promedio {PROM}")
        else:
            if (CARR == 4):
                if (SEM > 5 and PROM > 8.5):
                    print(f"Aceptado el alumno {MAT} en la carrera {CARR} con promedio {PROM}")

            else:
                print("Rechazado")
    
