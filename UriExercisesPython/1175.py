# 1175
maxInteracoes   = 20
#entradas
n               = [0] * maxInteracoes
#processos
for i in range(maxInteracoes - 1, -1, -1): n[i] = int(input())
for i in range(maxInteracoes): print("N[%d] = %d"%(i, n[i]))