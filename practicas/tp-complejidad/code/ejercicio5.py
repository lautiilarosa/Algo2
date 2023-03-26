def contiene_suma(A,n):
    for i in range(0,len(A)-1):
        s = A[i]
        j = 1
        for j in range(j,len(A)-1):
            if s + A[j] == n:
                return True   
        j += 1
    return False        



#Example if we have this array [2,7,5,6,1,4]

lista = [2,7,5,6,1,4]
boolean = contiene_suma(lista,9)
if boolean == True:
    print("Se encontró la suma que buscaba")
else:
    print("No se encontró la suma")
