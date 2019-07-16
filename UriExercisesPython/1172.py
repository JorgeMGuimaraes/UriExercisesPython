# 1172
x           = [0] * 10
#processos
for i in range(10):
    entrada = int(input()) 
    x[i]    = entrada if entrada > 0 else 1
    print("X[%d] = %d"%(i, x[i]))
