class dictionarynode:
    value = None
    key = None

#Función hash de la división
def hashfunction(k,m):
    return (k%m)

#Insert del hash 
def hashinsert(D,key,value):
    node = dictionarynode()
    node.value = value
    node.key = key
    hashindex = hashfunction(key,len(D))
    if D[hashindex] == None:
        list = []
        list.append(node)
        D[hashindex] = list
    else:
        D[hashindex].append(node)
    return key

#Search del hash
def hashsearch(D,key):
    hashindex = hashfunction(key,len(D))
    if D[hashindex] == None: return
    for i in range(0,len(D[hashindex])):
        if key == D[hashindex][i].key:
            return key
    return 

#Delete del hash
def hashdelete(D,key):
    hashindex = hashfunction(key,len(D))
    if D[hashindex] == None: return
    for i in range(0,len(D[hashindex])):
        if key == D[hashindex][i].key:
            D[hashindex].pop(i)
            if len(D[hashindex]) == 0:
                D[hashindex] = None
            return D
    return     



