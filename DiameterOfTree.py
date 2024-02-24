"""
Program to find Diameter of a binary Tree
i.e Number of Nodes in the Longest Path between any 2 nodes
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
        newNode.left=self.buildTree(nodes)
        newNode.right=self.buildTree(nodes)
        return newNode
    
    def heightOfTree(self,node):
        if node is None:
            return 0
        leftHeight = self.heightOfTree(node.left)
        rightHeight = self.heightOfTree(node.right)
        return max(leftHeight,rightHeight)+1
    
    def DiameterOfTree(self,node):
        """
        Method to find the diameter of the tree in O(n2) time complexity
        """
        if node is None:
            return 0
        leftdiameter = self.DiameterOfTree(node.left)
        rightdiameter = self.DiameterOfTree(node.right)
        nodediameter = self.heightOfTree(node.left)+self.heightOfTree(node.right)+1
        return max(leftdiameter,rightdiameter,nodediameter)
     
class TreeInfo:
    def __init__(self,height,diameter) -> None:
        self.height = height
        self.diameter = diameter
    @staticmethod
    def diameter2(node):
        """
        Method to calculate Diameter of a Tree in O(n)
        """
        if node is None:
            return TreeInfo(0,0)
        leftTree = TreeInfo.diameter2(node.left)
        rightTree = TreeInfo.diameter2(node.right)
        height = max(leftTree.height,rightTree.height)+1
        diameter1 = leftTree.diameter
        diameter2 = rightTree.diameter
        diameter3 = leftTree.height+rightTree.height+1
        diameter = max(diameter1,diameter2,diameter3) 
        treeinfo = TreeInfo(height,diameter)
        return treeinfo



if __name__ == "__main__":
    res=lambda x,y=5:x+y
    res = res(3)
    print(res)
    nodes = [1,2,4,-1,-1,5,-1,-1,3,6,-1,-1,7,8,9,10,-1,-1,-1,-1,-1]
    tree = BinaryTree()
    root=tree.buildTree(nodes)
    print("Diameter of binary tree:",tree.DiameterOfTree(root))
    print("Optimized code:",TreeInfo.diameter2(root).diameter)
