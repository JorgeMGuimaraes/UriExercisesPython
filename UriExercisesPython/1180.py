# 1180
numeroDeElementos   = int(input())
elementos           = list(map(int, input().split()))
#processos
menorValor  = 999
posicao     = 0
for i in range(numeroDeElementos):
    if elementos[i] < menorValor:
        menorValor  = elementos[i]
        posicao     = i
#saidas
print("Menor valor:", menorValor)
print("Posicao:", posicao)