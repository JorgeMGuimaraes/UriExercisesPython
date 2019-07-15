# 1021

#entrada
N = float(input())
#processos
#N (0 ≤ N ≤ 1000000.00)
if (0 <= N <= 1000000.00):
    notas100 = int(N / 100)
    resto   = N % 100
    notas50 = int(resto / 50)
    resto   = resto % 50
    notas20 = int(resto / 20)
    resto   = resto % 20
    notas10 = int(resto / 10)
    resto   = resto % 10
    nota5 = int(resto / 5)
    resto   = resto % 5
    nota2 = int(resto / 2)
    resto   = (resto % 2) * 100
    moedas100 = int(resto / 100)
    resto   = resto % 100
    moedas50 = int(resto / 50)
    resto   = resto % 50
    moedas25 = int(resto / 25)
    resto   = resto % 25
    moedas10 = int(resto / 10)
    resto   = resto % 10
    moedas5 = int(resto / 5)
    resto   = resto % 5
    moedas1 = int(resto)
    #saídas	
    print("NOTAS:")
    print(notas100, "nota(s) de R$ 100.00")
    print(notas50, "nota(s) de R$ 50.00")
    print(notas20, "nota(s) de R$ 20.00")
    print(notas10, "nota(s) de R$ 10.00")
    print(nota5, "nota(s) de R$ 5.00")
    print(nota2, "nota(s) de R$ 2.00")
    print("MOEDAS:")
    print(moedas100, "moeda(s) de R$ 1.00")
    print(moedas50, "moeda(s) de R$ 0.50")
    print(moedas25, "moeda(s) de R$ 0.25")
    print(moedas10, "moeda(s) de R$ 0.10")
    print(moedas5, "moeda(s) de R$ 0.05")
    print(moedas1, "moeda(s) de R$ 0.01")
