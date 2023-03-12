from algo1 import *
from Vector import *

#Create_Set(Array):
#Descripción: Crea un TAD de tipo Set a partir de un arreglo recibido como
#parámetro.
#Entrada: el Arreglo sobre el cual se quiere construir el TAD Set
#Salida: Un Array que representa el TAD Set

def Create_set(arreglo):
  n=len(arreglo)
  
  for i in range(0,len(arreglo)):
    aux=arreglo[i]
    cont=0
    if aux != None:
      for j in range(0,len(arreglo)):
        if i != j and aux == arreglo[j]:
          arreglo[j] = None
          cont = cont + 1
      n = n - cont    
        
  resarray=Array(n,0)
  s=0
  for k in range(0,len(arreglo)):
    if arreglo[k] != None:
      resarray[s] = arreglo[k]
      s=s+1

  return resarray

#Check_Duplicates(Array):
#Una función que devuelve un booleano si un array contiene elementos duplicados

def Check_Duplicates(arreglo):
  cont = 0
  for i in range(0,len(arreglo)):
    aux = arreglo[i]
    for j in range(0,len(arreglo)):
      if i != j and aux == arreglo[j]:
        cont = cont + 1

  if cont > 0:
    v=True
  else:
    v=False
  return v

#Union(Array S,Array T):
#Descripción: Aplica la operación UNIÓN sobre los conjuntos (Sets) S y T.
#Precondición: La operación debe garantizar que no hay elementos duplicados
#en los arreglos. (Ver Nota más abajo)
#Entrada: Dos arreglos que representan los Sets S y T
#Salida: Un Array que representa un nuevo TAD Set  

def Union(arrays,arrayt):
  
  if (Check_Duplicates(arrays) == False and Check_Duplicates(arrayt) == False):
    aux=Array(len(arrays)+len(arrayt),0)
    
    for i in range(0,len(arrays)):
      aux[i] = arrays[i]
    for j in range(0,len(arrayt)):
      aux[j+len(arrays)] = arrayt[j]

    newarray=Create_set(aux)
    return newarray
  else:
    return 

#Intersection(Array S,Array T):
#Descripción: Aplica la operación INTERSECCIÓN sobre los conjuntos S
#y T.
#Precondición: La operación debe garantizar que no hay elementos
#duplicados en los arreglos. (Ver Nota más abajo)
#Entrada: Dos arreglos que representan los Sets S y T
#Salida: Un Array que representa un nuevo TAD Set

def Intersection(arrays,arrayt):

  if (Check_Duplicates(arrays) == False and Check_Duplicates(arrayt) == False):
    
    ind=0

    for i in range(0,len(arrays)):
      for j in range(0,len(arrayt)):
        if arrays[i] == arrayt[j] :
          ind=ind+1
    newarray=Array(ind,0)

    n=0
    for i in range(0,len(arrays)):
      for j in range(0,len(arrayt)):
        if arrays[i] == arrayt[j]:
            newarray[n] = arrays[i]
            n=n+1
          
    return newarray
  else:
    return 

#Difference(Array S, Array T):
#Descripción: Aplica la operación DIFERENCIA sobre los conjuntos S y T.
#Precondición: La operación debe garantizar que no hay elementos duplicados
#en los arreglos. (Ver Nota más abajo)
#Entrada: Dos arreglos que representan los Sets S y T
#Salida: Un Array que representa un nuevo TAD Set

def Difference(arrays,arrayt):

  if (Check_Duplicates(arrays) == False and Check_Duplicates(arrayt) == False):
    ind=0
    for i in range(0,len(arrays)):
      cont=0
      for j in range(0,len(arrayt)):
        if arrays[i] == arrayt[j]:
          cont=cont+1
      if cont == 0:
        ind=ind+1

    newarray=Array(ind,0)
    n=0 
    for i in range(0,len(arrays)):
      c=0
      for j in range(0,len(arrayt)):
        if arrays[i] == arrayt[j]:
          c=c+1
      if c == 0:
        newarray[n] = arrays[i]
        n=n+1
    return newarray
  else:
    return
        