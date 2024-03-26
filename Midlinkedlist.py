class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, d):
            self.data = d
            self.next = None

    def push(self, new_data):
        new_node = self.Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        tnode = self.head
        while tnode is not None:
            print(tnode.data, end=" -> ")
            tnode = tnode.next
        print("NULL")

    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while fast_ptr is not None and fast_ptr.next is not None:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next.next
            print("The middle element is:", slow_ptr.data)

if __name__ == "__main__":
    llist = LinkedList()
    for i in range(15, 0, -1):
        llist.push(i)
        llist.printList()
        llist.printMiddle()