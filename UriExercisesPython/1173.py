# 1173
#constantes
totalDeValores = 10
#entradas
valor = int(input())
#processos
ordenadosEmDobro = [valor] * totalDeValores
print("N[%d] = %d"%(0, ordenadosEmDobro[0]))
for i in range(1, len(ordenadosEmDobro)):
    ordenadosEmDobro[i] = ordenadosEmDobro[i - 1] * 2
    print("N[%d] = %d"%(i, ordenadosEmDobro[i]))
