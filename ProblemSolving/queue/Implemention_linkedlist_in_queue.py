class Node:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.item_count -= 1

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.rear.item

    def size(self):
        return self.item_count

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1.size())
print(q1.get_front())
print(q1.get_rear())
q1.dequeue()
print(q1.size())
print(q1.get_front())
print(q1.get_rear())


