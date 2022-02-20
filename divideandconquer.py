# -*- coding: utf-8 -*-
"""
Created on Thu May 22 14:24:49 2014

@author: AGS
"""

#Algoritmo de busqueda lineal: recibe secuencia y condición booleana sobre elementos. Itera hasta encontrar un elemento que cumple la condición booleana. En el peor caso itera n veces.

#Eficiencia lineal (n) 
#Seudocodigo:

#Datos de entrada:
#  vec: vector en el que se desea buscar el dato
#  tam: tamaño del vector. Los subíndices válidos van desde 0 hasta tam-1 inclusive.
#  dato: elemento que se quiere buscar.
#
#Variables
#  pos: posición actual en el arreglo
#
#pos = 0
#Mientras pos < tam:
# Si vec[pos] == dato devolver verdadero y/o pos, de lo contrario:
# pos = pos + 1
#Fin (Mientras)
#Devolver falso.

x= 5
a= [0, 5, 6, 1, 4, 5]
def algolineal(a, x):
    i = 0
    while (i < len(a) and a[i] != x):
        i+= 1
    return i < len(a)
print(algolineal(a, x))

#Algoritmo busqueda binaria:

#seudocodigo:
#Datos de entrada:
#  vec: vector en el que se desea buscar el dato
#  tam: tamaño del vector. Los subíndices válidos van desde 0 hasta tam-1 inclusive.
#  dato: elemento que se quiere buscar.
#
#Variables
#  centro: subíndice central del intervalo
#  inf: límite inferior del intervalo
#  sup: límite superior del intervalo
#
#inf = 0
#sup = tam-1
#
#Mientras inf <= sup:
#  centro = ((sup - inf) / 2) + inf // División entera: se trunca la fracción
#  Si vec[centro] == dato devolver verdadero y/o pos, de lo contrario:
#   Si dato < vec[centro] entonces:
#    sup = centro - 1
#   En caso contrario:
#    inf = centro + 1
#Fin (Mientras)
#Devolver Falso

a = range(50000)
x=450

def BusquedaBinaria(a, x):
    if len (a) == 0:
        return False
    elif len(a) == 1:
        return a[0] == x
    else:
        medio = len (a) // 2
        if x < a[medio]:
            return BusquedaBinaria(a[:medio], x)
        elif x > a[medio]:
            return BusquedaBinaria(a[medio+1:], x)
        else:
            return True
print(BusquedaBinaria(a, x))

#Suma maxima de un lista en forma iterative y en forma recursiva.

a= [3, -4, 5, -2, -2, 6, -3, 5, -3, 2]
def SumaMax(a):
    max = a[0]
    sum = 0
    for i in range (0, len(a)):
        for j in range (i, len(a)):
            sum = sum + a[j]
            if  sum > max:
                max = sum
            print(max)
        return max
print(SumaMax(a))

#funciones auxiliares:

def max(a, b):
    if a > b:
        return a
    else:
        return b

def SubMaxMedio(a, m):
    suma1, suma2 = 0, 0
    m == len(a) // 2
    for i in range (m-1, -1, -1):
        max1 = a[0]
        suma1 = suma1 + a[i]
        if suma1 > max1:
            max1 = suma1
    for j in range (m, len(a)):
        max2 = a[0]
        suma2 = suma2 + a[j]
        if suma2 > max2:
            max2 = suma2
    return max1 + max2
print(SubMaxMedio(a, m))

#def Submax(a):
#    if len (a)== 0:
#        return 0
#    elif len (a) == 1:
#        return a[0]
#    else:
#        m = len (a) // 2
#        if 
#



            