#Escribir un programa que pida al usuario un n�mero entero positivo y muestre por pantalla todos los n�meros impares desde 1 hasta ese n�mero separados por comas.

num = int(input("Introduce un n�mero entero positivo: "))
for i in range(1, num+1, 2):
    print(i, end=", ")