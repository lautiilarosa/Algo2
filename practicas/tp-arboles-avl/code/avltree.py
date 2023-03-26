
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


# Función Recursiva que calcula el balanceo de un nodo raíz

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


#Ejercicio 4:
#Implementar la operación insert() en  el módulo avltree.py garantizando que el árbol  binario resultante sea un árbol AVL. 

def insert(AVLTree, element, key):
  newnode = AVLNode()
  newnode.value = element
  newnode.key = key
  if AVLTree.root != None:
    insertR(newnode, AVLTree.root)
    return reBalance(AVLTree)
  else:
    newnode.bf = 0
    AVLTree.root = newnode


def insertR(newnode, currentnode):
  if newnode.key != currentnode.key:
    if newnode.key > currentnode.key:
      if currentnode.rightnode == None:
        currentnode.rightnode = newnode
        newnode.parent = currentnode
        return 
      else:
        return insertR(newnode, currentnode.rightnode)
    else:
      if currentnode.leftnode == None:
        currentnode.leftnode = newnode
        newnode.parent = currentnode
        return 
      else:
        return insertR(newnode, currentnode.leftnode)
  else:
    return
  

#Ejercicio 5:
#Implementar la operación delete() en  el módulo avltree.py garantizando que el árbol  binario resultante sea un árbol AVL.

def deleteAVL(AVL, element):
  deletenode = accessnodeE(AVL.root, element)
  if deletenode != None:
    deleteNodeCases(AVL, deletenode)
    return reBalance(AVL)
  else:
    return


def deleteNodeCases(AVL, deletenode):
  key = deletenode.key

  #Caso 1: El nodo a eliminar es una hoja
  if deletenode.leftnode == None and deletenode.rightnode == None:
    if deletenode.parent != None:
      if deletenode.parent.leftnode != None and deletenode.parent.leftnode == deletenode:
        deletenode.parent.leftnode = None
        return key
      else:
        deletenode.parent.rightnode = None
        return key
    else:
      AVL.root = None
      return key

  #Caso 2: El nodo a eliminar tiene un hijo

  if deletenode.leftnode != None and deletenode.rightnode == None:
    if deletenode.parent != None:
      if deletenode.parent.leftnode != None and deletenode.parent.leftnode == deletenode:
        deletenode.parent.leftnode = deletenode.leftnode
      else:
        deletenode.parent.rightnode = deletenode.leftnode

      deletenode.leftnode.parent = deletenode.parent
      return key

    else:
      AVL.root = deletenode.leftnode
      deletenode.leftnode.parent = None
      return key

  if deletenode.rightnode != None and deletenode.leftnode == None:
    if deletenode.parent != None:
      if deletenode.parent.leftnode != None and deletenode.parent.leftnode == deletenode:
        deletenode.parent.leftnode = deletenode.rightnode
      else:
        deletenode.parent.rightnode = deletenode.rightnode
        
      deletenode.rightnode.parent = deletenode.parent
      return key

    else:
      AVL.root = deletenode.rightnode
      deletenode.rightnode.parent = None
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
  changenode = smaller(deletenode.rightnode)
  deletenode.value = changenode.value
  deletenode.key = changenode.key

  if changenode.parent.rightnode == changenode:
    changenode.parent.rightnode = None
  else:
    changenode.parent.leftnode = None

  return key  


def bigger(node):
  if node.rightnode != None:
    return bigger(node.rightnode)
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
      rightnode = accessnodeE(node.rightnode, element)
      if rightnode != None:
        return rightnode

      leftnode = accessnodeE(node.leftnode, element)
      if leftnode != None:
        return leftnode
  else:
    return
