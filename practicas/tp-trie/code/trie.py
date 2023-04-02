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
    if T != None :
        #Caso 1: el árbol esta vacio
        if T.root == None:
            T.root = trienode()
            T.root.children = linkedlist.LinkedList()
            linkedlist.add(T.root.children,trienode())
            T.root.children.head.value.parent = T.root
            fillword(T.root.children.head,element,0)
            return T
        #Caso 2: el árbol no esta vacío 
        #Acá agregar la funcion search para verificar si va a ingresar una palabra ya ingresada :)
        #En el caso que no esté ingresada usamos lo de abajo.   
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
                currentnode = list.head
            elif currentnode.value.isendofword == True:
                linkedlist.add(list,trienode())
                list.head.value.parent = currentnode.value.parent
                end = True
            else:
                if currentnode.nextNode != None:
                    currentnode = currentnode.nextNode
                else:
                    linkedlist.add(list,trienode())
                    list.head.value.parent = currentnode.value.parent
                    end = True

        fillword(list.head,element,i)
        return T
    else:  
        return
    

#Insertamos una palabra en el trie    
def fillword(currentnode,element,i):
    for i in range(i,len(element)):
        currentnode.value.key = element[i]
        currentnode.value.children = linkedlist.LinkedList()
        linkedlist.add(currentnode.value.children,trienode())
        currentnode.value.children.head.value.parent = currentnode
        currentnode = currentnode.value.children.head

    currentnode.value.isendofword = True
    return     



arbol = trie()
word = "Hola"
insert(arbol,word)
word2 = "papu"
insert(arbol,word2)
word3 = "papus"
insert(arbol,word3)

currentnode = arbol.root.children.head
for i in range(0,len(word2)):
    print(currentnode.value.key,end="")
    currentnode = currentnode.value.children.head

#print(" ")
#print(currentnode.value.parent.value.parent.value.children.head.value.isendofword)
print(" ")
currentnode = currentnode.value.parent
print(currentnode.value.children.head.nextNode.value.isendofword)