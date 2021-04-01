N = int(input())

MULT = 1
x = 2

while x<=10000:
    div = x%(N*MULT)
    if x == MULT:
        MULT += 1
    if div ==2:
        print(x)
    x += 1 
    
