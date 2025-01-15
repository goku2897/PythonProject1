class Node:
    def __init__(self, data,next):
        self.data = data
        self.next = next

#Creating node
node1 = Node(10,None)
node2 = Node (20,None)
node3 = Node (30,None)
node4 = Node (40,None)

#Connecting node to form a linked list
node1.next = node2
node2.next = node3
node3.next = node4

head = node1
current = head
while current is not None:
    print(current.data,end= " -> ")
    current = current.next
print("None")