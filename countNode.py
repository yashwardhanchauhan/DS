"""
Program for counting Number of Nodes in a binary Tree
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
    
    def countNodes(self,node):
        if node is None:
            return 0
        leftNodes = self.countNodes(node.left)
        rightNode = self.countNodes(node.right)
        return leftNodes+rightNode+1
    

if __name__ == "__main__":
    nodes = [1,2,4,-1,-1,5,-1,-1,3,6,-1,-1,7,-1,-1]
    tree = BinaryTree()
    root=tree.buildTree(nodes)
    print(root.left.data)
    print("Count of Node is:",tree.countNodes(root))
