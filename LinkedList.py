# Dean Blank
# Section: CS-172-A; Lab 061

import sys

# Node Class
class Node:

  def __init__(self,v = None):
    self.value = v
    self.next = None
    self.previous = None

  # string Method
  def __str__(self):
    return '['+str(self.value)+']'

  # gets next Node
  def getNext(self):
    return self.next

  # sets node to next node
  def setNext(self,n):
    self.next = n

  # gets previous node
  def getPrev(self):
    return self.previous

  # sets node to previous
  def setPrev(self,p):
    self.previous = p

  # gets value of node 
  def getValue(self):
    return self.value

  # sets value of node
  def setValue(self,v):
    self.value = v


# linked list class
class DoubleLinkedList:

  # constructor
  def __init__(self, n = None):
    self.head = n

  # string method
  def __str__(self):
    current = self.head 
    mystr = ''  # empty string
    while current != None:  # loop through all nodes until current node equals None
      mystr+= str(current)+'->' # add current node to string
      current = current.getNext() # iterates to next node
    mystr = mystr[:-2] # returns everything as string except last arrow (removes last arrow)
    return mystr

  # returns reference to last element in list
  def last(self):
    current = self.head # set current to head
    if current== None:  # current is none exit method
      return
    else:
      while current.getNext()!=None:  # loop through nodes and return last node until getNext = None
        current = current.getNext()
      return current

  # returns reference to value in given parameter
  def find(self,v):
    current = self.head # loop through list until you get value in parameter an break loop
    while current!=None:
      if current.getValue()==v:
        break
      else:
        current = current.getNext()
    return current # returns either value or None

  # appends node to end of list
  def append(self,v):
    new = Node(v) # creates a new node
    if self.head == None: # if head is none set head to new node
      self.head = new
      return
    current = self.last() # current node is equal to last node in list
    current.setNext(new) # set current node to new node
    new.setPrev(current) # set new node to the current node

  # adds node with specific value before first node in list
  def prepend(self,v):
     new = Node(v) # create new node
     self.head.setPrev(new) # set previous of head to new node
     new.setNext(self.head) # set new node pointer to the head
     self.head = new # make the new node the head

  # Removes node in list with value in parameter
  def delete(self, x):
    current = self.find(x) # find reference of node that needs to be deleted 
    if current==None: # if value not found in list then print not valid input
      return
    if current.getPrev()==None: # if previous of current node is None, set the current as the head
      self.head = current.getNext()
      self.head.setPrev(None)
    elif current.getNext()!= None: # if current's next is not None then set its next to its previous
      current.getNext().setPrev(current.getPrev())
      current.getPrev().setNext(current.getNext()) # set the currents previous to its next
    else:
      current.getPrev().setNext(current.getNext()) # otherwise set the currents previous to its next
      
      
  #insert Node with value y after node with value x
  def insertAfter(self, x, y):
    new = Node(y) # create new node
    current = self.find(x)  # find reference of current node with value x
    if current==None: # value not found if current equals None
      print('value not found in linked list')
      return

    else: # if current != None
      if current.getNext()!=None:
        current.getNext().setPrev(new) # set currents next previous to new
        new.setNext(current.getNext()) # set news next to currents next
        current.setNext(new) # set currents next to new
        new.setPrev(current) # set news previous to current
      else:
        current.setNext(new) # set currents next to new
        new.setPrev(current) # set news previous to current

  def clear(self):      # delete the last value and loop to clear all nodes
    while self.head !=None:
      current = self.head
      self.head= current.getNext()
      self.delete(current.getValue())

      
# intro 
def main():
  print('Welcome to the Linked List Tester')
  print('Commands:')
  print('clear - Removes every value from the list')
  print('exit - Quit the program')
  print('prepend num - Add the number given to the beginning of list')
  print('append num - add the number given to the end of list')
  print('delete num - Deletes the first appearance of given number')
  print('insertAfter num1 num2 - Places num2 after the first appearance of num 1')


  command = input('command: ') # ask user for command
  command = command.split() # split command string

  
  LL = DoubleLinkedList() # creating instance of double linked list
  while command[0]!='exit': # run loop while command isnt 'exit'
    if command[0] == 'clear':
      LL.clear() # run method
      print(LL) # print list
      command = input('command: ') # ask for input
      command = command.split() # split string so I can access numbers or text from string
    elif command[0] == 'prepend':
      try:
        LL.prepend(command[1])
        print(LL)
        command = input('command: ')
        command = command.split()
      except:
        command = input('command: ')
        command = command.split()
    elif command[0] == 'append':
      try:
        LL.append(command[1])
        print(LL)
        command = input('command: ')
        command = command.split()
      except:
        command = input('command: ')      
        command = command.split()
    elif command[0] == 'delete':
      try:
        LL.delete(command[1])
        print(LL)
        command = input('command: ')
        command = command.split()
      except:
        command = input('command: ')
        command = command.split()
    elif command[0] == 'insertAfter':
      try:
        LL.insertAfter(command[1],command[2])
        print(LL)
        command = input('command: ')
        command = command.split()
      except:
        command = input('command: ')
        command = command.split()
    else:
      command = input('command: ')
      command = command.split()
    

 

main()
sys.exit() # exit program




