# Funciones en python

print("Funciones")

def sumar ( x , y ):
    z = x + y
    return z

def restar (  x , y ):
    return x - y

"""
def mi_print( texto ):
    print(f"Este es mi primer print: {texto}")

def multiplica(valor, veces):
    if valor == None:
        print('Nada que imprimir, pon algo')

    else :
        print( valor*veces)
"""

def comanda (mesa , comensal , entrada , medio , fuerte , postre="Gela de limon" ):
    print(f"mesa: {mesa} comensal: {comensal}")
    print(f"\t Entrada: { entrada } ")
    print(f"\t Segundo tiempo: { medio } ")
    print(f"\t Plato fuerte: {fuerte} ")
    print(f"\t Postre: {postre } ")



comanda(2, 1, "Ensalada", "Sopa de rana", "Filete de Oso", )
print()
comanda(mesa="1", comensal="2", entrada="Ensalada", medio="Sopa de rana", fuerte="Filete de pompi de sirena", postre="Flan")

def comanda2(**comida):
    llaves = comida.keys()
    for elem in llaves:
        print(elem, "->", comida[elem])
        


def imprime_argumentos(*argumentos):
    for index in range( len(argumentos)):
        print(argumentos[index])

imprime_argumentos('hola', True, 3.1416, 1000, {'id': 'sc01', 'nombre' : 'juan'} )
imprime_argumentos()
comanda2(mesa="1", comensal="2", entrada="Ensalada", medio="Sopa de rana", fuerte="Filete de pompi de sirena", postre="Flan")


