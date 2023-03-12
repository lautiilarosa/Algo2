from algo1 import *
import math
import random

#input int
def input_vector_int(vector):
  for i in range(0,len(vector)):
    vector[i]=input_int(f"Ingrese el componente número {i+1} del vector:")
  print("Su vector es el siguiente:",vector)
  print(" ")
    
#input real
def input_vector_real(vector):
  for i in range(0,len(vector)):
    vector[i]=input_real(f"Ingrese el componente número {i+1} del vector:")
  print("Su vector es el siguiente:",vector)
  print(" ")

#check dimension
def check_dimension(vector1,vector2):
  v=False
  amount1=0
  amount2=0
  for i in range(0,len(vector1)):
    amount1=amount1+1

  for i in range(0,len(vector2)):
    amount2=amount2+1

  if amount1 == amount2:
    v=True
  else:
    v=False

  return v  

#operations
  
def module_vector(vector):
  media=0
  for i in range(0,len(vector)):
    media=media+math.pow(vector[i],2)
  media=math.sqrt(media)
  return media

def scalar_product(vector1,vector2):
  mod1=module_vector(vector1)
  mod2=module_vector(vector2)
  mods=mod1*mod2
  product=0

  for i in range(0,len(vector1)):
    product=product + (vector1[i] * vector2[i])

  res=math.acos(product/mods)
  return res

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
        
  