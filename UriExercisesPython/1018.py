# 1018

#constantes
#entradas
valorTotal = int(input())
#processos
notaDeCem       = int(valorTotal / 100)
valorRestante   = valorTotal % 100
notaDeCinquenta = int( valorRestante / 50)
valorRestante   %= 50
NotaDeVinte     = int( valorRestante / 20)
valorRestante   %= 20
NotaDeDez       = int( valorRestante / 10)
valorRestante   %= 10
NotaDeCinco     = int( valorRestante / 5)
valorRestante   %= 5
NotaDeDois      = int( valorRestante / 2)
valorRestante   %= 2
NotaDeUm        = valorRestante
#saídas
print(valorTotal)
print(notaDeCem, "nota(s) de R$ 100,00")
print(notaDeCinquenta, "nota(s) de R$ 50,00")
print(NotaDeVinte, "nota(s) de R$ 20,00")
print(NotaDeDez, "nota(s) de R$ 10,00")
print(NotaDeCinco, "nota(s) de R$ 5,00")
print(NotaDeDois, "nota(s) de R$ 2,00")
print(NotaDeUm, "nota(s) de R$ 1,00")