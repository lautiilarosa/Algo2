from algo1 import *
import math

def search(array,element):
  index=None
  i=0
  finish=False
  while i <= len(array)-1 and finish == False:
    if array[i] == element:
      index = i
      finish = True
    else:
      i += 1
  return index    
 
def insert(array,element,position):
  if (position >= 0 and position <= len(array)-1):
    for j in range(len(array)-1,position,-1):
      array[j] = array[j-1]  
    array[position] = element
    return position
  else:
    return None

def delete(array,element):
  index = search(array,element)
  if index != None:
    for j in range(index,len(array)-1):
      array[j] = array[j+1]
    array[len(array)-1] = None
    return index
  else:
    return 

def length(array):
  cont=0
  for i in range(0,len(array)):
    if array[i] != None:
      cont += 1
  return cont    

def access(array,position):
  return array[position]
