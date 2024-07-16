class Stack:
    def __init__(self):
        self.stack = []
        self.max_size = 10

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            print("Pushed:", item)
            self.display_stack()
        else:
            print("Stack is full!")

    def pop(self):
        if self.stack:
            popped_item = self.stack.pop()
            print("Popped:", popped_item)
            self.display_stack()
        else:
            print("Stack is empty!")

    def view_top(self):
        if self.stack:
            print("Top element:", self.stack[-1])
        else:
            print("Stack is empty!")

    def display_stack(self):
        print("Stack:", self.stack)


# Test the stack
stack = Stack()

# Pushing elements
stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")
stack.push("E")
stack.push("F")
stack.push("G")
stack.push("H")
stack.push("I")
stack.push("J")
stack.push("K")  # Trying to push when stack is full

# Popping elements twice
#popping an element twice from the array
stack.pop()
stack.pop()

# Viewing top element
stack.view_top()

def findmax():
    list = []
    amount = int(input("amount of numbers in the list"))
    for i in range(amount):
        items_in_new_list = int(input("enter values"))
        list.append(items_in_new_list)
    print(list)
    a = max(list)
    print(a)
findmax()


c:\Users\Hp\pycharmProjects\pythonProject
