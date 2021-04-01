num, quant = map(int, input().split())

LANCHES = [0, 4, 4.5, 5, 2, 1.5]

total = LANCHES[num]*quant

print("Total: R$ %.2f" % total)
