# Linked Lists implementation in python

+ Here we created a class called Node that will simply have data(its value) and a pointer to the next node
```python
class Node: 
    def __init__(self, data): #Class constructor
        self.data = data
        self.next = None
```

+ Next, we create another class that will represent the Linked Lists data structure. A linked list has just a head as its first node and the head points to subsequent nodes
```python
from Node import Node #importing the node class which was in another file


class Nodes_List:
    def __init__(self): #constructor initialising the head to None
        self.head = None
```

+ Defining a function to insert a node which takes in a data argument which is  the data to be inserted
+ It initially checks if the head of the least is empty then the head is assigned to the newly created node with the data
```python
    def insertNode(self,data):

        node = Node(data) #creating a Node instance with the data to be inserted as the parameter
        if self.head is None:
            self.head = node
```
+ If the list is not empty, we create a counter variable that will be used in traversing the list and it is initialised to the head of the list
+ As long as the next value of last is not none, then we assign last new value to be equal to last.next 
````python
       else:
            last = self.head
            while last.next != None:
                last = last.next

            last.next = node #represents insertion where the loop's condition is broken(i.e. the last.next is None) then last.next now points to the new node

        return Nodes_List # we are returning the instance of Nodes_Lists
````

+ Defining a function to print the list
+ If the list is empty, ie the head is None, then we just print that
```python
 def printList(self):
        if self.head == None:
            print("List is empty")
            return
```
+ If not empty, we create a "counter" variable that will be used to traverse through the list and print the current value of current.data
+ The loop condition is as long as the counter(current) is not none, which will eventually break out when the final node is reached. Each iteration of current(node) is printed
```python
        else:
            current = self.head
            print("Linked List: ",end="")
            while current != None:
                print(str(current.data)+", ",end="")
                current = current.next
```

+ Defining a function for deleting a node
+ A counter variable current is initialised to the head of the list and if its data is equal to the target, then the value of the head of the list is set to the next node that current was pointing to
```python
 def deleteNode(self, target):
        current = self.head

        if current != None and current.data == target:
            self.head = current.next
            return
```
+ Here we initialise a variable prev that is equal to None that will later be used to equal to what current.next was pointing to when current is found to contain the data being targeted
+ The loop is incremented each time current exists(not None) and its data is not in the target
+ When the target is eventually found, then the loop breaks out and its prev.next now pointing to what current.next was pointing to
+ The  prev.next now is pointing to current.next, effectively "jumping" current node leading to deletion
```python
  prev = None
        while current and current.data != target:
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next
```

+ Sample function calls in main method
```python
def main():
    Lists = Nodes_List()

    Lists.insertNode(5)
    Lists.insertNode(6)
    Lists.insertNode(7)
    Lists.insertNode(8)

    Lists.printList() #example call for printing the list

    Lists.deleteNode(5)#sample deletion
    print()
    print("After deleting 5:")
    Lists.printList()

main()
```