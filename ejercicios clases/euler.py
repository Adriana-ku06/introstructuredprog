#. Calculate the Euler constant e using the series
def fact(n):# obtenemos el factorial del numero
    if n == 0:
        r = 1
    else:
        r = n * fact(n - 1)
    return r


num=int(input("Enter the number of terms: "))
sum1=1


for i in range(1,num+1):
    sum1=sum1+(1/fact(i))
print("The eulers is",round(sum1,4))# controla el numero de nigitos que quieres que se vean