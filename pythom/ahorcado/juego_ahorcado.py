# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:21:10 2020

@author: Adriana
"""

import tkinter as tk
from random import randint
import tkinter.messagebox as msg
from PIL import ImageTk


letrasUsadas=[]
vidas=7#numero de vidas en el juego
letras_correctas=0 #coonteo de letras correctas


#esta funcion permite mostrar las letras que ya han sido utilizadas
def administrarLetras():
    x=35
    y=75
    contador=0
    tk.Label(canvas, text="Letras usadas hasta el momento",font=("Helvetica",14),bg="yellow").place(x=25,y=50)
    for i in range(26):# crea una posicion posible de 1 a 27 del ordel alfabetico
        contador+=1
        letras_label[i].place(x=x,y=y)##posiciona la letra en el arreglo
        x+=30
        if contador ==5:
            y+=35#posicionamiento en y de la letra
            contador=0
            x=25#posicionamento de de la letra
        
 #acciones del botton       
def bottonFuntion():
    global vidas
    global letras_correctas
    #print(leerletra.get())
    letrasUsadas.append(leerletra.get())#obtenemos la letra para mostrala mas adelante
    print(letrasUsadas)
    letras_label[ord(leerletra.get())-97].config(text=leerletra.get())# letras tecleadas por el usuario
    
    if leerletra.get() in palabra:#leemos letras desde el Entry
        if palabra.count(leerletra.get())>1:
            letras_correctas+=palabra.count(leerletra.get())
            for i in range(len(palabra)):
                if palabra[i]==leerletra.get():
                    dibujar_guiones[i].config(text=""+leerletra.get())
        else:
            letras_correctas+=1#verificamos que la letra introducida sea correcta
            dibujar_guiones[palabra.index(leerletra.get())].config(text=""+leerletra.get())
        if letras_correctas==len(palabra):
            msg.showwarning(title="Felicidades", message="Haz ganado")
    else:
        vidas-=1#si la letra es incorrecta entonces se resta una vida
        canvas.itemconfig(id_img,image=imagenes[vidas-1])
        if vidas==0:#cuando las vidas lleguen a 0 se muestra un msj en pantalla
            msg.showerror(title="Perdiste", message="Haz utilizado tus 7 vidas")
            
            
app=tk.Tk()
archivo_palabras=open("palabras.txt","r")# lectura del archivo que contiene las letras
palabras_lista=list(archivo_palabras.read().split("\n"))#leermos las palabras y usamos el salto de linea como separador
palabra=palabras_lista[randint(0,len(palabras_lista)-1)].lower()# en este juego las letras son en minuscula 

leerletra=tk.StringVar()#leemos letra del Entry

app.config(width=400,
           height=600, 
           relief="raised")
          

#juego_frame=Frame(app)
#juego_frame.config(width=1000,
#                   height=600,
#                   relief="sunken", 
#                   bd=15)
#juego_frame.grid_propagate(False)
#juego_frame.pack()
app.geometry("650x480")#creamos contenedor del canvas
canvas=tk.Canvas(app,width=600,#creamos el cambas, con altura u anchura
                  height=600, )


canvas.pack(expand=True,fill="both")#both permite que el canvas ocupe todo el espacio del geometry
#obtenemos las imagenes del juego de ahorcado
imagenes=[ImageTk.PhotoImage(file="1.png"),
          ImageTk.PhotoImage(file="2.png"),
          ImageTk.PhotoImage(file="3.png"),
          ImageTk.PhotoImage(file="4.png"),
          ImageTk.PhotoImage(file="5.png"),
          ImageTk.PhotoImage(file="6.png"),
          ImageTk.PhotoImage(file="7.png"),]
id_img=canvas.create_image(450,150, image=imagenes[6])

#creamosuna etiqueta de referencia
tk.Label(canvas,
      text="Introduce una letra",
      font=("Verdana",15)).place(x=300,y=300)
#se crea la entrada de texto
letra= tk.Entry(canvas,width=1,
             font=("Verdana",18), 
             textvariable=leerletra).place(x=530,y=300)
#accion botton
botton =tk.Button(canvas,
                text="Comprobar",
                command=bottonFuntion).place(x=380,y=350)

#creamos arreclo de letras para letras usadas
letras_label=[tk.Label(canvas,
                    text="",
                    font=("Verdana",15)) for j in range(26)]
administrarLetras()

#dibujamos guiones del numero de letras de la alabra elegida
dibujar_guiones=[tk.Label(canvas,text="_",
                 font=("Verdana",15)) for _ in palabra]
inicial=200
#posicionamos la palabra
for i in range(len(palabra)):
    dibujar_guiones[i].place(x=inicial, y=400)
    inicial+=50


app.mainloop()
