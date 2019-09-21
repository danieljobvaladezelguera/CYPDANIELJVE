#problema 1.5
print ("Programa para sacar area y volumen de un cilindro")

RADIO = float(input("Dame el radio")) 
ALTU = float(input("Dame la altura"))
π = 3.1415

VOL = π * (RADIO **2) * ALTU
AREA = 2 * π * RADIO * ALTU

print ("El volumen es de",( VOL ))
print ("El area es de",( AREA ))
