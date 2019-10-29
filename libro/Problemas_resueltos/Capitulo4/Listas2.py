#arreglos
#lectura
#escritura/asignacion
#actualizacion: insercion, eliminacion, modificacion
#ordenamiento
#busqueda

#escritura
frutas = ["Zapote", "Manzanas", "Pera", "Aguacate", "Durazno", "Uva", "Sandia"]

# lectura, el selector [ indice ]
print(frutas[2])

for indice in range (0,7):
    print(frutas[indice])
print("________________________")

#for opcion 2 --pdr por un itinerador for each

for fr in frutas:
    print(fr)
    
#asignacion
frutas[2]="Melon"
print(frutas)

#insercion al final
frutas.append("naranja")
print("frutas")
