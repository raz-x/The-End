class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.val, end=' ')
        printinorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=' ')

def printPreorder(root):
    if root:
        print(root.val, end=' ')
        printPreorder(root.left)
        printPreorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printinorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)