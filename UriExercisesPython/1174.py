#1174

maxIteracoes    = 100
a               = [0] * maxIteracoes
#processos
for i in range(maxIteracoes):
    a[i] = float(input())
    if a[i] <= 10:
        print("A[" + str(i) + "] = " + "{:.1f}".format(a[i]))
