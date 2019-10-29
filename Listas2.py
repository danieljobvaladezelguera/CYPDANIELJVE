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
frutas.append("Naranja")
print(frutas)
frutas.insert(2,"limon")
print(len(frutas))
print(frutas)
print(len(frutas))

#eliminacion

print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas[2] = "limon"
frutas.append("limon")
frutas.append("limon")
print(frutas)
frutas.remove("limon")
print(frutas)

#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

#busqueda

print(f"El Uva esta en la pos { frutas.index('Uva') } ")
print(f"El limon esta { frutas.count ('limon') } veces en la lista ")

#concatenar

print(frutas)
otras_frutas = ["Rambutan", "Nispero", "Lichie", "Pitahaya"]
frutas.extend(otras_frutas)
print(frutas)

#copiar

copia = frutas
copia.append("Naranja")
print(copia)

otra_copia = frutas
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)
