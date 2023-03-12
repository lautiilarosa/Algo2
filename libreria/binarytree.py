
# from algo1 import *
from linkedlist import *
from myqueue import *


class BinaryTree:
  root = None


class BinaryTreeNode:
  key = None
  value = None
  leftnode = None
  rigthnode = None
  parent = None


# search(B,element)
# Descripción: Busca un elemento en el TAD árbol binario.
# Entrada: el árbol binario B en el cual se quiere realizar la búsqueda
# (BinaryTree) y el valor del elemento (element) a buscar.
# Salida: Devuelve la key asociada a la primera instancia del elemento.
# Devuelve None si el elemento no se encuentra.


def search(B, element):
  return searchR(element, B.root)


def searchR(element, node):
  if node != None:
    if node.value == element:
      return node.key
    else:
      rigthkey = searchR(element, node.rigthnode)
      if rigthkey != None:
        return rigthkey

      leftkey = searchR(element, node.leftnode)
      if leftkey != None:
        return leftkey
  else:
    return


# insert(B,element,key)
# Descripción: Inserta un elemento con una clave determinada del TAD
# árbol binario.
# Entrada: el árbol B sobre el cual se quiere realizar la inserción
# (BinaryTree), el valor del elemento (element) a insertar y la clave
# (key) con la que se lo quiere insertar.
# Salida: Si pudo insertar con éxito devuelve la key donde se inserta el
# elemento. En caso contrario devuelve None.


def insert(B, element, key):
  newnode = BinaryTreeNode()
  newnode.value = element
  newnode.key = key
  if B.root != None:
    return insertR(newnode, B.root)
  else:
    B.root = newnode
    return key


def insertR(newnode, currentnode):
  if newnode.key != currentnode.key:
    if newnode.key > currentnode.key:
      if currentnode.rigthnode == None:
        currentnode.rigthnode = newnode
        newnode.parent = currentnode
        return newnode.key
      else:
        return insertR(newnode, currentnode.rigthnode)
    else:
      if currentnode.leftnode == None:
        currentnode.leftnode = newnode
        newnode.parent = currentnode
        return newnode.key
      else:
        return insertR(newnode, currentnode.leftnode)
  else:
    return


# delete(B,element)
# Descripción: Elimina un elemento del TAD árbol binario.
# Poscondición: Se debe desvincular el Node a eliminar.
# Entrada: el árbol binario B sobre el cual se quiere realizar la
# eliminación (BinaryTree) y el valor del elemento (element) a eliminar.
# Salida: Devuelve clave (key) del elemento a eliminar. Devuelve None si
# el elemento a eliminar no se encuentra.


def delete(B, element):
  deletenode = accessnodeE(B.root, element)
  if deletenode != None:
    return deleteNodeCases(B, deletenode)
  else:
    return


def deleteNodeCases(B, deletenode):
  key = deletenode.key

  #Caso 1: El nodo a eliminar es una hoja
  if deletenode.leftnode == None and deletenode.rigthnode == None:
    if deletenode.parent != None:
      if deletenode.parent.leftnode != None and deletenode.parent.leftnode == deletenode:
        deletenode.parent.leftnode = None
        return key
      else:
        deletenode.parent.rigthnode = None
        return key
    else:
      B.root = None
      return key

  #Caso 2: El nodo a eliminar tiene un hijo

  if deletenode.leftnode != None and deletenode.rigthnode == None:
    if deletenode.parent != None:
      if deletenode.parent.leftnode != None and deletenode.parent.leftnode == deletenode:
        deletenode.parent.leftnode = deletenode.leftnode
      else:
        deletenode.parent.rigthnode = deletenode.leftnode

      deletenode.leftnode.parent = deletenode.parent
      return key

    else:
      B.root = deletenode.leftnode
      deletenode.leftnode.parent = None
      return key

  if deletenode.rigthnode != None and deletenode.leftnode == None:
    if deletenode.parent != None:
      if deletenode.parent.leftnode != None and deletenode.parent.leftnode == deletenode:
        deletenode.parent.leftnode = deletenode.rigthnode
      else:
        deletenode.parent.rigthnode = deletenode.rigthnode
        
      deletenode.rigthnode.parent = deletenode.parent
      return key

    else:
      B.root = deletenode.rigthnode
      deletenode.rigthnode.parent = None
      return key

  #Caso 3: El nodo a eliminar tiene dos hijos

  #Quiero insertar el mayor de los menores
  # changenode = bigger(deletenode.leftnode)
  # deletenode.value = changenode.value
  # deletenode.key = changenode.key

  # if changenode.parent.leftnode == changenode:
  #   changenode.parent.leftnode = None
  # else:
  #   changenode.parent.rigthnode = None

  # return key  

  #Quiero insertar el menor de los mayores
  changenode = smaller(deletenode.rigthnode)
  deletenode.value = changenode.value
  deletenode.key = changenode.key

  if changenode.parent.rigthnode == changenode:
    changenode.parent.rigthnode = None
  else:
    changenode.parent.leftnode = None

  return key  


def bigger(node):
  if node.rigthnode != None:
    return bigger(node.rigthnode)
  else:
    return node


def smaller(node):
  if node.leftnode != None:
    return smaller(node.leftnode)
  else:
    return node


def accessnodeE(node, element):
  if node != None:
    if node.value == element:
      return node
    else:
      rigthnode = accessnodeE(node.rigthnode, element)
      if rigthnode != None:
        return rigthnode

      leftnode = accessnodeE(node.leftnode, element)
      if leftnode != None:
        return leftnode
  else:
    return


# deleteKey(B,key)
# Descripción: Elimina una clave del TAD árbol binario.
# Poscondición: Se debe desvincular el Node a eliminar.
# Entrada: el árbol binario B sobre el cual se quiere realizar la
# eliminación (BinaryTree) y el valor de la clave (key) a eliminar.
# Salida: Devuelve clave (key) a eliminar. Devuelve None si el elemento
# a eliminar no se encuentra.

def deleteKey(B,key):
  deletenode = accessnodeK(B.root,key)
  if deletenode != None:
    return deleteNodeCases(B,deletenode)
  else:
    return 


def accessnodeK(node,key):
  if node != None:
    if node.key == key:
      return node
    else:
      if key > node.key:
        rigthkey = accessnodeK(node.rigthnode,key)
        if rigthkey != None:
          return rigthkey
      else:
        leftkey = accessnodeK(node.leftnode,key)
        if leftkey != None:
          return leftkey
  else:
    return 
    
# access(B,key)
# Descripción: Permite acceder a un elemento del árbol binario con una
# clave determinada.
# Entrada: El árbol binario (BinaryTree) y la key del elemento al cual
# se quiere acceder.
# Salida: Devuelve el valor de un elemento con una key del árbol
# binario, devuelve None si no existe elemento con dicha clave.


def access(B, key):
  return accessR(B.root, key)


def accessR(node, key):
  if node != None:
    if node.key == key:
      return node.value
    else:
      if key > node.key:
        rigthvalue = accessR(node.rigthnode, key)
        if rigthvalue != None:
          return rigthvalue
      else:
        leftvalue = accessR(node.leftnode, key)
        if leftvalue != None:
          return leftvalue
  else:
    return


# update(B,element,key)
# Descripción: Permite cambiar el valor de un elemento del árbol binario
# con una clave determinada.
# Entrada: El árbol binario (BinaryTree) y la clave (key) sobre la cual
# se quiere asignar el valor de element.
# Salida: Devuelve None si no existe elemento para dicha clave. Caso
# contrario devuelve la clave del nodo donde se hizo el update.


def update(B, element, key):
  return updateR(B.root, element, key)


def updateR(node, element, key):
  if node != None:
    if node.key == key:
      node.value = element
      return node.key
    else:
      if key > node.key:
        rigthkey = updateR(node.rigthnode, element, key)
        if rigthkey != None:
          return rigthkey
      else:
        leftkey = updateR(node.leftnode, element, key)
        if leftkey != None:
          return leftkey
  else:
    return


# traverseInOrder(B)
# Descripción: Recorre un árbol binario en orden
# Entrada: El árbol binario (BinaryTree)
# Salida: Devuelve una lista (LinkedList) con los elementos del árbol en
# orden. Devuelve None si el árbol está vacío.

def traverseInOrder(B):
  if B.root != None:
    list = LinkedList()
    traverseInOrderR(B.root,list)
    return inverted(list)
  else:
    return

def traverseInOrderR(node,list):
  if node != None:
    traverseInOrderR(node.leftnode,list)
    add(list,node.key)
    traverseInOrderR(node.rigthnode,list)
  else:
    return 


# traverseInPostOrder(B)
# Descripción: Recorre un árbol binario en post-orden
# Entrada: El árbol binario (BinaryTree)
# Salida: Devuelve una lista (LinkedList) con los elementos del árbol en
# post-orden. Devuelve None si el árbol está vacío.

def traverseInPostOrder(B):
  if B.root != None:
    list = LinkedList()
    traverseInPostOrderR(B.root,list)
    return inverted(list)
  else:
    return


def traverseInPostOrderR(node,list):
  if node != None:
    traverseInPostOrderR(node.leftnode,list)
    traverseInPostOrderR(node.rigthnode,list)
    add(list,node.key)
  else:
    return 


# traverseInPreOrder(B)
# Descripción: Recorre un árbol binario en pre-orden
# Entrada: El árbol binario (BinaryTree)
# Salida: Devuelve una lista (LinkedList) con los elementos del árbol en
# pre-orden. Devuelve None si el árbol está vacío.

def traverseInPreOrder(B):
  if B.root != None:
    list = LinkedList()
    traverseInPreOrderR(B.root,list)
    return inverted(list)
  else:
    return 

def traverseInPreOrderR(node,list):
  if node != None:
    add(list,node.key)
    traverseInPreOrderR(node.leftnode,list)
    traverseInPreOrderR(node.rigthnode,list)
  else:
    return 


# traverseBreadFirst(B)
# Descripción: Recorre un árbol binario en modo primero anchura/amplitud
# Entrada: El árbol binario (BinaryTree)
# Salida: Devuelve una lista (LinkedList) con los elementos del árbol
# ordenados de acuerdo al modo primero en amplitud. Devuelve None si el
# árbol está vacío.

def traverseBreadFirst(B):
  if B.root != None:
    
    list = LinkedList()
    cola = LinkedList()
    enqueue(cola,B.root)
    while length(cola) != 0:
      currentnode = dequeue(cola)
      add(list,currentnode.key)
      if currentnode.leftnode != None:
        enqueue(cola,currentnode.leftnode)
      if currentnode.rigthnode != None:
        enqueue(cola,currentnode.rigthnode)

    return inverted(list)
  else:
    return 