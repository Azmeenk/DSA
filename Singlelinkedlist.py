class LinkedList:
    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None

    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def traverse(self, callback):
        temp = self.head
        while temp:
            callback(temp.data)
            temp = temp.next

if __name__ == '__main__':
    list = LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    list.insert(4)
    list.insert(5)

    print("Printing the LinkedList:")
    list.printList()

    print("Traversing the LinkedList:")
    list.traverse(lambda data: print(data))
