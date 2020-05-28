#Given a list of strings delete all special chars in each one (non-alphanumeric chars).

import re 

frase=input("Enter the string: ")

 
#la funcion list crea una lista que consta de los elementos iterable por ejemplo hola = h,o,l,a
valores = list([letra for letra in frase 
               if letra.isalpha() or letra.isnumeric()]) 
               #isisalpha() verifica si es una letra
               #isnumeric() verifica que es un numero
  
r = "".join(valores)# La función join convierte una lista en una cadena formada por los elementos de la lista separados por comas,
#por lo cual une todas las variables antes separadas con list
  

print ("final string", r) 