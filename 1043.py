A, B, C = map(float, input().split())

LADOS = []

for x in [A, B, C]:
    LADOS.append(x)
    
LADOS = sorted(LADOS)

if (LADOS[0] + LADOS[1])<=(LADOS[2]):
    AREA = (A+B)*C/2
    print("Area = %.1f" % AREA)
else:
    PERI = A + B + C
    print("Perimetro = %.1f" %PERI)