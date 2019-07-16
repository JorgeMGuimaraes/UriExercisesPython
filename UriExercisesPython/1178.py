# 1178
maxIteracoes    = 100
#entradas
x               = float(input())
#processos
n               = [x] * maxIteracoes
print("N[", 0, "] = ", "{:.4f}".format(n[0]), sep="")
for i in range(1, maxIteracoes):
    n[i] = n[i -1] / 2
    print("N[", i, "] = ", "{:.4f}".format(n[i]), sep="")