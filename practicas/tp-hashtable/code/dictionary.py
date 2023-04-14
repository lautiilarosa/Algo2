from algo1 import *
import linkedlist

class dictionarynode:
    value = None
    key = None

def hashfunction(k,m):
    return (k%m)

#insert(D,key, value)
def hashinsert(D,key,value):
    node = dictionarynode()
    node.value = value
    node.key = key
    hashvalue = hashfunction(key,len(D))
    if D[hashvalue] == None:
        newlist = linkedlist.LinkedList()
        linkedlist.add(newlist,node)
        D[hashvalue] = newlist
        return D
    linkedlist.add(D[hashvalue],node)

#search(D,key)
def hashsearch(D,key):
    hashvalue = hashfunction(key,len(D))
    if D[hashvalue] == None:return None
    currentnode = D[hashvalue].head
    while currentnode != None:
        if currentnode.value.key == key:
            return key
        currentnode = currentnode.nextNode
    return None    

#delete(D,key)
def hashdelete(D,key):
    hashvalue = hashfunction(key,len(D))
    if D[hashvalue] == None:return None
    currentnode = D[hashvalue].head
    while currentnode != None:
        if currentnode.value.key == key:
            linkedlist.delete(D[hashvalue],currentnode.value)
            return D
        currentnode = currentnode.nextNode
    return None    


dictionary = []
for i in range(0,9):
    dictionary.append(None)

print("")
hashinsert(dictionary,5,"frank")
hashinsert(dictionary,33,"lautaro")
hashinsert(dictionary,15,"nicolas")
hashdelete(dictionary,5)

