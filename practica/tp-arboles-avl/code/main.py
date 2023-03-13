from avltree import *

tree = AVLTree()
nodo1 = AVLNode()
nodo2 = AVLNode()
nodo3 = AVLNode()
nodo4 = AVLNode()
nodo5 = AVLNode()
nodo6 = AVLNode()


tree.root = nodo5

nodo1.value = "A"
nodo2.value = "B"
nodo3.value = "C"
nodo4.value = "D"
nodo5.value = "E"
nodo6.value = "F"

nodo5.rightnode = nodo6
nodo6.parent = nodo5
nodo5.leftnode = nodo3
nodo3.parent = nodo5
nodo3.rightnode = nodo4
nodo4.parent = nodo3
nodo3.leftnode = nodo2
nodo2.parent = nodo3
nodo2.leftnode = nodo1
nodo1.parent = nodo2


calculateBalance(tree)

print(" ")
print(tree.root.bf)