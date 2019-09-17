# print tiene 4 formas de uso
"""
1.- con comas
2.- con signo +
3.- con la funcion format ()
4.- es con una variante de format

"""

# con comas, concatenar agregando un
#espacio y haciendo casting de tipo

edad = 10
nombre = "Juan"
estatura = 1.67

print(edad , estatura , nombre )

# con '+' hace lo mismo pero no
# realiza el casting automatico
# no agregra espacio
print( str(edad) + str(estatura) + str(nombre))


#funcion format ()
print("Nombre: {} Edad: {} ".format(nombre, edad))


#con una variante de format() simplificada

print (f"Nombre: \"{nombre}\" \nEdad: \t{edad}")

# print y el argumento end
print ("Solo hay 11 tipos de personas, los que entienden el chiste, los que no lo entienden y los que nunca lo entenderan",end=" ")
print("otra linea")

