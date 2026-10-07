size = 5
li = [None] * size
print(li)

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    def enqueue(self, value):
        # Check if queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return
        # First element
        if self.front == -1:
            self.front = 0
        # Move rear circularly
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        # Check if queue is empty
        if self.front == -1:
            print("Queue is Empty")
            return
        value = self.queue[self.front]
        self.queue[self.front] = None
        # Only one element was present
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return value

    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        return self.queue[self.front]

    def display(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()
print("Deleted:", cq.dequeue())
print("Deleted:", cq.dequeue())
cq.enqueue(60)
cq.enqueue(70)
cq.display()
print("Front:", cq.peek())

    