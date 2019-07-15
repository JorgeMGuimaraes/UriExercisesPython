# 1014

#entradas
distancia           = int(input())
combustivelGasto    = float(input())
#processos
consumoMedio        = float(distancia / combustivelGasto) 
#saída
print("{:.3f}".format(consumoMedio), "km/l")