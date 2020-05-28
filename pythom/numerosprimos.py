#numeros primos del 1 al 200
cont = 0
for i in range(200):
    primos = True
    for j in range(2,11):
        if i == j:
           break
        elif i%j == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(' ',i, end='')
        cont += 1
print("\n Números primos {}".format( cont) )