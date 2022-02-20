# -*- coding: utf-8 -*-

import TP1_with_comments as tp

N = 1000 # cantidad de puntos de la lista de puntos aleatorios.  

A = tp.abrirarchivo_txt() # cargamos un archivo de texto
B = tp.randomlist(N) # creamos una lista aleatoria de puntos

B_ord = tp.mergesort(B) # ordenamos la lista

FB = tp.fuerzabruta(B_ord) # corremos fuerzabruta. 
IG = tp.inteligente(B_ord) # corremos inteligente

# Comparamos FB e IG

# Search devuelve True si se respecta el rango de tolerancia.
tolerancia= 1e-9
print(tp.search(N, tolerancia))
print('Resultado FB:',FB)
print('Resultado IG:',IG)
tp.Scatter_plot_min_distance(B_ord,IG[1],IG[2])
# tp.Scatter_plot_min_distance(B_ord,FB[1],FB[2])

# Graficamos los tiempos de corrida de FB y IG en escala log. 
step= 2 # la base de una sucesion exponencial para el tamano del conjunto de puntos hasta alcanzar N.
tp.Plot_logscale_Running_time(N, step)
