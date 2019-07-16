# 1177
maxIteracoes = 1000
#entradas
t = int(input())
#processos
n = [0] * maxIteracoes
for i in range(maxIteracoes):
    n[i] = i % t
    print("N[%d] = %d"%(i, n[i]))
