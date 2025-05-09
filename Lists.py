class Nodes_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
