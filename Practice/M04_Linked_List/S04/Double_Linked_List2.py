class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Double_LL:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head ==None:
            return new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    def delete_begin(self):
        if self.head is None:
            return
        self.head = self.head.next
        del del_node

    def delete_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        del_node = temp.next
        temp.next.prev = None
        temp.next = None
        del del_node
        
    

    def count_nodes(self):
        if self.head is None:
            return 0
        if self.head.next is None:
            return 1
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    
    def traverse(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, "<->", end=" ")
            temp = temp.next
        print("None")
dll = Double_LL()
dll.insert_begin(10)
dll.insert_begin(20)    
dll.insert_begin(30)
dll.traverse()