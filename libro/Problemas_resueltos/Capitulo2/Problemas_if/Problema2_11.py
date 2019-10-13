#Problema 2.11

print("Programa para saber costos de llamadas")

CLAVE = int(input("Dame la clave de teléfono: "))
COSTO = int(input("Dame los minutos que hablarás: "))
NCOS = 0

if CLAVE == 12:
    NCOS = COSTO * 2
    print(f"el costo por llamada a A.Norte es de ${NCOS}")

if CLAVE == 15:
    NCOS = COSTO *2.2
    print(f"El costo por llamada a A.Central es de ${NCOS}")

if CLAVE == 18:
    NCOS = COSTO *4.5
    print(f"El costo por llamada a A.del Sur es de ${NCOS}")

if CLAVE == 19:
    NCOS = COSTO *3.5
    print(f"El costo por llamada a Europa es de ${NCOS}")

if CLAVE == 23:
    NCOS = COSTO *6
    print(f"El costo por llamada a Asia es de ${NCOS}")

if CLAVE == 25:
    NCOS = COSTO *6
    print(f"El costo por llamada a Africa es de ${NCOS}")

if CLAVE == 29:
    NCOS = COSTO *5
    print(f"El costo por llamada a Oceania es de ${NCOS}")

print("Fin del programa")
