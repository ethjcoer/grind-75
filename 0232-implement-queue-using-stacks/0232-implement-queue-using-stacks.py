class MyQueue:
    # This class implements a queue using two stacks (stack1 and stack2).
    # The queue operations are push, pop, peek, and empty.

    def __init__(self):
        # Initialize two empty stacks, stack1 and stack2.
        # stack1 will be used for enqueuing elements.
        # stack2 will be used for dequeuing elements.
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Push an element to the queue.
        # The element x is always pushed onto stack1.
        self.stack1.append(x)

    def pop(self) -> int:
        # Pop an element from the front of the queue.
        # The pop operation requires stack2 to have elements, so we call peek()
        # to ensure stack2 is populated before popping from it.
        self.peek()
        # Remove and return the element from the top of stack2, which is the front
        # of the queue.
        return self.stack2.pop()

    def peek(self) -> int:
        # Peek at the front element of the queue without removing it.
        # If stack2 is empty, transfer all elements from stack1 to stack2.
        # This reverses the order of elements so that the first element in stack1
        # becomes the top element in stack2.
        if not self.stack2:
            while self.stack1:
                # Move each element from stack1 to stack2. This reverses their order.
                self.stack2.append(self.stack1.pop())
        # Return the top element from stack2, which corresponds to the front of the
        # queue.
        return self.stack2[-1]

    def empty(self) -> bool:
        # Check if the queue is empty.
        # The queue is empty if both stack1 and stack2 are empty.
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
