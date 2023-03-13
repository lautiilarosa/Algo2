from linkedlist import *
from myqueue import *

class AVLTree:
	root = None

class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None


#rotateLeft(Tree,avlnode) 
#Descripción: Implementa la operación rotación a la izquierda 
#Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  izquierda
#Salida: retorna la nueva raíz

def rotateLeft(Tree,avlnode):
      newroot = avlnode.rightnode
      newroot.parent = avlnode.parent
      if avlnode.parent == None:
            Tree.root = newroot
      else:
            if avlnode.parent.leftnode == avlnode:
                  avlnode.parent.leftnode = newroot
            else:
                  avlnode.parent.rightnode = newroot
      
      avlnode.rightnode = newroot.leftnode
      avlnode.parent = newroot
      newroot.leftnode = avlnode
      if avlnode.rightnode != None:
            avlnode.rightnode.parent = avlnode




#rotateRight(Tree,avlnode) 
#Descripción: Implementa la operación rotación a la derecha 
#Entrada: Un Tree junto a un AVLnode sobre el cual se va a operar la rotación a la  derecha
#Salida: retorna la nueva raíz

def rotateRight(Tree,avlnode):
      newroot = avlnode.leftnode
      newroot.parent = avlnode.parent
      if avlnode.parent == None:
            Tree.root = newroot
      else:
            if avlnode.parent.leftnode == avlnode:
                  avlnode.parent.leftnode = newroot
            else:
                  avlnode.parent.rightnode = newroot

      avlnode.leftnode = newroot.rightnode
      avlnode.parent = newroot
      newroot.rightnode = avlnode
      if avlnode.leftnode != None:
            avlnode.leftnode.parent = avlnode




#calculateBalance(AVLTree) 
#Descripción: Calcula el factor de balanceo de un árbol binario de búsqueda. 
#Entrada: El árbol AVL  sobre el cual se quiere operar.
#Salida: El árbol AVL con el valor de balanceFactor para cada subarbol

def calculateBalance(AVLTree):
      if AVLTree.root != None:
            if AVLTree.root.leftnode == None and AVLTree.root.rightnode == None:
                  AVLTree.root.bf = 0
                  return 
            else:
                  calculateBalanceR(AVLTree.root)
                  return 
      else:
            return


# Función Recursiva que calcula el balanceo

def calculateBalanceR(currentnode):
      #Caso Base
      if currentnode == None:
            return 0

      #Caso general
      leftH = calculateBalanceR(currentnode.leftnode)
      rightH = calculateBalanceR(currentnode.rightnode)

      currentnode.bf = leftH - rightH

      if leftH >= rightH:
            return leftH + 1
      else:
            return rightH + 1

