"""
Developing Tree using PreOrder List
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

    

if __name__ == "__main__":
    nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    root=tree.buildTree(nodes)
    print(root.left.data)
