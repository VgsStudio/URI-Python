N1, N2, N3, N4 = map(float, input().split())

Med = (2*N1 + 3*N2 + 4*N3 + N4)/10

if Med >= 7:
    print("Media: %.1f" % Med)
    print("Aluno aprovado.")
    
elif Med < 7 and Med >= 5:
    exame = float(input())
    print("Media: %.1f" % Med)
    print("Aluno em exame.")
    print("Nota do exame: %.1f" % exame)
    Med = (Med + exame)/2
    if Med >= 5:
        print("Aluno aprovado.")
    
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % Med)
    
else:
    print("Media: %.1f" % Med)
    print("Aluno reprovado.")