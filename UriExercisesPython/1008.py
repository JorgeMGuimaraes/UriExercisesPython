# 1008

#get inputs
idDoFuncionario     = int(input())
horasTrabalhadas    = int(input())
valorPorHora        = float(input())
#process data
salary              = horasTrabalhadas * valorPorHora
#output
print("NUMBER =", idDoFuncionario)
print("SALARY = U$", "{:.2f}".format(salary))