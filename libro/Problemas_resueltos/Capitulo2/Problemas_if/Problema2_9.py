#Programa 2.9

print("Programa para saber pagar impuestos")

COSTO = float(input("Deme el costo del artículo: "))

IMP = 0
NIMP = 0

if COSTO > 500:
    IMP = 20*0.30+((COSTO-40)*0.50)
    NIMP = IMP + COSTO
    print(f"El valor del producto con el impuesto es de {NIMP}")

elif COSTO > 40:
    IMP = 20*0.30+((COSTO-40)*0.40)
    NIMP = IMP + COSTO
    print(f"El valor del producto con el impuesto es de {NIMP}")

elif COSTO > 20:
    IMP = (COSTO-20)*(0.30)
    NIMP = IMP + COSTO
    print(f"El valor del producto con el impuesto es de {NIMP}")

else:
    print(f"El valor del producto con el impuesto es de {IMP + COSTO}")


