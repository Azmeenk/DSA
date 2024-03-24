# define a class stack to implement using arrays
class Stack:
    # declaration of size, top_index and the array
    def __init__(self):
        self.MAX = 1000
        self.top = 0
        self.stack = list()

    # func to return whether stack is empty or not
    def is_empty(self):
        return self.top == 0

    # func checks if the stack is full or not then appends the data
    def push(self, data):
        if self.top >= self.MAX:
            print("Stack Overflow")
            return False
        self.stack.append(data)
        self.top += 1
        return True

    # func check pop is empty or not then pops the top element
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        val = self.stack.pop()
        self.top -= 1
        return val

    # func checks if the stack is empty or not then return the top element
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.stack[self.top-1]


# Driver code
if __name__ == "__main__":
    s = Stack()
    print(s.push(10))
    print(s.push(20))
    print(s.push(30))
    print(s.pop())
    print(s.peek())
