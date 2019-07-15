# 1020

#constantes
diasNoAno       = 365
diasNoMes       = 30
#entradas
idadeEmDias     = int(input())
#processos
anos            = int(idadeEmDias / diasNoAno)
idadeRestante   = (idadeEmDias % diasNoAno) if(anos != 0) else idadeEmDias
meses           = int(idadeRestante // diasNoMes)
dias            = int(idadeRestante % diasNoMes) if(meses != 0) else idadeRestante
#saída
print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")