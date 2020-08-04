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
vidas=7#amount of lives in the game
letras_correctas=0 #correct letter count


#this function allows showing the letters that have already been used
def administrarLetras():
    x=35
    y=75
    contador=0
    tk.Label(canvas, text="Letras usadas hasta el momento",font=("Helvetica",14),bg="yellow").place(x=25,y=50)
    for i in range(26):# create a possible position from 1 to 27 of the alphabetical order
        contador+=1
        letras_label[i].place(x=x,y=y)## positions the letter in the array
        x+=30
        if contador ==5:
            y+=35#positioning in and of the letter
            contador=0
            x=25#positioning of the letter
        
#botton actions     
def bottonFuntion():
    global vidas
    global letras_correctas
    #print(leerletra.get())
    letrasUsadas.append(leerletra.get())#get the letter to show it later
    print(letrasUsadas)
    letras_label[ord(leerletra.get())-97].config(text=leerletra.get())# letters typed por el usuario
    
    if leerletra.get() in palabra:#we read letters from the Entry
        if palabra.count(leerletra.get())>1:
            letras_correctas+=palabra.count(leerletra.get())
            for i in range(len(palabra)):
                if palabra[i]==leerletra.get():
                    dibujar_guiones[i].config(text=""+leerletra.get())
        else:
            letras_correctas+=1#verify that the letter entered is correct
            dibujar_guiones[palabra.index(leerletra.get())].config(text=""+leerletra.get())
        if letras_correctas==len(palabra):
            msg.showwarning(title="Felicidades", message="Haz ganado")
    else:
        vidas-=1#if the letter is wrong then a life is subtracted
        canvas.itemconfig(id_img,image=imagenes[vidas-1])
        if vidas==0:#when lives reach 0 a message is displayed on the screen
            msg.showerror(title="Perdiste", message="Haz utilizado tus 7 vidas")
            
            
app=tk.Tk()
archivo_palabras=open("palabras.txt","r")# reading the file containing the letters
palabras_lista=list(archivo_palabras.read().split("\n"))#read the words and use the line break as a separator
palabra=palabras_lista[randint(0,len(palabras_lista)-1)].lower()# in this game the letters are lowercase
leerletra=tk.StringVar()#read of the Entry

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
app.geometry("650x480")#create of canvas
canvas=tk.Canvas(app,width=600,#we create the canvas, with height and width
                  height=600, )


canvas.pack(expand=True,fill="both")#both allows the canvas to occupy the entire space of the geometry
#get the images of the hangman game
imagenes=[ImageTk.PhotoImage(file="1.png"),
          ImageTk.PhotoImage(file="2.png"),
          ImageTk.PhotoImage(file="3.png"),
          ImageTk.PhotoImage(file="4.png"),
          ImageTk.PhotoImage(file="5.png"),
          ImageTk.PhotoImage(file="6.png"),
          ImageTk.PhotoImage(file="7.png"),]
id_img=canvas.create_image(450,150, image=imagenes[6])

#we create a reference tag
tk.Label(canvas,
      text="Introduce una letra",
      font=("Verdana",15)).place(x=300,y=300)
#se crea la entrada de texto
letra= tk.Entry(canvas,width=1,
             font=("Verdana",18), 
             textvariable=leerletra).place(x=530,y=300)
#acction botton
botton =tk.Button(canvas,
                text="Comprobar",
                command=bottonFuntion).place(x=380,y=350)
#We create letter arrangement for used letters
letras_label=[tk.Label(canvas,
                    text="",
                    font=("Verdana",15)) for j in range(26)]
administrarLetras()
#we draw hyphens of the number of letters of the chosen word
dibujar_guiones=[tk.Label(canvas,text="_",
                 font=("Verdana",15)) for _ in palabra]
inicial=200
#position the word
for i in range(len(palabra)):
    dibujar_guiones[i].place(x=inicial, y=400)
    inicial+=50


app.mainloop()
