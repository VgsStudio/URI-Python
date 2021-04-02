I, F = map(int, input().split())

if F-I > 0:
    tempo = F-I
    print("O JOGO DUROU %i HORA(S)" % tempo)
    
else:
    tempo = 24 -I + F
    print("O JOGO DUROU %i HORA(S)" % tempo)
