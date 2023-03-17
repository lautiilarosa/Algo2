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
                  update_bf(AVLTree.root)
                  return 
      else:
            return


# Función Recursiva que calcula el balanceo de un nodo raíz

def update_bf(currentnode):
      #Caso Base
      if currentnode == None:
            return 0

      #Caso general
      leftH = update_bf(currentnode.leftnode)
      rightH = update_bf(currentnode.rightnode)

      currentnode.bf = leftH - rightH

      if leftH >= rightH:
            return leftH + 1
      else:
            return rightH + 1


#reBalance(AVLTree) 
#Descripción: balancea un árbol binario de búsqueda. Para esto se deberá primero calcular el balanceFactor del árbol y luego en función de esto aplicar la estrategia de rotación que corresponda.
#Entrada: El árbol binario de tipo AVL  sobre el cual se quiere operar.
#Salida: Un árbol binario de búsqueda balanceado. Es decir luego de esta operación se cumple que la altura (h) de su subárbol derecho e izquierdo difieren a lo sumo en una unidad.

def reBalance(AVLTree):
      calculateBalance(AVLTree)
      rebalanceR(AVLTree.root,AVLTree)

# Un rebalance Recursivo en donde analizo el balancefactor de los nodos más profundos y realizo las rotaciones adecuadas
# Calculo el balance factor del árbol después de una rotación, ya que una vez balanceado un subárbol que no estaba balanceado, el árbol vuelve a estar balanceado
def rebalanceR(currentnode,AVLTree):
      #Caso Base
      if currentnode == None:
            return

      #Caso general
      rebalanceR(currentnode.leftnode,AVLTree)
      rebalanceR(currentnode.rightnode,AVLTree)

      if currentnode.bf < -1:
            if currentnode.rightnode.bf > 0:
                  rotateRight(AVLTree,currentnode.rightnode)
                  rotateLeft(AVLTree,currentnode)
            else:
                  rotateLeft(AVLTree,currentnode)
      elif currentnode.bf > 1:
            if currentnode.leftnode.bf < 0:
                  rotateLeft(AVLTree,currentnode.leftnode)
                  rotateRight(AVLTree,currentnode.rightnode)
            else:
                  rotateRight(AVLTree,currentnode)
      else:
            return

      calculateBalance(AVLTree)            

