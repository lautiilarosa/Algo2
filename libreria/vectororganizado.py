def minvec(vector):
  min=vector[0]
  for i in range(0,len(vector)):
    if (min > vector[i]):
      min = vector[i]
  return min

def maxvec(vector):
  max=vector[0]
  for i in range(0,len(vector)):
    if (max < vector[i]):
      max = vector[i]
  return max    

def medvec(vector,min,max):
  med=vector[0]
  for i in range(0,len(vector)):
    if (vector[i] != min and vector[i] != max):
      med = vector[i]
  return med


#Esto es un comentario normal
print("Hola")

      
      