#NodeTree

class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

class Tree:
    def __init__(self, max):
        self.root = Node(1)
        self.max = max
 
    def insert(self, data):
        if self.root == None:
            self.root = Node(1)

    def _insert_value(self, node, data, dataRight, dataLeft):
        if node.data == data:
            node.left = dataLeft
            node.right = dataRight

        else:
            self._insert_value(node.left, data, dataRight, dataLeft)
            self._insert_value(node.right, data, dataRight, dataLeft)

    def node_print(self):
        print(self.root.data)
        print(self.root.left.data)
        print(self.root.right.data)
        

node_num = int(input())
tree = Tree(node_num)
for i in range(node_num):
    a, b, c = input('a, b, c').split()
    a, b, c = int(a), int(b), int(c)
    tree._insert_value(tree.root, 1, 2, 3)

tree.node_print()