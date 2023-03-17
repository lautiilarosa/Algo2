from avltree import *

tree = AVLTree()
nodo1 = AVLNode()
nodo2 = AVLNode()
nodo3 = AVLNode()
nodo4 = AVLNode()
nodo5 = AVLNode()


tree.root = nodo1

nodo1.leftnode = nodo2
nodo2.parent = nodo1
nodo1.rightnode = nodo3
nodo3.parent = nodo1
nodo2.rightnode = nodo4
nodo4.parent = nodo2
nodo4.leftnode = nodo5
nodo5.parent = nodo4

nodo1.value = "A"
nodo2.value = "B"
nodo3.value = "C"
nodo4.value = "D"
nodo5.value = "E"

print("Se está por balancear el árbol")
reBalance(tree)
print("")
print("Se acaba de balancear el árbol")

print(tree.root.leftnode.value)

