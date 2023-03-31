from linkedlist import *
import math 

#Ejercicio 4
def middlesort(A):
    #Calculamos primero la longitud del Array,la posición del medio y el elemento posición
    length = len(A)
    middlepos = math.trunc(length/2)
    middle = A[middlepos]
    
    #Luego iniciamos varios contadores
    #minorscounter va a ser igual a la cantidad de menores en todo el array,minorsmiddlecounter igual a la cantidad de menores a la izq
    #minorspos va a ser una linkedlist con las posiciones de los menores y minorsposinverted la posicion de los menores pero de manera invertida
    minorspos = LinkedList()
    minorsposinverted = LinkedList()
    minorscounter = 0
    minorsmiddlecounter = 0
    j = 0
    
    #En este bucle verificamos los elementos menores y sumamos e insertamos respectivamente
    for i in range(0,length):
        if A[i] < middle:
            if i < middlepos:
                minorsmiddlecounter +=1
            minorscounter += 1
            insert(minorspos,i,j)
            add(minorsposinverted,i)
            j +=1

    #flag es la mitad de los menores
    flag = math.trunc(minorscounter/2)
    
    # Caso 1 : si la mitad de los menores es igual a la cantidad de menores que hay a la izquierda retornamos la lista.
    if flag == minorsmiddlecounter:
        return A
    
    # Caso 2: Si la mitad de los menores es menor que la cantidad de menores a la izq,hacemos un cambio de elementos entre los elementos mayores 
    #y menores utilizando como referencia la posicion de los menores con la linkedlist minorspos
    if flag < minorsmiddlecounter:
        currentnode = minorspos.head
        for i in range(middlepos+1,length):
            if A[i] > middle:
                aux = A[currentnode.value]
                A[currentnode.value] = A[i]
                A[i] = aux
                minorsmiddlecounter -=1
                if flag == minorsmiddlecounter:
                    return A
                else:
                    currentnode = currentnode.nextNode

    #Caso 3: Si la mitad de los menores es mayor que la cantidad de menores a la izq,hacemos un cambio de elementos como en el bucle anterior
    #Pero con la linkedlist minorsposinverted, ya que queremos las posiciones de los menores a la derecha del elemento del medio.
    if flag > minorsmiddlecounter:
        currentnode = minorsposinverted.head
        for i in range(0,middlepos-1):
            if A[i] > middle:
                aux = A[currentnode.value]
                A[currentnode.value] = A[i]
                A[i] = aux
                minorsmiddlecounter += 1
                if flag == minorsmiddlecounter:
                    return A
                else:
                    currentnode = currentnode.nextNode


    return 



#Ejercicio 5
#Tomamos el primer elemento del array y lo sumamos con cada uno que se encuentre también en el array y si es igual a n retornamos un verdadero
def contiene_suma(A,n):
    for i in range(0,len(A)-1):
        s = A[i]
        j = 1
        for j in range(j,len(A)-1):
            if s + A[j] == n:
                return True   
        j += 1
    return False        




array = [6,2,10,11,5,3,4,1,9]
middle = math.trunc(len(array)/2)
print("Lista antes del middle sort:",array)
print(" ")
middlesort(array)
print("Lista después del middle sort:",array)