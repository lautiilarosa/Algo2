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
            T.root.isendofword = True
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
        return searchR(T.root.children.head,element,0)
    else:
        return 
    
def searchR(currentword,word,index):
    if index == len(word) or currentword == None:
        return False

    if currentword.value.key == word[index]:
        if currentword.value.isendofword == True and index == len(word)-1:
            return True
        elif currentword.value.children == None:
            return False
        else:
            return searchR(currentword.value.children.head,word,index+1)
    else:
        return searchR(currentword.nextNode,word,index)    


#delete(T,element)
#Descripción: Elimina un elemento se encuentre dentro del Trie
#Entrada: El Trie sobre la cual se quiere eliminar el elemento (Trie)  y el valor del elemento (palabra) a  eliminar.
#Salida: Devuelve False o True  según se haya eliminado el elemento.

def searchNode(currentword,word,index):
    if index == len(word) or currentword == None:
        return 

    if currentword.value.key == word[index]:
        if currentword.value.isendofword == True and index == len(word)-1:
            return currentword
        elif currentword.value.children == None:
            return 
        else:
            return searchNode(currentword.value.children.head,word,index+1)
    else:
        return searchNode(currentword.nextNode,word,index)    
    

def delete(T,element):
    #Buscamos la última letra de la palabra si es que existe
    node = searchNode(T.root.children.head,element,0)
    if node != None:
        #Caso donde la palabra esta incluida en otra
        if node.value.children != None:
            node.value.isendofword = False
            return True
        node.value.isendofword = False
        return deleteR(node,T)
    

def deleteR(currentnode,T):
    #Caso donde la palabra a eliminar tiene una palabra en su cadena
    if currentnode.value.isendofword == True:
        return True
    
    parent = currentnode.value.parent
    #Si el parent es justo la raíz del arbol eliminamos la letra y hacemos none al children de la raíz SI LA LISTA QUEDÓ VACÍA
    if parent == T.root:
        linkedlist.delete(parent.children,currentnode.value)
        if parent.children.head == None:
            parent.children = None
            return True
        return True
    
    list = currentnode.value.parent.value.children
    linkedlist.delete(list,currentnode.value)
    if list.head != None:
        return True
    
    parent.value.children = None
    return deleteR(parent,T)


#Ejercicio 5
#Implementar un algoritmo que dado los Trie T1 y T2 devuelva True si estos pertenecen al mismo documento y False en caso contrario

def sametrie(t1,t2):
    t1words = []
    word = ""
    getallwordR(t1.root.children.head,word,t1words)
    for i in range(0,len(t1words)):
        if search(t2,t1words[0]) == False:
            return False
    return True    

#Función que retorna una lista con todas las palabras del trie
def getallwordR(currentnode,word,list):
    if currentnode == None:
        return
    word = word + currentnode.value.key
    if currentnode.value.isendofword == True:
        list.append(word)
    
    if currentnode.value.children != None:
        getallwordR(currentnode.value.children.head,word,list)

    getallwordR(currentnode.nextNode,word[:-1],list)



#Ejercicio 6
#Implemente un algoritmo que dado el Trie T devuelva True si existen en el documento T dos cadenas invertidas. Dos cadenas son invertidas si se leen de izquierda a derecha y contiene los mismos caracteres que si se lee de derecha a izquierda, ej: abcd y dcba son cadenas invertidas, gfdsa y asdfg son cadenas invertidas, sin embargo abcd y dcka no son invertidas ya que difieren en un carácter.

def inverted(T):
    twords = []
    word = ""
    getallwordR(T.root.children.head,word,twords)
    newlist = []
    for i in range(0,len(twords)):
        wordinverted = twords[i]
        newlist.append(wordinverted[::-1])
    
    finalist = []
    for i in range(0,len(newlist)):
        if search(T,newlist[i]) == True:
            finalist.append(newlist[i])

    if len(finalist) != 0:
        print("Se encuentran al menos dos cadenas invertidas en el trie")
        print(finalist)
        return
    print("No se encontraron cadenas invertidas")        


#Ejercicio 7
#implementar la función autoCompletar(Trie, cadena) dentro del módulo trie.py, que dado el árbol Trie T y la cadena “pal” devuelve la forma de auto-completar la palabra

def searchpattern(currentnode,p,index):
    if currentnode == None:
        return 
    
    if currentnode.value.key == p[index]:
        if index == len(p)-1:
            return currentnode
        if currentnode.value.children != None:
            return searchpattern(currentnode.value.children.head,p,index+1)
        return 
    return searchpattern(currentnode.nextNode,p,index)


def autoCompletar(Trie,cadena):
    pattern = searchpattern(Trie.root.children.head,cadena,0)
    if pattern == None:
        print("No se encontraron palabras")
        return 
    if pattern.value.children == None:
        print("")
        return 
    word = cadena
    list = []
    getallwordR(pattern.value.children.head,word,list)
    print(list)




