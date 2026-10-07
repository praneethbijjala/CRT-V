'''
Double Linked List :
The data can be store in the nodes
Nodes - -> 3 parts
1. Data
2.prev
3. next

Algorithm 
1. Create node
2.insert data
3. connection
4.traverse
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
node1 =Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

def traverse():
    curr = node1
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")
traverse()

