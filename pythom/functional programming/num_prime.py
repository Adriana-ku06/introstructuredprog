import math
 
def es_primo(numero):#funcion para saber si un numero es primo o no
    if (numero<=1):
        return False
 #un numero primo solo puede ser divisible entre uno y si mismo
    for i in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return False
    return True
 
while True:
    
        numero = int(input("Ingrese un numero"))
        if numero==0:
            break #permite salir del programa
        if es_primo(numero):
            print ("\nEl numero %s es primo" % numero)
        else:
            print ("\nEl numero %s no es primo" % numero)
   