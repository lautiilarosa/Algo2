from algo1 import *
from linkedlist import *
from mystack import *
from myqueue import *

class PriorityQueue:
  head=None

class PriorityNode:
  value=None
  nextNode=None
  priority=None


def enqueue_priority(Q,element,priority):
  newnode = PriorityNode()
  newnode.value = element
  newnode.priority = priority
  index = 0
  if Q.head == None:
    Q.head = newnode
    return index
  elif priority > Q.head.priority:
    newnode.nextNode = Q.head
    Q.head = newnode
    return index
  else:
    index += 1
    previousnode = Q.head
    currentnode = previousnode.nextNode
    while currentnode != None:
      if priority > currentnode.priority:
        newnode.nextNode = currentnode
        previousnode.nextNode = newnode
        return index
      else:
        previousnode = currentnode
        currentnode = currentnode.nextNode
        index += 1
    
    if currentnode == None:
      previousnode.nextNode = newnode
      return index



def dequeue_priority(Q):
  if Q.head == None:
    return None
  else:
    value = Q.head.value
    delete(Q,value)
    return value