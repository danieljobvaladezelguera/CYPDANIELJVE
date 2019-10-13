#Problema 2.8

print("Programa para hacer descuentos dependiendo las compras")

PAGO = int(input("Cuanto es el valor de la compra?? "))

if PAGO < 500:
    print(f"Es en total {PAGO}")

elif PAGO <= 1000:
    print(f"Es en total {PAGO - PAGO*0.005}")

elif PAGO <= 7000:
    print(f"Es en total {PAGO - PAGO*0.11}")

elif PAGO <= 15000:
    print(f"Es en total {PAGO - PAGO*0.18}")

else:
    print(f"Es em total {PAGO - PAGO*0.25}")

print("Fin del programa")
        

    
 
