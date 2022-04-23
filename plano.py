"""Programa 8: 
Cuadrantes del plano"""

#input
X = int(input("Digite el valor de X: "))
Y = int(input("Digite el valor de Y: "))

#processing
if X > 0:
    A = 1
else:
    A = 0
if Y > 0:
    B = 1
else:
    B = 0
if A == 1 and B == 1:
    msj = "Esta en el cuadrante No. 1"
if A == 1 and B == 0:
    msj = "Esta en el cuadrante No. 4"
if A == 0 and B == 1:
    msj = "Esta en el cuadrante No. 2"
if A == 0 and B == 0:
    msj = "Esta en el cuadrante No. 3"

if X == 0 and Y == 0:
    msj = "Se encuentra en el origen"

if X == 0 and Y > 0:
    msj = "Esta posicionado sobre el eje Y"

if Y == 0 and X > 0:
    msj = "Esta posicionado sobre el eje X"


#output
print(msj)