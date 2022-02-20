# -*- coding: utf-8 -*-+

class Laberinto(object):
  def __init__(self, parent=None):
    self.parent = parent
#    self.cargar('laberintovacio.lab')
    self.paredes =[[]]
    
    ##### interfaz (metodos publicos)

    ####
    #### COMPLETAR CON LOS METODOS PEDIDOS
    ####
    
  def __str__(self):
    estado = self.estado
    estado[self.getPosicionRata()[0]][self.getPosicionRata()[1]] = 'R'
    estado[self.getPosicionQueso()[0]][self.getPosicionQueso()[1]] = 'Q'
    toprint = '\n '
    if self.paredes[0][0][:2] == [True, True]:
      toprint += '+'
    if self.paredes[0][0][:2] == [True, False]:
      toprint += ' '
    if self.paredes[0][0][:2] == [False, True]:
      toprint += '-'
    if self.paredes[0][0][:2] == [False, False]:
      toprint += ' '
    for j in range(self.tamano()[1]):
      if self.paredes[0][j][1:3] == [False, False]:
        toprint += '  '
      if self.paredes[0][j][1:3] == [True, False]:
        toprint += '--' 
      if self.paredes[0][j][1:3] == [False, True]:
        toprint += ' +'
      if self.paredes[0][j][1:3] == [True, True]:
        toprint += '-+' 
    toprint += '\n'	
    for i in range(self.tamano()[0]):
      line = [' ', ' ']
      if self.paredes[i][0][0] == True and self.paredes[i][0][3] == True:
        line[0] += '|'
        line[1] += '+'
      if self.paredes[i][0][0] == False and self.paredes[i][0][3] == True:
        line[0] += ' '
        line[1] += '-'
      if self.paredes[i][0][0] == True and self.paredes[i][0][3] == False:
        line[0] += '|'
        line[1] += '+'
      if self.paredes[i][0][0] == False and self.paredes[i][0][3] == False:
        line[0] += ' '
        line[1] += ' '
      for j in range(self.tamano()[1]):
        if self.paredes[i][j][2:] == [False, False]:
          if i + 1 < self.tamano()[0] and self.paredes[i+1][j][2] == True:
            line[0] += str(estado[i][j]) + ' ' 
            line[1] += ' +'
          elif j + 1 < self.tamano()[1] and self.paredes[i][j+1][3] == True:
            line[0] += str(estado[i][j]) + ' ' 
            line[1] += ' -'
          else:
            line[0] += str(estado[i][j]) + ' ' 
            line[1] += '  '
        if self.paredes[i][j][2:] == [True, False]:
          line[0] += str(estado[i][j]) + '|' 
          line[1] += ' +'
        if self.paredes[i][j][2:] == [False, True]:
          if i + 1 < self.tamano()[0] and self.paredes[i+1][j][2] == True:
            line[0] += str(estado[i][j]) + ' ' 
            line[1] += '-+'
          else:
            line[0] += str(estado[i][j]) + ' ' 
            line[1] += '--'
        if self.paredes[i][j][2:] == [True, True]:
          line[0] += str(estado[i][j]) + '|' 
          line[1] += '-+'
      toprint += line[0] + '\n' + line[1] + '\n'    
    return toprint
     
   
  
  def cargar(self, fn):
    q = open(fn, "r") #open lab file
    #    
    strdims = q.readline()
    strdims = strdims.lstrip('Dim(').rstrip(')\n')
    dims = strdims.split(',')
    N = int(dims[0])  
    M = int(dims[1])       
    #    
    str_list = q.readlines()
    A = []    
    for i in range(N):
      a = str_list[i].split('][')
      end = len(a)-1
      a[0] = a[0].lstrip('[')
      a[end] = a[end].rstrip(']\n')
      for j in range(M):
        a[j] = a[j].split(',')
        a[j] = [bool(int(a[j][0])),bool(int(a[j][1])),bool(int(a[j][2])),bool(int(a[j][3]))]     
      A.append(a) 
    self.paredes = A
    self.estado = self._matrizvacia()
    self.R = [0,0]
    self.Q = [N-1,M-1]
    self.PrePos = []
    self.J = []
    self.contadores = []
    self.N = 0
    self.k = -1
    
  def tamano(self):
    N = len(self.paredes)
    M = len(self.paredes[0])
    return [N,M]
    
  def resetear(self):
    self.estado = self._matrizvacia()
    self.PrePos = []
    self.J = []
    self.contadores = []
    self.N = 0
    self.k = -1
    
  def getPosicionRata(self):
    return self.R

  def getPosicionQueso(self):
    return self.Q
      
  def setPosicionRata(self,i,j):
    if i >= 0 and j >= 0 and i < self.tamano()[0] and j < self.tamano()[1]:
      self.R = [i,j]
      return True
    else:
      return False
      
  def setPosicionQueso(self,i,j):
    if i >= 0 and j >= 0 and i < self.tamano()[0] and j < self.tamano()[1]:
      self.Q = [i,j]
      return True
    else:
      return False
      
  def esPosicionRata(self, i, j):
    if [i, j] == self.getPosicionRata():
      return True
    else:
      return False      
  
  def esPosicionQueso(self, i, j):
    if [i, j] == self.getPosicionQueso():
      return True
    else:
      return False

  def get(self, i, j):
    return self.paredes[i][j]
    
  def getInfoCelda(self, i, j):
    visit = False
    actual = False
    if self.estado[i][j] == 'V':
      visit = True
    if self.estado[i][j] == 'A':
      actual = True  
    return {'visitado' : visit, 'caminoActual' : actual}    
    
  def resuelto(self):
    if self.getPosicionRata() == self.getPosicionQueso():
      return True
    else:
      return False
    
  def resolver(self):
    return self.getPosicionRata() == self.getPosicionQueso() or self.backtracking([],[0,0])
    
  #def avanzarN(self,n):
    #if self.getPosicionRata() == self.getPosicionQueso():
      #return True
    #else:
      #flag, n, temp = self.backtracking([],n,self.PrePos[len(self.PrePos)-1])  
      #self.PrePos.append(temp)         
      #if(flag):
        #return True
      #else:
        #return False
        
  def backtracking(self,I,PrePos):   
    if(I != []):       
      self.AvanzarHacia(I)
      if self.getPosicionRata() == self.getPosicionQueso():
        return True  
    ActPos = self.getPosicionRata()
    flag, I = self.posibilidades()
    if flag == '0':
      if(I == []):
        return False
      self.volveratras(PrePos)           
    if flag == '1+':
      i = 0
      rama = False
      while(rama == False and i < 4):
        if(I[i]):	
          J = [False, False, False, False]            
          J[i] = True
          #print(self)
          rama = self.backtracking(J,ActPos)
        i += 1
      if not rama:        
        self.volveratras(PrePos)
        return False
      else:
        return True
    return False
    
  def avanzarN(self,N):
    if self.getPosicionRata() == self.getPosicionQueso():
      return True
    n = N
    Nant = N
    N = self.N + N
    self.N = N
    kant = 0
    while(n > 0):
      if(n != N):       
        if self.getPosicionRata() == self.getPosicionQueso():
          return True  
      flag, I = self.posibilidades()
      if(n > 0 and flag == '0'):
        if n == N:
          return False
        if(self.k == -1):
          k = 1
        else:
          k = self.k
        while(n > 0 and k < self.contadores[len(self.contadores)-1] + 1):
          J = self.volveratras(self.PrePos[N-n-2*k+1-kant])
          print(self)
          self.J.append(J)
          k += 1
          n -= 1
          self.k = k
        if(k == self.contadores[len(self.contadores)-1] + 1):
          self.k = -1
        kant += 2*self.contadores[len(self.contadores)-1]
        j = 1
        while(j < len(self.contadores) + 1):
          self.contadores[len(self.contadores)-j] -= k - 1
          j += 1
        self.contadores = self.contadores[:len(self.contadores)-1]
        self.PrePos = self.PrePos[:(N-n-kant)]
      if(n > 0 and flag == '1+'):
        i = 0
        flag2 = False
        while(i < 4 and flag2 == False):
          if(I[i]): 
            J = [False, False, False, False]            
            J[i] = True
            flag2 = True
            PrePos = self.getPosicionRata()
            self.PrePos.append(PrePos)
            self.J.append(J)
            self.AvanzarHacia(self.J[N-n])
            n -= 1
            print(self)
            m = I[0]*1 + I[1]*1 + I[2]*1 + I[3]*1
            if m > 1:
              self.contadores.append(0)
            j = 1
            while(j < len(self.contadores) + 1):
              self.contadores[len(self.contadores)-j] += 1
              j += 1
          i += 1
    return False         

  
      
  #def volveratras(self,n,PrePos):		
    #ActPos = self.getPosicionRata()    
    #I = [False, False, False, False]
    #if(PrePos == [ActPos[0],ActPos[1]-1]):
      #I[0] = True
    #if(PrePos == [ActPos[0]-1,ActPos[1]]):
      #I[1] = True
    #if(PrePos == [ActPos[0],ActPos[1]+1]):
      #I[2] = True
    #if(PrePos == [ActPos[0]+1,ActPos[1]]):
      #I[3] = True
    #n = self.AvanzarHacia(I,n)
    #self.estado[ActPos[0]][ActPos[1]] = 'V'
    #return n

  #def AvanzarHacia(self,I,n):
    #ActPos = self.getPosicionRata()
    #self.estado[ActPos[0]][ActPos[1]] = 'A'
    #if(I[0]):
      #self.setPosicionRata(ActPos[0],ActPos[1]-1)
    #if(I[1]):
      #self.setPosicionRata(ActPos[0]-1,ActPos[1])
    #if(I[2]):
      #self.setPosicionRata(ActPos[0],ActPos[1]+1)
    #if(I[3]):
      #self.setPosicionRata(ActPos[0]+1,ActPos[1])
    #return n-1
    
  def volveratras(self,PrePos):		
    ActPos = self.getPosicionRata()    
    I = [False, False, False, False]
    if(PrePos == [ActPos[0],ActPos[1]-1]):
      I[0] = True
    if(PrePos == [ActPos[0]-1,ActPos[1]]):
      I[1] = True
    if(PrePos == [ActPos[0],ActPos[1]+1]):
      I[2] = True
    if(PrePos == [ActPos[0]+1,ActPos[1]]):
      I[3] = True
    self.AvanzarHacia(I)
    self.estado[ActPos[0]][ActPos[1]] = 'V'
    return I 
    
  def AvanzarHacia(self,I):
    ActPos = self.getPosicionRata()
    self.estado[ActPos[0]][ActPos[1]] = 'A'
    if(I[0]):
      self.setPosicionRata(ActPos[0],ActPos[1]-1)
    if(I[1]):
      self.setPosicionRata(ActPos[0]-1,ActPos[1])
    if(I[2]):
      self.setPosicionRata(ActPos[0],ActPos[1]+1)
    if(I[3]):
      self.setPosicionRata(ActPos[0]+1,ActPos[1])
    
      
  def posibilidades(self):
    I = [True, True, True, True]     
    ActPos = self.getPosicionRata()    
    if(ActPos[1] > 0 and (self.estado[ActPos[0]][ActPos[1]-1] == 'A' or self.estado[ActPos[0]][ActPos[1]-1] == 'V') or self.paredes[ActPos[0]][ActPos[1]][0] == 1):
      I[0] = False
    if(ActPos[0] > 0 and (self.estado[ActPos[0]-1][ActPos[1]] == 'A' or self.estado[ActPos[0]-1][ActPos[1]] == 'V') or self.paredes[ActPos[0]][ActPos[1]][1] == 1):
      I[1] = False
    if(ActPos[1] < self.tamano()[1] - 1 and (self.estado[ActPos[0]][ActPos[1]+1] == 'A' or self.estado[ActPos[0]][ActPos[1]+1] == 'V') or self.paredes[ActPos[0]][ActPos[1]][2] == 1):
      I[2] = False
    if(ActPos[0] < self.tamano()[0] - 1 and (self.estado[ActPos[0]+1][ActPos[1]] == 'A' or self.estado[ActPos[0]+1][ActPos[1]] == 'V') or self.paredes[ActPos[0]][ActPos[1]][3] == 1):
      I[3] = False
    sumaposibilidades = 0
    for i in range(4):
      sumaposibilidades += 1*I[i]   
    if(sumaposibilidades == 0):
      return '0', I
    if(sumaposibilidades >= 1):
      return '1+', I        
             
    ##### auxiliares (metodos privados)
    
  def _redibujar(self):
    if self.parent is not None:
      self.parent.update()
      
  def _matrizvacia(self):
    M = []
    for j in range(self.tamano()[0]):
      m = []
      for i in range(self.tamano()[1]):
        m.append(' ')
      M.append(m)
    return M


A = Laberinto()
A.cargar('laberinto10x10.lab')
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
A.avanzarN(1)
