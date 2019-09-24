NUM1 = int(input("Dame el primer numero: "))
NUM2 = int(input("Dame el segundo numero: "))
NUM3 = int(input("Dame el tercer numero: "))

if NUM1 > NUM2 and NUM2 > NUM3:
    print(f"El orden de mayor a menor es { NUM1 }, { NUM2 } y { NUM3 }")
if NUM3 > NUM2 and NUM2 > NUM1:
    print(f"El orden de mayor a menor es {NUM3}, {NUM2} y {NUM1}")
if NUM1 > NUM3 and NUM3 > NUM2:
    print(f"El orden de mayor a menor es {NUM1}, {NUM3} y {NUM2}")
if NUM2 > NUM1 and NUM1 > NUM3:
    print(f"El orden de mayor a menor es {NUM2}, {NUM1} y {NUM3}")
if NUM3 > NUM1 and NUM1 > NUM2:
    print(f"El orden de mayor a menor es {NUM3}, {NUM1} y {NUM2}")
if NUM2 > NUM3 and NUM3 > NUM1:
    print(f"El orden de mayor a menor es {NUM2}, {NUM3} y {NUM1}")
print("fin del programa")

