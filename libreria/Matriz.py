from algo1 import * 
import math
import random

#input matriz

def input_matriz_int(matriz):
  row=len(matriz)
  columns=len(matriz[0])
  for i in range(0,row):
    for j in range(0,columns):
      matriz[i][j]=input_int(f"Ingrese el valor ubicado en {i+1},{j+1}:")
  print_matriz(matriz)
  print(" ")
  
def input_matriz_real(matriz):
  row=len(matriz)
  columns=len(matriz[0])
  for i in range(0,row):
    for j in range(0,columns):
      matriz[i][j]=input_real(f"Ingrese el valor ubicado en {i+1},{j+1}:") 
  print_matriz(matriz)
  print(" ")

def input_matriz_str(matriz):
  row=len(matriz)
  columns=len(matriz[0])
  for i in range(0,row):
    for j in range(0,columns):
      matriz[i][j]=input_str(f"Ingrese el valor ubicado en {i+1},{j+1}:")
  print_matriz(matriz)
  print(" ")
  
#print matriz

def print_matriz(matriz):
  row=len(matriz)
  columns=len(matriz[0])
  for i in range(0,row):
    print(" ")
    for j in range(0,columns):
      print(matriz[i][j],end=" ")
    print(" ")  

#operations 

def addition_matriz(matriz1,matriz2):
  row1=len(matriz1)
  row2=len(matriz2)
  columnns1=len(matriz1[0])
  columns2=len(matriz2[0])

  if row1 == row2 and columns1 == columns2:
    matriz3=Array(row1,Array(columns1,0))
    for i in range (0,row1):
      for j in range (0,columns1):
        matriz3[i][j]=matriz1[i][j] + matriz2[i][j]
    return matriz3
  else:
    return



def substraction(matriz1,matriz2):
  row1=len(matriz1)
  row2=len(matriz2)
  columns1=len(matriz1[0])
  columns2=len(matriz2[0])

  if row1 == row2 and columns1 == columns2:
    matriz3=Array(row1,Array(columns1,0))
    for i in range (0,row1):
      for j in range (0,columns1):
        matriz3[i][j]=matriz1[i][j] - matriz2[i][j]  
    return matriz3
  else:
    return


def product_matriz(matriz1,matriz2):
  row1=len(matriz1)
  row2=len(matriz2)
  columns1=len(matriz1[0])
  columns2=len(matriz2[0])
  
  if columns1 == row2:
    matriz3=Array(row1,Array(columns2,0))
    in_matriz(matriz3)

    for i in range(0,row1):
      for j in range(0,columns2):
        for n in range(0,row2):
          matriz3[i][j] += matriz1[i][n] * matriz2[n][j]
    return matriz3    
  else:
    return

def product_matriz_vector(matriz,vector):
  row1=len(vector)
  row2=len(matriz)
  columns2=len(matriz[0])

  if row1 == columns2:
    result=Array(row2,0)
    for i in range(0,row2):
      for j in range(0,columns2):
        result[i] = matriz[i][j] * vector[j]
    return result 
  else:
    return

def strictly_dominant_diagonal_row(matriz):
  row=len(matriz)
  column=len(matriz)
  norm=0
  cont=0

  for i in range(0,row):
    diagonal=matriz[i][i]
    for j in range(0,column):
      if i != j:
        norm=norm+math.pow(matriz[i][j],2)
    if diagonal > norm:
      cont=cont+1

  if cont == row:
    v=True
  else:
    v=False

  return v

def transposed(matriz):
  row=len(matriz)
  column=len(matriz[0])

  tran=Array(row,Array(column,0))
  for i in range(0,row):
    for j in range(0,column):
      tran[i][j]=matriz[j][i]

  return tran 

def upper_triangular_matrix(matriz):
  row=len(matriz)
  column=len(matriz[0])
  cont=0
  v=False

  for i in range(0,row):
    for j in range(0,column):
      if i > j:
        if matriz[i][j] != 0:
          cont=cont+1
  if cont == 0:
    v=True
  else:
    v=False
  return v  

def lower_triangular_matrix(matriz):
  row=len(matriz)
  column=len(matriz[0])
  cont=0

  for i in range(0,row):
    for j in range(0,column):
      if j > i:
        if matriz[i][j] != 0:
          cont=cont+1
  if cont == 0:
    v=True
  else:
    v=False
  return v

def determinant(matriz):
  row=len(matriz)
  column=len(matriz[0])
  det = 1
  if row != column:
    return None
  else:
    for i in range(0,row):
      for j in range(0,column):
        if i == j :
          det *= matriz[i][j]
    return det      
  
#initialization
def matriz_int(matriz):
  row=len(matriz)
  column=len(matriz[0])

  for i in range(0,row):
    for j in range(0,column):
      matriz[i][j]=random.randint(0,100)

def matriz_real(matriz):
  row=len(matriz)
  column=len(matriz[0])
  for i in range(0,row):
    for j in range(0,column):
      matriz[i][j]=random.uniform(0,100)

def initialize_matriz(matriz):
  for i in range(0,len(matriz)):
    for j in range(0,len(matriz[0])):
      matriz[i][j] = 0