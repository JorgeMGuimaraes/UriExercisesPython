# 2310

#main
dados       = [0] * 6
jogadores   = int(input())
for i in range(jogadores):
    n = input()
    s, b, a = map(int, input().split())
    dados[0] += s
    dados[1] += b
    dados[2] += a
    s, b, a = map(int, input().split())
    dados[3] += s
    dados[4] += b
    dados[5] += a

print("Pontos de Saque: %.2f %%.\nPontos de Bloqueio: %.2f %%.\nPontos de Ataque: %.2f %%."%(100 * dados[3] / dados[0], 100 * dados[4] / dados[1], 100 * dados[5] / dados[2]))