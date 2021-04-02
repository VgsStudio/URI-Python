#Principal
A, B, C = map(float, input().split())


LADOS = []
    
for x in [A, B, C]:
    LADOS.append(x)
        
        
LADOS = sorted(LADOS, reverse = True)
    
A =  LADOS[0]
B =  LADOS[1]
C =  LADOS[2]

if A >= (B + C): #Será que da pra fazer com menos if?
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    elif A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
        
    elif A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")

    if A == (B and C):
        print("TRIANGULO EQUILATERO")
        
    elif (A == (B or C)) or (B == C):
        print("TRIANGULO ISOSCELES")