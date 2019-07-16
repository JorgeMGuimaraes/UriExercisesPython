# 2547


while True:
  try:
    entrada = input()
    while entrada != "":
        visitantes, altMin, altMax  = map(int, entrada.split())
        total                       = 0
        for i in range(visitantes):
            altVis = int(input())
            if altMin <= altVis <= altMax: total += 1
        print(total)
        entrada = input()
  except EOFError:
    break