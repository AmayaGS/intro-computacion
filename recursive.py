# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 20:30:45 2014

@author: AGS
"""


#Fibonacci series:

#Ejercicio 1:

n=4

#def fib(n):
#    if n <= 1:
#        return n   
#    t = fib(n-1) + fib(n-2) 
#    print(n)
#    return t
#    
##print(fib(10))
#
#def factorial(n):
#    if n==1:
#        return 1
#    else:
#        return n*factorial(n-1)
#print (factorial(n))

#Ejercicio 3:

a=[3, 2, 7, 6, 2, 8] 

#def maximo (a):
#    if len(a)==1:
#        return a[0]
#    else:
#        if a[0]>maximo(a[1:]):
#            return a[0]
#        else:
#            return maximo(a[1:])
#print(maximo(a))
  
     
#def suma(a):
#    if len(a)==0:
#        return 0
#    else:
#        return (a[0]) + suma (a[1:])     
#print(suma(a))
#
#def todospares(a):
#    if len(a)==1:
#        return a[0] % 2 == 0
#    else:
#        return a[0] % 2 == 0 and todospares(a[1:])
#print(todospares(a))
        
#i=3
#def eliminar(a, i):
#    if i == 0:
#        return (a[1:])
#    else:
#        return [a[0]] + eliminar (a[1:], i - 1) 
#print(eliminar(a, i))
        
#def promedio(a):
#    if len(a)==1:
#        return a[0]
#    else:
#        return ((a[0]) + suma (a[1:]))/len(a)
#print(promedio(a))   

a=[3, 2, 7, 2, 2, 8]         
x=3
#def cantidadapariciones(a, x):
#    if len (a) == 0:
#        return 0
#    else:
#        if a[0] == x:
#            return 1 + cantidadapariciones(a[1:], x)
#        else:
#            return cantidadapariciones(a[1:], x)
#print(cantidadapariciones(a, x))
        
        
#def BuscarEliminar(a, x):
#    if len (a) == 0:
#        return []
#    else:
#        if a[0] == x:
#           return BuscarEliminar(a[1:], x) 
#        else:
#            return [a[0]] + BuscarEliminar(a[1:], x)
#print(BuscarEliminar(a, x))
# 

#a=["h", "o", "l", "a"]        
#def reverso(a):
#    if len (a) == 0:
#        return []
#    else:
#        return reverso(a[1:]) + [a[0]]
#print(reverso(a))
#print(reverso(reverso(a)))
#            

#a= [1, 2, 3, 4, 5, 6, 9]
#def ordenascendente(a):
#    if len(a)== 1:
#        return True 
#    else:
#        return a[0] < a[1] and ordenascendente(a[1:])
#print(ordenascendente(a))
#           
#            
#print([a[0]]+a[1:])       
 
a=[-11, 2, 7, 2, 2, 8, -10]         
#def listaAbs(a):
#    if len(a) == 0:
#        return [] 
#    else:
#        if a[0] < 0:
#            return [-a[0]] + listaAbs(a[1:])
#        else:
#            return [a[0]] + listaAbs(a[1:]) 
#print(listaAbs(a))         

#def maximoAbs(a):
#    if len (a) == 1:
#        return a[0]
#    else:
#        if a[0] > maximoAbs(a[1:]):
#            return a[0]  
#        else:
#            return maximoAbs(a[1:])
            
#def maximoAbs(a):
#    if len (a) == 1:
#        if a[0] < 0:
#            return -a[0]
#        else:
#            return a[0]
#    else:
#        if a[0] < 0 and -a[0] > maximoAbs(a[1:]):
#            return -a[0]  
#        else:
#            return maximoAbs(a[1:])                        
#print(maximoAbs(a))

V=[2, 4, 8, 3, 1, 8]
X=[12, 8, 5, 3, 1, 12]  

def pert(c, X):
    return c in X
          
def ePCHM(X, V): 
    if len (X) == 0:
        return []
    else:
        if pert(X[0], V):
            return ePCHM(X[1:], V)
        else:
            return [X[0]] + ePCHM(X[1:], V)
print(ePCHM(X, V))
#importa el orden de las listas en la entrada!!!!!!!!!! 
        
    
    
    
    
    
    
    
    
    
        






   