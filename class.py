class Stack:
    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size

    def is_full(self):
        return len(self.stack) >= self.max_size

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
            print("Pushed:", item)
            self.display_stack()
        else:
            print("Stack is full!")

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack.pop()
            print("Popped:", popped_item)
            self.display_stack()
        else:
            print("Stack is empty!")

    def view_top(self):
        if not self.is_empty():
            print("Top element:", self.stack[-1])
        else:
            print("Stack is empty!")

    def display_stack(self):
        print("Stack:", self.stack)


# Test the stack
def test_stack_operations():
    stack = Stack(max_size=10)

    # Pushing elements
    for letter in "1,2,3,4,5,6,7,8,9,10":
        stack.push(letter)

    # Trying to push when stack is full
    stack.push("K")

    # Popping elements twice
    stack.pop()
    stack.pop()

    # Viewing top element
    stack.view_top()


if __name__ == "__main__":
    test_stack_operations()
