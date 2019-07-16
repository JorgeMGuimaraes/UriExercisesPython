# 1176
totalDeCasos = 61
#entradas
casosDeTeste        = int(input())
#processos
serieDeFibonacci    = [0] * totalDeCasos
serieDeFibonacci[0] = 0
serieDeFibonacci[1] = 1
for i in range(2, totalDeCasos):
        serieDeFibonacci[i] = serieDeFibonacci[i - 1] + serieDeFibonacci[i -2]

for i in range(casosDeTeste):
    caso = int(input())
    print("Fib(%d) = %d" %(caso, serieDeFibonacci[caso]))