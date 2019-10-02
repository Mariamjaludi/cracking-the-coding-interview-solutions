class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def addNode(self, node):
        current = self.head
        if current is None:
            self.head = node
        else:
            while current.next is not None:
                current = current.next
            current.next = node

    def printList(self):
        array = []
        current = self.head
        while current is not None:
            array.append(current.data)
            current = current.next
        print(array)

    def removeDuplicates(self):
        hash = {}
        current = self.head
        prev = None
        while current is not None:
            if current.data in hash:
                prev.next = current.next
            else:
                hash[current.data] = 1
                prev = current
            current = current.next


n0 = Node(0)
nodeList = [
    Node(1),
    Node(2),
    Node(1),
    Node(2),
    Node(3),
    Node(4)
]


linkedL = LinkedList(n0)

for node in nodeList:
    linkedL.addNode(node)

linkedL.printList()
linkedL.removeDuplicates()
linkedL.printList()
