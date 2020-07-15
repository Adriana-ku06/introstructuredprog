#operaciones con numeros
def crear_funcion(operador): #funcion que permite crear nuevas funciones depediendo del operado enviado
    if operador == '+':#suma
        def suma(num1=0, num2=0):
            return num1 + num2
        return suma
    if operador == '-': #resta
        def resta(num1=0, num2=0):
            return num1 - num2
        return resta
    if operador == '*': #multiplicacion
        def multiplicacion(num1=0, num2=0):
            return num1 * num2
        return multiplicacion

      

def operacion(funcion, num1=0, num2=0):
    return funcion(num1, num2)

funcion = crear_funcion('*')
resultado = operacion(funcion, 10, 20)#mandamos el operado a funcion
print(resultado)