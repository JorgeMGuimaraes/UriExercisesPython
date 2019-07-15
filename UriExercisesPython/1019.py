# 1019

#constatntes
segundosEmUmaHora   = 60 * 60
SegundosEmUmMinuto  = 60
#entradas
totalDeSengundos    = int(input())
#processos
horas               = int(totalDeSengundos / segundosEmUmaHora)
segundosRestantes   = totalDeSengundos % segundosEmUmaHora
minutos             = int(segundosRestantes / SegundosEmUmMinuto) if(segundosRestantes != 0) else 0
segundos            =  segundosRestantes % SegundosEmUmMinuto
#saídas
print(horas, ":", minutos, ":", segundos, sep="")