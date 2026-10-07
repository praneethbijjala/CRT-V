'''
#stack implementation using python list

from pyclbr import Class


class stack:
    def __init__(self):
        self.s =[]

    def push(self,val):
        self.s.append(val)

    def is_empty(self):
        return len(self.s) == 0

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.s.pop()
    
    def size(self):
        return len(self.s)

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.s[-1]
st=stack()
print(st.is_empty())
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())
print(st.pop())
print(st.size())
print(st.peek())

#stack implementation using linked list

class Node:
    pass

    def __init__(self):
        self.top = None
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node
    def is_empty(self):
        return self.top is None
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        del_val = self.top.data
        self.top = self.top.next
        return del_val
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.top.data
    def size(self):
        temp = self.top
        count=0
        while temp:
            count +=1
            temp = temp.next
        return count
'''
#Implementation of a Queue Using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,val):
        new_node = Node(val)
        if self.rear is None:
            self.rear = self.front=new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        del_val = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return del_val
    def front(self):
       if self.front is None:
            return "Queue is empty"
       return self.front.data
    def dispaly(self):
        if self.front is None:
            print("Queue is empty")
            return
        temp = self.front
        while temp:
            print(temp.data,end="  ")
            temp = temp.next
        print()
queue = Queue_LL()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.dispaly()
queue.dequeue()
queue.dispaly()
print(queue.peek())
         
