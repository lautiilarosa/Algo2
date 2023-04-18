import random

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



#Ejercicio 4
def ispermutation(s,p):
    #Si la longitud de las dos cadenas son distintas, no es una permutación
    if len(s) != len(p) or s == p: return False
    hashtable = []
    hashtable = generartabla(hashtable)
    asciiS = 0
    asciiP = 0
    for i in range(0,len(s)):
        asciiS = asciiS + ord(s[i])
        asciiP = asciiP + ord(p[i])
    #Con el codigo ascii como key inserto una cadena y luego busco en la tabla la otra key generado por la otra cadena
    hashinsert(hashtable,asciiS,s)
    string = hashsearch(hashtable,asciiP)
    if string != None:
        if string == s:
            return True
    return False

#Generar una table con el tamaño de slots primo aleatorio
def generartabla(table):
    list = [2]
    for i in range(3,100,2):
        for j in range(3,int(i**.5)+1,2):
            if i%j==0:
                break
        else:         
            list.append(i)
    index = random.randint(0,len(list)-1)
    for i in range(0,list[index]):
        table.append(None)
    return table


#Ejercicio 5
def uniquelist(list):
    hashtable = []
    hashtable = generartabla(hashtable)
    hashinsert(hashtable,list[0],list[0])
    for i in range(1,len(list)):
        if hashsearch(hashtable,list[i]) != None:
            return False
        hashinsert(hashtable,list[i],list[i])
    return True


#Ejercicio 7
def compressed(s):
    #Hago toda la cadena en minúscula y inicializo una cadena vacía para ir agregando la cadena comprimida
    s = s.lower()
    compressedstring = ""
    character = s[0]
    j = 1
    for i in range(1,len(s)):
        if s[i] == character:
            j += 1
        else:
            compressedstring = compressedstring + character
            compressedstring = compressedstring + str(j)
            j = 1
            character = s[i]
    compressedstring = compressedstring + character
    compressedstring = compressedstring + str(j)
    #Si la longitud de la cadena comprimida es mayor o igual que la cadena original retorno s
    if len(compressedstring) >= len(s):
        return s
    return compressedstring
    
#Ejercicio 8
def ocurrencia(p,a):
    sizep = len(p)
    sizea = len(a)

    hashtable = []
    hashtable = generartabla(hashtable)
    keyp = 0
    for i in range(0,sizep):
        keyp = keyp + (ord(p[i]) * pow(256,sizep-1-i))
    hashinsert(hashtable,keyp,p)
    
    hashtexto = 0
    for i in range(0,sizep):
        hashtexto = hashtexto + (ord(a[i]) * pow(256,sizep-1-i))
    
    for i in range(0,sizea - sizep + 1):
        if hashsearch(hashtable,hashtexto) != None:
            if a[i:i+sizep] == p:
                return i
        if i < sizea - sizep:
            hashtexto = (hashtexto - ord(a[i]) * pow(256,sizep-1)) * 256 + ord(a[i+sizep])
    return -1

#Ejercicio 9
def subconjunto(t,s):
    lens = len(s)
    lent = len(t)
    hashtable = []
    hashtable = generartabla(hashtable)
    
    keys = 0
    for i in range(0,lens):
        keys = keys + (s[i] * pow(10,lens-1-i))
    hashinsert(hashtable,keys,s)

    keyt = 0
    listT = []    
    for i in range(0,lens):
        keyt = keyt + (t[i] * pow(10,lens-1-i))
        listT.append(t[i])
    
    for i in range(0,lent-lens + 1):
        if hashsearch(hashtable,keyt) != None:
            if listT == s:
                return True
        if i < lent-lens:
            keyt = (keyt - t[i] * pow(10,lens-1)) * 10 + t[i+lens]
            listT.pop(0)
            listT.append(t[i+lens])
    return False        


s = [1,2,3,4]
t = [15,18,1,2,3,4]
if subconjunto(t,s) == True:
    print("Se encontró el subconjunto")
else:
    print("No se encontró el subconjunto")