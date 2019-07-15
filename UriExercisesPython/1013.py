# 1013

# subs
def maior(a, b):
    return int((a + b + abs(a - b)) / 2)

#entrada
a, b, c     = map(int, input().split())
#processo
maiorNumero = maior(maior(a, b), c)
print(maiorNumero, "eh o maior")