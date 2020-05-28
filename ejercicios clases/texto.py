#4. Count the Word Frequency in a Text (Unique String). Don't forget to: normalize to
#lower case and delete special chars.

import re
#cadena = 'i2t was the best of times it was the worst of times *?/'
cadena=input("Enter the string: ")
#cadenaPalabras += 'it was the age of wisdom it was the age of foolishness'
cadenaPalabras = re.sub('[^a-zA-Z \n\.]', '', cadena) 
# dejamos solo las letras con sub
listaPalabras = cadenaPalabras.split()
#convierte una lista en una cadena formada por los elementos de la lista separados por comas

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))
    #.count Divide una cadena en una lista donde cada palabra es un elemento de la lista
     #.append agrega los valores a nueva lista
    

print("Cadena\n" + cadenaPalabras +"\n")


print("Palabras\n" + str(list(zip(listaPalabras, frecuenciaPalab))))
# zip toma como argumento dos o más objetos iterables ( y retorna un nuevo iterable en este caso el numero de palabras repetidas
#list ordenada un conjunto
#str une las listas y las imprime

