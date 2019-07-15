# 1009

comissao        = 0.15
#get inputs
nome            = input()
salarioFixo     = float(input())
totalDeVendas   = float(input())
#process data
totalAReceber   = salarioFixo + (totalDeVendas * comissao)
#output
print("TOTAL = R$", "{:.2f}".format(totalAReceber))