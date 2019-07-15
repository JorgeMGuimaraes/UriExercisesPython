# 1017

#entradas
tempoDeViagem           = int(input())
velocidadeMedia         = int(input())
#processos
consumo                 = 12
combustivelNecessario   = (tempoDeViagem * velocidadeMedia) / consumo
#saídas
print("{:.3f}".format(combustivelNecessario))