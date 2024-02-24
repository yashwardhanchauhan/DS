"""
Program to find Height in a binary Tree
"""
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    index=-1

    def buildTree(self,nodes):
        BinaryTree.index+=1
        if nodes[BinaryTree.index]==-1:
            return None
        newNode = Node(nodes[BinaryTree.index])
        print(newNode.data)
        newNode.left=self.buildTree(nodes)
        newNode.right=self.buildTree(nodes)
        return newNode
    
    def heightOfTree(self,node):
        if node is None:
            return 0
        leftHeight = self.heightOfTree(node.left)
        rightHeight = self.heightOfTree(node.right)
        return max(leftHeight,rightHeight)+1
     

if __name__ == "__main__":
    nodes = [1,2,4,-1,-1,5,-1,-1,3,6,-1,-1,7,8,9,10,-1,-1,-1,-1,-1]
    tree = BinaryTree()
    root=tree.buildTree(nodes)
    print(root.left.data)
    print("Height of binary tree:",tree.heightOfTree(root))
