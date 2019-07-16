# 1179
pares               = []
impares             = []
totalDeIteracoes    = 15
# entradas

# processos
for i in range(totalDeIteracoes):
    entrada = int(input())
    if entrada % 2 == 0:
        pares.append(entrada)
        if len(pares) == 5:
            for i in range(len(pares)):
                print("par[%d] = %d"%(i, pares[i]))
            pares.clear()
    else:
        impares.append(entrada)
        if len(impares) == 5:
            for i in range(len(impares)):
                print("impar[%d] = %d"%(i, impares[i]))
            impares.clear()
for i in range(len(impares)):
    print("impar[%d] = %d"%(i, impares[i]))
for i in range(len(pares)):
    print("par[%d] = %d"%(i, pares[i]))
