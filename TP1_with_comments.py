# -*- coding: utf-8 -*-
"""
Created on Tue May 27 12:59:56 2014

@author: asyed

"""
# Ejercicio 1:

# Se importan los funciones necesarias del repositorio de funciones de python.

from math import sqrt
from time import time
from random import random
import matplotlib.pyplot as plt

# La funcion abriarchivo modifica la lista de cadena de caracteres que obtenemos del archivo texto "puntosplano.txt" a una lista de lista donde cada element corresponde a las coordenadas [x, y] de los puntos.

def abrirarchivo_txt():
    q=open("puntosplano.txt", "r") #open txt file
    str_list=q.readlines()
    A = []    
    for i in range (len(str_list)):
        a=str_list[i].split(' ')   
        A.append([float(a[0]), float(a[1])]) 
    return A

# Definimos una funcion que nos devuelve una lista de puntos aleatorios B.
    
def randomlist(N):
    B = []    
    for i in range (N):
        B.append([random(), random()])
    return B

# 1) La definición fuerzabruta() compara la distancia entre todo los elementos de la lista, devolviendo los pares menos alejados y la distancia que los separa. Complejidad cuadratica.

def fuerzabruta(A):
    d_min =  sqrt((A[0][0] - A[1][0])**2 + (A[0][1] - A[1][1])**2)  # d_min= cota de minima distancia
    for i in range(0, len(A)):
        for j in range(i+1,len(A)):    
            d1 =  sqrt((A[i][0] - A[j][0])**2 + (A[i][1] - A[j][1])**2)
            if d1 <= d_min:
                d_min = d1
                a = A[i]
                b = A[j] 
    return d_min, a, b 

# 2) a) La función mergersort ordena la lista de puntos en su coordenada x. Complejidad n.log n.
    
def mergesort(A):
    if len(A) == 1: # conquer
        return A 
    elif len(A) == 2: # conquer
        if A[0][0] < A[1][0]:
            return A 
        else:
            return [A[1],A[0]] 
    else:
        m = len(A) // 2 # divide
        left = mergesort(A[:m]) # llamada recursiva hasta caso base
        right = mergesort(A[m:])        
        return merge(left,right) # combine    

def merge(left, right): # combinar dos listas ordenadas.
    A = []
    i = 0
    j = 0
# recorre ambas listas hasta que alguna de las condiciones del ciclo se haga False:
    while i < len (left) and j < len(right):
        if left[i][0] < right[j][0]:
            A.append(left[i])
            i+= 1
        else:
            A.append(right[j])
            j+= 1
 # si alguna lista se termina antes de la otra, se agrega lo que falta:
    if i == len(left):
        A = A + right[j:]
    if j == len(right):
        A = A + left[i:]        
    return A

# 2) b) algoritmo que busca recursivamente la distancia minima y la devuelve junto al par de puntos. 

def distancia(A, B): #funcion auxiliar
    d = sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)        
    return d
        
def inteligente(A):       
    if len(A) == 2: # conquer
        return distancia(A[0], A[1]), A[0], A[1] 
    if len(A) == 3: # conquer, para listas impares.  
       return fuerzabruta(A) # se miden las distancias entre los tres puntos usando fuerza bruta (tupla)
    if len(A) > 3:
       m = len(A) // 2 # divide
       left = inteligente(A[:m]) # llamada recursiva
       right = inteligente(A[m:])        
       return combine(left,right, A[:m],A[m:]) #merge 
       
def combine(left, right, L, R): # merge
#los puntos entre las dos listas dentro de x1 y x2 se guardan en la lista Points.
    Points = [] 
    if left[0] < right[0]:
        d = left[0]
        punto= left[1],left[2]
    else:
        d = right[0]
        punto= right[1],right[2]
#cota para buscar a la izquierda del ultimo punto de la lista left        
    x1 = L[len(L)-1][0] - d 
#cualquier punto en left mayor a x1 es agregado a Points.    
    for i in range (len(L)):    
        if L[i][0] >= x1:
            Points += [L[i]]
#cota para buscar a la derecha del primer punto de la lista right    
    x2 = R[0][0] + d 
#cualquier punto en right menor a x2 es agregad a Points.    
    for i in range (len(R)):    
        if R[i][0] <= x2:
            Points += [R[i]]
    if len(Points) > 1:
#se busca la minima distancia dentro de Points por fuerzabruta, se compara con el minimo de left y right.
        if d < fuerzabruta(Points)[0]:
            return d, punto[0],punto[1]
        else:
            return fuerzabruta(Points)
    else:
        return d,punto[0],punto[1]

# La función search define un rango de tolerancia al modulo la resta de las distancias devueltas por fuerzabruta y inteligente para verificar los resultados.
def search(N, tolerancia):   
        A = mergesort(randomlist(N))
        s = fuerzabruta(A)[0]
        r = inteligente(A)[0]
        if abs(r - s)<tolerancia:
            return True
        else:
            return False
            
def Scatter_plot_min_distance(A,a,b): 
# Scatterplot: grafica el conjunto de puntos y señala el par de distancia minima. 
#Argumentos: A=lista de puntos; a, b= coordenadas del par de puntos de minima distancia.
    x = [row[0] for row in A]
    y = [row[1] for row in A]            
    plt.scatter(x, y)
    xa = a[0]
    ya = a[1]
    xb = b[0]
    yb = b[1]
    plt.plot([xa,xb],[ya,yb], linestyle='-', marker='o', color='r')
    plt.axes().set_aspect('equal')
    
#Running_time mide el tiempo que tarda en ejecutarse la funciones fuerzabruta, mergesort y inteligente.            
def Running_time(N):
#el menor tiempo que detecta la funcion time es el millisegundo.
    A = randomlist(N)
    time1=time()
    fuerzabruta(A)
    time2=time()
    time3=time()    
    A = mergesort(A)
    inteligente(A)
    time4=time()
    return time2-time1, time4-time3

# Definimos una funcion para graficar Running_time en escala log.    
def Plot_logscale_Running_time(N,step):
    x = []
    y1 = []
    y2 = []
    plt.figure()
    ax = plt.gca()    
    i = 0
    j = 1    
    while i < N:            
        i = step**j
        t1,t2 = Running_time(i)
        x += [i]
        y1 += [t1]
        y2 += [t2]         
        j += 1
        plt.scatter(x, y1,color='b')
        plt.scatter(x, y2,color='r')
    plt.axes().set_autoscale_on(True)
    plt.axes().autoscale_view(False,False,True)    
    ax.set_yscale('log')
    ax.set_xscale('log')    
    plt.show()