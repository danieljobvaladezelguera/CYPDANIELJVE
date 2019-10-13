#Problema 2.12

print("Programa para calcular el pago según horas trabajadas")

SUE = int(input("Dame el sueldo que ganas x hora: "))
CATE = int(input("Dime que categoría eres x empleado: "))
HE = int(input("Dime cuantas horas trabajaste extras: "))

PHE = 0
NSUE = 0

if CATE == 1:
    PHE = 30
    if HE > 30:
            NSUE = SUE + (30*PHE)
            print(f"tu nuevo salario es de ${NSUE}")
    else:
        NSUE  = SUE + (HE*PHE)
        print(f"Tu nuevo salario es de ${NSUE}")
        
if CATE == 2:
    PHE = 38
    if HE > 30:
            NSUE = SUE + (30*PHE)
            print(f"tu nuevo salario es de ${NSUE}")
    else:
        NSUE  = SUE + (HE*PHE)
        print(f"Tu nuevo salario es de ${NSUE}")
    
if CATE == 3:
    PHE = 50
    if HE > 30:
            NSUE = SUE + (30*PHE)
            print(f"tu nuevo salario es de ${NSUE}")
    else:
        NSUE  = SUE + (HE*PHE)
        print(f"Tu nuevo salario es de ${NSUE}")
    
if CATE == 4:
    PHE = 70
    if HE > 30:
            NSUE = SUE + (30*PHE)
            print(f"tu nuevo salario es de ${NSUE}")
    else:
        NSUE  = SUE + (HE*PHE)
        print(f"Tu nuevo salario es de ${NSUE}")
    
if  PHE == 0:
    if HE > 30:
            NSUE = SUE + (30*PHE)
            print(f"tu nuevo salario es de ${NSUE}")
    else:
        NSUE  = SUE + (HE*PHE)
        print(f"Tu nuevo salario es de ${NSUE}")
print("Fin del programa")
