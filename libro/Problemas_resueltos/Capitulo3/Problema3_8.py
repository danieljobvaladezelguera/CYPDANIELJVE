#Problema 3.8

print("Conjetura de ULAM")
print("Dame un numero y te lo podre dividir hasta llegar a 1")

NUM = int(input("Dame un numero: "))

if NUM > 0:

    while NUM != 1:
        print(NUM)

        if ((-1)**(NUM)) > 0:
            NUM = (NUM) / (2)

        else:
            NUM = ((NUM)*(3)) + 1

    else:
        print(NUM)
        
else:
    print("Dame un numero positivo")
