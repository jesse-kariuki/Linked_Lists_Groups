from Node import Node


class Nodes_List:
    def __init__(self):
        self.head = None


    def insertNode(self,data):

        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next != None:
                last = last.next

            last.next = node

        return Nodes_List

    def printList(self):
        if self.head == None:
            print("List is empty")
            return

        else:
            current = self.head
            print("Linked List: ",end="")
            while current != None:
                print(str(current.data)+", ",end="")
                current = current.next

    def deleteNode(self, target):
        current = self.head

        if current != None and current.data == target:
            self.head = current.next
            return

        prev = None
        while current and current.data != target:
            prev = current
            current = current.next
        if current != None:
            prev.next = current.next





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

