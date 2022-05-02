#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


from cProfile import label
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]


def ej1():
    # Line Plot
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = list(range(-10, 11, 1))

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    y3 = [i**4 for i in x]
    
    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos
    fig = plt.figure()
    fig.suptitle('EJ 1', c='forestgreen')

    ax1 = fig.add_subplot(3, 1, 1)
    ax2 = fig.add_subplot(3, 1, 2)
    ax3 = fig.add_subplot(3, 1, 3)

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    ax1.plot(y1, c='b', label='y = x^2')
    ax2.plot(y2, c='g', label='y = x^3')
    ax3.plot(y3, c='r', label='y = x^4')
    
    # Cada gráfico realizarlo con un color distinto
    # a su elección
       
    ax1.legend()
    ax2.legend()
    ax3.legend()

    ax1.grid()
    ax2.grid()
    ax3.grid()

    mplcursors.cursor()
    plt.show()


def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    x = np.arange(0, 4*np.pi, 0.1)

    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    y1 = [np.sin(i) for i in x]
    y2 = [np.cos(i) for i in x]
    
    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos
    fig = plt.figure()
    fig.suptitle('EJ 2: SCATTER PLOT')

    ax1 = fig.add_subplot(1, 2, 1) 
    ax2 = fig.add_subplot(1, 2, 2)

    ax1.scatter(x,y1, marker='.', label='y1=sin(x)')
    ax2.scatter(x,y2, marker='^', label='y2=cos(x)')

    ax1.grid()
    ax2.grid()

    ax1.legend()
    ax2.legend()

    mplcursors.cursor()
    plt.show()

    # Se debe 
    # colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.11111111


def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.

    fig = plt.figure()
    fig.suptitle('EJ 3: BAR PLOT')

    ax = fig.add_subplot()
    ax.bar(lenguajes,color='r', height= performance)
    plt.ylabel('PERFORMANCE')
    plt.xlabel('LENGUAJES')
    ax.grid()

    plt.show()


def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico

    fig = plt.figure()
    fig.suptitle('USO DE LENGUAJES EN NUEVOS PROGRAMADORES')
    
    ax = fig.add_subplot()
    # i= uso_lenguajes.values()
    ax.pie(uso_lenguajes.values(), labels=uso_lenguajes.keys(), autopct='%1.1f%%',startangle=90, explode= (0.3, 0,0,0.1,0,0,0))
    ax.axis('equal')
    
    plt.show()
def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal

    # signal_x = [....]
    # signal_y = [....]
    signal_x = [i['X'] for i in signal]
    signal_y = [i['Y'] for i in signal]
    # print(signal_y)
    # plot(signal_x, signal_y)
    fig = plt.figure()
    fig.suptitle('Multiples lineas en un mismo grafico')
    
    # ax.plot(signal_y, color='r')
    
    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7

    # filter_signal_x = [....]
    # filter_signal_y = [....]
    filter = [i for i in signal if abs(i['Y']) > 0.7 ]
    filter_signal_x = [i['X'] for i in filter]
    filter_signal_y = [i['Y'] for i in filter]
    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)
    
    ax = fig.add_subplot()
    ax.plot(signal_x, signal_y, label='Senoidal')
    ax.scatter(filter_signal_x, filter_signal_y, label='Filtrados', color='Green')

    plt.legend()
    plt.grid()
    plt.show()
    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    ej5()
