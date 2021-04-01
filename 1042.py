x, y, z = map(int, input().split())

LISTA = [ ]
novaLISTA = [ ]
var = [x, y, z]

for x in var:
    LISTA.append(x)

novaLISTA = sorted(LISTA)

for x in [0,1,2]:
    print(novaLISTA[x])

print("")

for x in [0,1,2]:
    print(LISTA[x])
