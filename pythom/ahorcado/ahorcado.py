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
vidas=7
letras_correctas=0


def administrarLetras():
    x=35
    y=75
    contador=0
    tk.Label(canvas, text="Letras disponibles",font=("Helvetica",14),bg="yellow").place(x=25,y=50)
    for i in range(26):
        contador+=1
        letras_label[i].place(x=x,y=y)
        x+=30
        if contador ==5:
            y+=35
            contador=0
            x=25
        
        
def bottonFuntion():
    global vidas
    global letras_correctas
    #print(leerletra.get())
    letrasUsadas.append(leerletra.get())
    print(letrasUsadas)
    letras_label[ord(leerletra.get())-97].config(text="")
    
    if leerletra.get() in palabra:
        if palabra.count(leerletra.get())>1:
            letras_correctas+=palabra.count(leerletra.get())
            for i in range(len(palabra)):
                if palabra[i]==leerletra.get():
                    dibujar_guiones[i].config(text=""+leerletra.get())
        else:
            letras_correctas+=1
            dibujar_guiones[palabra.index(leerletra.get())].config(text=""+leerletra.get())
        if letras_correctas==len(palabra):
            msg.showwarning(title="Felicidades", message="Haz ganado")
    else:
        vidas-=1
        canvas.itemconfig(id_img,image=imagenes[vidas-1])
        if vidas==0:
            msg.showerror(title="Perdiste", message="Haz utilizado tus 7 vidas")
app=tk.Tk()
archivo_palabras=open("palabras.txt","r")
palabras_lista=list(archivo_palabras.read().split("\n"))
palabra=palabras_lista[randint(0,len(palabras_lista)-1)].lower()

leerletra=tk.StringVar()

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
app.geometry("650x480")
canvas=tk.Canvas(app,width=600,
                  height=600, )
canvas.pack(expand=True,fill="both")

imagenes=[ImageTk.PhotoImage(file="1.png"),
          ImageTk.PhotoImage(file="2.png"),
          ImageTk.PhotoImage(file="3.png"),
          ImageTk.PhotoImage(file="4.png"),
          ImageTk.PhotoImage(file="5.png"),
          ImageTk.PhotoImage(file="6.png"),
          ImageTk.PhotoImage(file="7.png"),]
id_img=canvas.create_image(450,150, image=imagenes[6])


tk.Label(canvas,
      text="Introduce una letra",
      font=("Verdana",15)).place(x=300,y=300)

letra= tk.Entry(canvas,width=1,
             font=("Verdana",18), 
             textvariable=leerletra).place(x=530,y=300)

botton =tk.Button(canvas,
                text="Comprobar",
                command=bottonFuntion).place(x=380,y=350)


letras_label=[tk.Label(canvas,
                    text=chr(j+97),
                    font=("Verdana",15),bg="white") for j in range(26)]
administrarLetras()

dibujar_guiones=[tk.Label(canvas,text="_",
                 font=("Verdana",15)) for _ in palabra]
inicial=200

for i in range(len(palabra)):
    dibujar_guiones[i].place(x=inicial, y=400)
    inicial+=50


app.mainloop()
