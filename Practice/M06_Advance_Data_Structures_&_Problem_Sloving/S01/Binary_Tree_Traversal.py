class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

root = Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

def Pre_Order(root):
    if root:
        print(root.data,end="--|")
        Pre_Order(root.left)
        Pre_Order(root.right)
Pre_Order(root)

