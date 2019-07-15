# 1012

#entradas
A, B, C     = map(float, input().split())
#processamento dos dados
pi          = 3.14159
trinagulo   = float(A * C / 2)
circulo     = float(pi * C ** 2)
trapezio    = float((A + B) * C / 2)
quadrado    = float(B ** 2)
retangulo   = float(A * B)
#saída
print("TRIANGULO:", "{:.3f}".format(trinagulo))
print("CIRCULO:", "{:.3f}".format(circulo))
print("TRAPEZIO:", "{:.3f}".format(trapezio))
print("QUADRADO:", "{:.3f}".format(quadrado))
print("RETANGULO:", "{:.3f}".format(retangulo))