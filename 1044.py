A, B = map(int, input().split())

LISTA = [ ]

for x in [A, B]:
    LISTA.append(x)
    
LISTA = sorted(LISTA)

if LISTA[1]%LISTA[0] == 0:
    print("Sao Multiplos")
    
else:
    print("Nao sao Multiplos")

