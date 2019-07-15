# 1015

#entrada
x1, y1      = map(float, input().split())
x2, y2      = map(float, input().split())
#processo dos dados
distancia   = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)
#saida
print("{:.4f}".format(distancia))