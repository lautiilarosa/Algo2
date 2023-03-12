#from algo1 import *
from linkedlist import *

#Descripción: Agrega un elemento al comienzo de Q, siendo Q una
#estructura de tipo LinkedList.

def enqueue(q,element):
  add(q,element)

#Descripción: extrae el último elemento de la cola Q, siendo Q
#una estructura de tipo LinkedList.

def dequeue(q):
  if q.head == None:
    return None
  else:
    index = length(q)
    i = 0
    currentnode = q.head
    while currentnode != None:
      if i == index-1:
        value = currentnode.value
        delete(q,value)
        return value
      else:
        currentnode = currentnode.nextNode
        i += 1    

