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
            fillword(T.root.children.head,element,0)
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
                    if i == len(element):
                        currentnode.value.isendofword = True
                        return T
                    
                    list = currentnode.value.children
                    if list == None:
                        currentnode.value.children = linkedlist.LinkedList()
                        list = currentnode.value.children
                        linkedlist.add(list,trienode())
                        list.head.value.parent = currentnode
                        end = True
                    else:
                        currentnode = list.head
                elif currentnode.nextNode == None:
                    linkedlist.add(list,trienode())
                    list.head.value.parent = currentnode.value.parent
                    end = True
                else:
                    currentnode = currentnode.nextNode

            fillword(list.head,element,i)
            return T            



#Agregar la palabra en el árbol
def fillword(currentnode,word,i):
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





arbol = trie()
word1 = "hola"
word2 = "ho"
word3 = "papu"
word4 = "hoz"
word5 = "holas"

