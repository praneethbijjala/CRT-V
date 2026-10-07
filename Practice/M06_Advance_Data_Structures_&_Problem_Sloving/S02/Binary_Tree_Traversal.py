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

def BFS(node):
    if node is None:
        return
    d = deque([node])
    while d:
        first_node = d.popleft()
        print(first_node.data,end=" ")
        if node.left:
            d.append(first_node.left)
        if first_node.right:
            d.append(first_node.right)

BFS(root)