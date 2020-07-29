# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:35:29 2020

@author: Adriana
"""
import matplotlib.pyplot as plt

#ejemplos de definicion de funciones
def f1(x):
    return 2*(x**2) + 5*x - 8

def f2(x):
    return 4*x + 5
# Valores del eje X que toma el gráfico.
x = range(-10, 15)
# Graficar ambas funciones.
plt.plot(x, [f1(i) for i in x])
plt.plot(x, [f2(i) for i in x])
# Establecer el color de los ejes.
plt.axhline(0, color="black")
plt.axvline(0, color="black")
# Limitar los valores de los ejes.
plt.xlim(-10, 10)
plt.ylim(-10, 10)
# Guardar gráfico como imágen PNG.
plt.savefig("output.png")
# Mostrarlo.
