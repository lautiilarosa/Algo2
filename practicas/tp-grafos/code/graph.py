from linkedlist import *
from myqueue import *
import math

class graphnode:
    vertex = None
    adjacentvertex = None
    color = None
    parent = None
    distance = None
    time = None

#createGraph(V,A)
#Descripción: Implementa la operación crear grafo
#Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
#Salida: retorna el nuevo grafo
def createGraph(V,A):
    if len(V) == 0:
        return 
    
    graph = []
    for i in range(0,len(V)):
        newNode = graphnode()
        newNode.vertex = V[i]
        newNode.adjacentvertex = []
        graph.append(newNode)

    if len(A)>0:
        for j in range(len(A)):
            for k in range(len(graph)):
                if A[j][0] == graph[k].vertex:
                    graph[k].adjacentvertex.append(A[j][1])
                elif A[j][1] == graph[k].vertex:
                    graph[k].adjacentvertex.append(A[j][0])
    return graph

#existpath(Grafo,v1,v2)
#Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
#Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
#Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.

def existpath(Grafo,v1,v2):
    #Buscamos si existe un camino entre v1 y v2
    list = []
    q = LinkedList()
    return existpathR(Grafo,v1,v2,list,q)

def existpathR(graph,v,v2,list,q):
    indexV = searchvertex(graph,v)
    vertexadjacentList = graph[indexV].adjacentvertex
    if len(vertexadjacentList) != 0:
        list.append(v)
        for i in range(0,len(vertexadjacentList)):
            if v2 == vertexadjacentList[i]:
                return True
            if isinlist(list,vertexadjacentList[i]) == False:
                enqueue(q,vertexadjacentList[i])
        while q.head != None:
            nextvertex = dequeue(q)
            nextvertexQ = LinkedList()
            if existpathR(graph,nextvertex,v2,list,nextvertexQ) == True: 
                return True
    return False
        
def searchvertex(graph,v):
    for i in range(0,len(graph)):
        if graph[i].vertex == v:
            return i
    return 

def isinlist(list,v):
    for i in range(0,len(list)):
        if list[i] == v:
            return True
    return False    

#isConnected(Grafo)
#Descripción: Implementa la operación es conexo 
#Entrada: Grafo con la representación de Lista de Adyacencia.
#alida: retorna True si existe camino entre todo par de vértices, False en caso contrario.
def isConnected(Grafo):
    for i in range(0,len(Grafo)):
        vertex = Grafo[i].vertex
        j = i + 1 
        for j in range(j,len(Grafo)):
            if existpath(Grafo,vertex,Grafo[j].vertex) == False:
                return False
    return True
#isTree(Grafo): 
#Descripción: Implementa la operación es árbol 
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: retorna True si el grafo es un árbol.

def isTree(graph):
    if isConnected(graph) == True and totaledges(graph) == len(graph)-1:
        return True
    else:
        return False

def totaledges(graph):
    total = 0
    for i in range(0,len(graph)):
        total = total + len(graph[i].adjacentvertex)
    return math.trunc(total/2)

#isComplete(Grafo): 
#Descripción: Implementa la operación es completo 
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: retorna True si el grafo es completo.
def isComplete(graph):
    gradostotales = len(graph)-1
    for i in range(0,len(graph)):
        if len(graph[i].adjacentvertex) != gradostotales:
            return False
    return True    

#def convertTree(Grafo)
#Descripción: Implementa la operación es convertir a árbol 
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.
def convertTree(graph):
    tree_edges = []
    visited = []
    cola = LinkedList()
    for i in range(0,len(graph)):
        visited.append(graph[i].vertex)
        enqueue(cola,graph[i])
        while cola != None:
            currentnode = dequeue(cola)
            for j in range(0,len(currentnode.adjacentvertex)):
                if len(currentnode.adjacentvertex) > 0:
                    if currentnode.adjacentvertex[j] not in visited:
                        vecino = graph[searchvertex(graph,currentnode.adjacentvertex[j])]
                        visited.append(currentnode.adjacentvertex[j])
                        enqueue(cola,vecino)
                    else:
                        if searchinq(cola,currentnode.adjacentvertex[j]) == False:
                            graphcopy = graph
                            indexvecino = graph[searchvertex(graph,currentnode.adjacentvertex[j])]
                            indexcurrentnode = searchvertex(graph,currentnode.vertex)
                            graphcopy[indexcurrentnode].adjacentvertex.remove(currentnode.adjacentvertex[j])
                            graphcopy[indexvecino].adjacentvertex.remove(currentnode.vertex)
                            if isTree(graphcopy) == True:
                                tree_edges.append([currentnode.vertex,vecino.vertex])
    return tree_edges                   

def searchinq(q,value):
    currentnode = q.head
    while currentnode != None:
        if currentnode.value == value:
            return True
        currentnode = currentnode.nextNode
    return False    


#def countConnections(Grafo):
#Descripción: Implementa la operación cantidad de componentes conexas 
#Entrada: Grafo con la representación de Lista de Adyacencia.
#Salida: retorna el número de componentes conexas que componen el grafo.
def countConncections(graph):
    visited = []
    components = 0
    for i in range(0,len(graph)):
        if graph[i].vertex not in visited:
            busquedaenancho(graph,graph[i],visited)
            components = components + 1
    return components        


def busquedaenancho(graph,node,visited):
    visited.append(node.vertex)
    for j in range(0,len(node.adjacentvertex)):
        if node.adjacentvertex[j] not in visited:
            vecino = graph[searchvertex(graph,node.adjacentvertex[j])]
            busquedaenancho(graph,vecino,visited)


#def convertToBFSTree(Grafo, v):
#Descripción: Convierte un grafo en un árbol BFS
#Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
#Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
def convertToBFSTree(graph,v):
    if isConnected(graph) == False:
        return print("No es conexo")
    
    for i in range(0,len(graph)):
        graph[i].color = "White"
        graph[i].distance = 0
    bfslist = []
    v.parent = None
    v.color = "Grey"
    queue = LinkedList()
    enqueue(queue,v)
    while queue.head != None:
        currentnode = dequeue(queue)
        adjacentlist = []
        if currentnode.parent != None:
            adjacentlist.append(currentnode.parent.vertex)
        for j in range(0,len(currentnode.adjacentvertex)):
            neighbor = graph[searchvertex(graph,currentnode.adjacentvertex[j])]
            if neighbor.color == "White":
                adjacentlist.append(neighbor.vertex)
                neighbor.color = "Grey"
                neighbor.distance = currentnode.distance + 1
                neighbor.parent = currentnode
                enqueue(queue,neighbor)
        newnode = graphnode()
        newnode.vertex = currentnode.vertex
        newnode.adjacentvertex = adjacentlist
        bfslist.append(newnode)
        currentnode.color = "Black"
    return bfslist    

#def convertToDFSTree(Grafo, v):
#Descripción: Convierte un grafo en un árbol DFS
#Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
#Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.
def convertToDFSTree(graph,v):
    for i in range(0,len(graph)):
        graph[i].color = "White"
    dfslist = []
    time = 0
    DFSr(graph,v,dfslist,time)
    for j in range(0,len(graph)):
        if graph[j].color == "White":
            DFSr(graph,graph[j],dfslist,time)
    inv = list(reversed(dfslist))
    return inv        

def DFSr(graph,v,dfslist,time):
    adjacentlist = []
    node = graphnode()
    node.vertex = v.vertex
    node.adjacentvertex = adjacentlist
    if v.parent != None:
        adjacentlist.append(v.parent.vertex)

    time = time + 1
    v.color = "Grey"
    v.distance = time
    for i in range(0,len(v.adjacentvertex)):
        neighbor = graph[searchvertex(graph,v.adjacentvertex[i])]
        if neighbor.color == "White":
            adjacentlist.append(neighbor.vertex)
            neighbor.parent = v
            DFSr(graph,neighbor,dfslist,time) 
    time = time + 1
    v.time = time
    v.color = "Black"
    dfslist.append(node)

#def bestRoad(Grafo, v1, v2):
#Descripción: Encuentra el camino más corto, en caso de existir, entre dos vértices.
#Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices del grafo.
#Salida: retorna la lista de vértices que representan el camino más corto entre v1 y v2. La lista resultante contiene al inicio a v1 y al final a v2. En caso que no exista camino se retorna la lista vacía.
def bestRoad(graph,v1,v2):
    for i in range(0,len(graph)):
        graph[i].color = "White"
        graph[i].distance = 0
    v1.color = "Grey"
    queue = LinkedList()
    enqueue(queue,v1)
    road = []
    while queue.head != None:
        currentnode = dequeue(queue)
        road.append(currentnode.vertex)
        for j in range(0,len(currentnode.adjacentvertex)):
            neighbor = graph[searchvertex(graph,currentnode.adjacentvertex[j])]
            if neighbor.vertex == v2.vertex:
                road.append(v2.vertex)
                return road
            if neighbor.color == "White":
                neighbor.color = "Grey"
                neighbor.distance = currentnode.distance + 1
                neighbor.parent = currentnode
                enqueue(queue,neighbor)
        currentnode.color = "Black"
    return     







vertices = [1,2,3,4,5,6]
aristas = [[1,2],[2,3],[2,4],[3,5],[4,5]]
grafo = createGraph(vertices,aristas)

i = 0
j = 5
print(" ")
camino = bestRoad(grafo,grafo[i],grafo[j])
if camino != None:
    print("El camino entre el vertice:",grafo[i].vertex,"y el vértice:",grafo[j].vertex,"es:",camino)
else:
    print("No se encontró un camino")

