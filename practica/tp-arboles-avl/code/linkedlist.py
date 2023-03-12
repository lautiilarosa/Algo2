import random
import math


class Node:
  value = None
  nextNode = None


class LinkedList:
  head = None


#Descripción: Agrega un elemento al comienzo de L, siendo L una LinkedList
#que representa el TAD secuencia.


def add(L, element):
  newnode = Node()
  newnode.value = element
  if L.head != None:
    newnode.nextNode = L.head
    L.head = newnode
  else:
    L.head = newnode


#Descripción: Busca un elemento de la lista que representa el TAD
#secuencia.


def search(L, element):
  currentnode = L.head
  index = 0
  while currentnode != None:
    if element == currentnode.value:
      return index
    else:
      currentnode = currentnode.nextNode
      index += 1
  return None


#Descripción: Inserta un elemento en una posición determinada de la
#lista que representa el TAD secuencia.


def insert(L, element, position):
  if position <= length(L):
    if position == 0:
      add(L, element)
      return position
    else:
      index = 1
      previousnode = L.head
      currentnode = L.head.nextNode
      newnode = Node()
      newnode.value = element
      while previousnode != None:
        if index == position:
          previousnode.nextNode = newnode
          newnode.nextNode = currentnode
          return index
        else:
          index += 1
          previousnode = currentnode
          currentnode = currentnode.nextNode
      return None
  else:
    return None


#Descripción: Elimina un elemento de la lista que representa el TAD
#secuencia.


def delete(L, element):
  index = 0
  if L.head == None:
    return None
  elif element == L.head.value:
    L.head = L.head.nextNode
    return index
  else:
    index += 1
    previousnode = L.head
    currentnode = L.head.nextNode
    while currentnode != None:
      if element == currentnode.value:
        previousnode.nextNode = currentnode.nextNode
        return index
      else:
        index += 1
        previousnode = currentnode
        currentnode = currentnode.nextNode
    return None


#Descripción: Calcula el número de elementos de la lista que representa
#el TAD secuencia.


def length(L):
  currentnode = L.head
  index = 0
  while currentnode != None:
    index += 1
    currentnode = currentnode.nextNode
  return index


#Descripción: Permite acceder a un elemento de la lista en una posición
#determinada.


def access(L, position):
  currentnode = L.head
  index = 0
  while currentnode != None:
    if index == position:
      return currentnode.value
    else:
      index += 1
      currentnode = currentnode.nextNode
  return None


#Descripción: Permite cambiar el valor de un elemento de la lista en
#una posición determinada.


def update(L, element, position):
  index = 0
  currentnode = L.head
  while currentnode != None:
    if index == position:
      currentnode.value = element
      return index
    else:
      index += 1
      currentnode = currentnode.nextNode
  return None


# Descripción: La inversa de una linkedlist


def inverted(L):
  invertedlist = LinkedList()
  currentnode = L.head
  while currentnode != None:
    add(invertedlist, currentnode.value)
    currentnode = currentnode.nextNode
  return invertedlist


# Accede a un nodo de la linkedlist


def accessnode(L, position):
  currentnode = L.head
  index = 0
  while currentnode != None:
    if index == position:
      return currentnode
    else:
      index += 1
      currentnode = currentnode.nextNode
  return None


# Delete con position


def deletePosition(L, position):
  cont = 0
  currentNode = L.head

  if position >= length(L) or position < 0:
    return None

  if position == 0:
    delete(L, currentNode.value)
    return None

  if length(L) - position == 1:

    while currentNode.nextNode != None:
      previousNode = currentNode
      currentNode = currentNode.nextNode
    previousNode.nextNode = None

  else:
    while cont != position:
      previousNode = currentNode
      currentNode = currentNode.nextNode
      cont += 1
    previousNode.nextNode = currentNode.nextNode
    currentNode.nextNode = None


# Imprimir una lista


def printlist(list):
  currentnode = list.head
  print("[", end="")
  while currentnode != None:
    print(currentnode.value, end=" ")
    currentnode = currentnode.nextNode
  print("]")


##################--- Ordenamiento Avanzado --- ##################


def quicksort(list):
  if list.head == None:
    return
  elif list.head.nextNode == None:
    return list
  else:
    newlist = LinkedList()
    return inverted(quicksortR(list, newlist))


def quicksortR(list, newlist):

  # Caso Base

  if length(list) <= 1:
    if list.head != None:
      add(newlist, list.head.value)
      return newlist
    else:
      return

  else:
    # Caso General
    pivot = searchpivot(list)
    leftlist = LinkedList()
    rigthlist = LinkedList()
    posI = 0
    posD = 0
    currentnode = list.head

    while currentnode != None:
      if currentnode.value < pivot:
        insert(leftlist, currentnode.value, posI)
        posI += 1
      else:
        insert(rigthlist, currentnode.value, posD)
        posD += 1
      currentnode = currentnode.nextNode

    quicksortR(leftlist, newlist)
    quicksortR(rigthlist, newlist)
    return newlist


def searchpivot(list):
  index = length(list) - 1
  aux = random.randint(0, index)
  return access(list, aux)


def mergesort(list):

  # Caso Base
  if length(list) == 1:
    return list

  #Caso General

  longitud = length(list) - 1
  index = math.trunc(longitud / 2)
  leftlist = LinkedList()
  rigthlist = LinkedList()
  currentnode = list.head
  pos = 0

  for i in range(0, longitud + 1):
    if i <= index:
      insert(leftlist, currentnode.value, i)
    else:
      insert(rigthlist, currentnode.value, pos)
      pos += 1
    currentnode = currentnode.nextNode

  sublistL = mergesort(leftlist)
  sublistR = mergesort(rigthlist)

  currentnode1 = sublistL.head
  currentnode2 = sublistR.head

  list.head = None
  j = 0

  #Agregar los elementos a la nueva lista
  while currentnode1 != None and currentnode2 != None:
    if currentnode1.value > currentnode2.value:
      insert(list, currentnode2.value, j)
      j += 1
      currentnode2 = currentnode2.nextNode
    else:
      insert(list, currentnode1.value, j)
      j += 1
      currentnode1 = currentnode1.nextNode

  #Agregar los elementos restantes de las dos listas

  while currentnode1 != None and currentnode2 == None:
    insert(list, currentnode1.value, j)
    j += 1
    currentnode1 = currentnode1.nextNode

  while currentnode2 != None and currentnode1 == None:
    insert(list, currentnode2.value, j)
    j += 1
    currentnode2 = currentnode2.nextNode

  return list


##################--- Ordenamiento Básico --- ##################
def bubblesort(list):
  index = length(list) - 1
  contador = index
  for i in range(0, index):
    previousnode = list.head
    currentnode = previousnode.nextNode
    for j in range(0, contador):
      if previousnode.value > currentnode.value:
        if j == 0:
          aux = currentnode.value
          delete(list, aux)
          add(list, aux)
        else:
          auxnode = accessnode(list, j - 1)
          auxnode.nextNode = currentnode
          previousnode.nextNode = currentnode.nextNode
          currentnode.nextNode = previousnode

        currentnode = previousnode.nextNode

      else:
        previousnode = currentnode
        currentnode = currentnode.nextNode
    contador -= 1


def selectionsort(list):
  index = length(list) - 1

  for i in range(0, index):
    min = access(list, i)
    currentnode = accessnode(list, i)
    pos = i
    auxpos = i

    while currentnode != None:
      if currentnode.value < min:
        min = currentnode.value
        pos = auxpos
      currentnode = currentnode.nextNode
      auxpos += 1

    if pos != i:
      previousnode = accessnode(list, pos - 1)
      auxnode = accessnode(list, pos)
      previousnode.nextNode = auxnode.nextNode
      insert(list, min, i)


def insertionsort(list):
  index = length(list) - 1
  currentnode = list.head.nextNode

  for i in range(0, index):
    headnode = list.head
    flag = True
    j = 0
    while currentnode != headnode and flag:
      if currentnode.value < headnode.value:
        if j == 0:
          aux = currentnode.value
          delete(list, aux)
          add(list, aux)
          flag = False
        else:
          previousnode = accessnode(list, i)
          aux = currentnode.value
          previousnode.nextNode = currentnode.nextNode
          insert(list, aux, j)
          flag = False
      else:
        j += 1
        headnode = headnode.nextNode

    currentnode = currentnode.nextNode
