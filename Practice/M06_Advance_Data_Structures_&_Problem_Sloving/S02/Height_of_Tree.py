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


def Height(root):
    if root is None:
        return 0
    left_height =Height(root.left)
    right_height=Height(root.right)
    return 1+max(left_height,right_height)

def is_Balanced(root):
    if root is None:
        return True
    l= Height(root.left)
    r=Height(root.right)
    if abs (l-r)<=1:
        return True
    return False
print(is_Balanced(root))


print(Height(root))