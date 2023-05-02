from algo1 import *
from linkedlist import *

#Descripción: Agrega un elemento al comienzo de S, siendo S una
#estructura de tipo LinkedList

def push(S, element):
    add(S, element)


#Descripción: extrae el primer elemento de la pila S, siendo S
#una estructura de tipo LinkedList

def pop(S):
    deletenode = S.head
    if deletenode != None:
        S.head = deletenode.nextNode
        return deletenode.value
    else:
        return None
