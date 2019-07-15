# 1010

cod, peca1Quantidade, peca1Valor = map(float, input().split())
cod, peca2Quantidade, peca2Valor = map(float, input().split())
#processamento dos dados
valorPago = (peca1Valor * peca1Quantidade) + (peca2Valor * peca2Quantidade)
#saídas
print("VALOR A PAGAR: R$", "{:.2f}".format(valorPago))