#Escribir un programa que pida al usuario dos n�meros y muestre por pantalla su divisi�n. Si el divisor es cero el programa debe mostrar un error.

num = float(input("Introduce el primer numero "))
num2 = float(input("Introduce el segundo numero "))
if num2 == 0:
    print("�Error! division entre 0.")
else:
    print(num/num2)