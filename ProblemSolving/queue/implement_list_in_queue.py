class Queue:
    def __init__(self):
        self.item = []
        #self.front = None
        #self.rear = None

    def isEmpty(self):
        return len(self.item) == 0

    #insertion
    def enqueue(self, date):
        self.item.append(date)
    #deletion
    def dequeue(self):
        if not self.isEmpty():
            return self.item.pop(0)
        else:
            raise IndexError("Queue is empty")

    def get_front(self):
        if not self.isEmpty():
            return self.item[0]
        else:
            raise IndexError("Queue is empty")

    def get_rear(self):
        if not self.isEmpty():
            return self.item[-1]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.item)

q1 = Queue()
try:
    print(q1.get_front())
except Exception as e:
    print(e)



q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print(q1.get_front())
print(q1.get_rear())

try:
    print(q1.dequeue())
    print(q1.size())
except Exception as e:
    print(e)
