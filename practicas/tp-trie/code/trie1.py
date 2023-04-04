import linkedlist

class trie:
    root = None

class trienode:
    parent = None
    children = None
    key = None
    isendofword = False


#insert(T,element) 
#Descripción: insert un elemento en T, siendo T un Trie.
#Entrada: El Trie sobre la cual se quiere agregar el elemento (Trie)  y el valor del elemento (palabra) a  agregar.
#Salida:  No hay salida definida

def insert(T,element):
    if T != None:
        #Caso 1: El árbol está vacío
        if T.root == None:
            T.root = trienode()
            T.root.children = linkedlist.LinkedList()
            linkedlist.add(T.root.children,trienode())
            T.root.children.head.value.parent = T.root
            insertword(T.root.children.head,element,0)
            return T
        #Caso 2: El árbol no está vacio
        else:
            end = False
            i = 0
            list = T.root.children
            currentnode = list.head
            while end == False:
                if currentnode.value.key == element[i]:
                    i += 1
                    #La palabra está incluida dentro de otra
                    if i == len(element):
                        currentnode.value.isendofword = True
                        return T
                    
                    list = currentnode.value.children
                    #Se agrega una nueva lista en el children del nodo
                    if list == None:
                        currentnode.value.children = linkedlist.LinkedList()
                        list = currentnode.value.children
                        linkedlist.add(list,trienode())
                        list.head.value.parent = currentnode
                        end = True
                    else:
                        currentnode = list.head
                elif currentnode.nextNode == None:
                    #Se necesitan nodos extras en la lista
                    linkedlist.add(list,trienode())
                    list.head.value.parent = currentnode.value.parent
                    end = True
                else:
                    currentnode = currentnode.nextNode

            insertword(list.head,element,i)
            return T            



#Agregar la palabra en el árbol
def insertword(currentnode,word,i):
    for i in range(i,len(word)):
        currentnode.value.key = word[i]
        if i == len(word)-1:
            currentnode.value.isendofword = True
            return 
        currentnode.value.children = linkedlist.LinkedList()
        linkedlist.add(currentnode.value.children,trienode())
        currentnode.value.children.head.value.parent = currentnode
        currentnode = currentnode.value.children.head


#search(T,element)
#Descripción: Verifica que un elemento se encuentre dentro del Trie
#Entrada: El Trie sobre la cual se quiere buscar el elemento (Trie)  y el valor del elemento (palabra)
#Salida: Devuelve False o True  según se encuentre el elemento.

def search(T,element):
    if T.root != None and len(element) != 0:
        return searchR(T.root.children,T.root.children.head,element,0)
    else:
        return 
    
def searchR(currentlist,currentword,word,index):
    if index == len(word) or currentword == None:
        return False

    if currentword.value.key == word[index]:
        if currentword.value.isendofword == True and index == len(word)-1:
            return True
        elif currentword.value.children == None:
            return False
        else:
            return searchR(currentword.value.children,currentword.value.children.head,word,index+1)
    else:
        return searchR(currentlist,currentword.nextNode,word,index)    





arbol = trie()
insert()