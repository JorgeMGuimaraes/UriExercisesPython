# 1022

# Subs

def simplificar(num, den):
    num = abs(num)
    den = abs(den)
    i   = 2
    mdc = 1
    while i <= min(num, den):
        if num % i == 0 and den % i == 0:
            mdc *= i
            num /= i
            den /= i
        else:
            i   += 1
    return mdc

def imprimirTDARacional(num, den):
    divComum = simplificar(num, den)
    print("%d/%d = %d/%d"%(num, den, num / divComum, den / divComum))
    return None

def soma(num1, den1, num2, den2):
    numInicial = (num1 * den2) + (num2 * den1)
    denInicial = den1 * den2
    imprimirTDARacional(numInicial, denInicial)
    return None

def subtracao(num1, den1, num2, den2):
    numInicial = (num1 * den2) - (num2 * den1)
    denInicial = den1 * den2
    imprimirTDARacional(numInicial, denInicial)
    return None

def multiplicacao(num1, den1, num2, den2):
    numInicial = num1 * num2
    denInicial = den1 * den2
    imprimirTDARacional(numInicial, denInicial)
    return None

def divisao(num1, den1, num2, den2):
    numInicial = num1 * den2
    denInicial = num2 * den1
    imprimirTDARacional(numInicial, denInicial)
    return None

# Main
casos = int(input())
for i in range(casos):
    n1, div1, d1, operador, n2, div2, d2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    d1 = int(d1)
    d2 = int(d2)
    if operador == "+"      : soma(n1, d1, n2, d2)
    elif operador == "-"    : subtracao(n1, d1, n2, d2)
    elif operador == "*"    : multiplicacao(n1, d1, n2, d2)
    elif operador == "/"    : divisao(n1, d1, n2, d2)