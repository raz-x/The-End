class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

stack = Stack()

while True:
    print("push <value>")
    print("pop")
    print("quit")
    do = input("What would you like to do? ").split()

    operation = do[0].strip().lower()

    if operation == 'push':
        if len(do) != 2 or not do[1].isdigit():
            print("Please enter a value to push.")
            continue
        stack.push(int(do[1]))

    elif operation == 'pop':
        popped = stack.pop()
        if popped is None:
            print("Stack is empty.")
        else:
            print("Popped value:", popped)

    elif operation == 'quit':
        break

    else:
        print("Invalid operation.")
    print()