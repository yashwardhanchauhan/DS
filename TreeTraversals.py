"""
Tree Traversal Approaches
"""
class Node:
    """
    A Node class to create Node for Tree
     ---------------
    |left|Data|right|
     ----------------
    """

    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    index=-1

    def buildTree(self,nodes:list):
        """
        Method to Build a Tree using list of nodes
        :param : nodes ->"List of nodes"
        """
        BinaryTree.index+=1
        if nodes[BinaryTree.index]==-1:
            return None
        newNode = Node(nodes[BinaryTree.index])
        newNode.left = self.buildTree(nodes)
        newNode.right = self.buildTree(nodes)
        return newNode
    
    def preOrder(self,node:Node):
        """
        Method to traverse tree in preOrder (Root,LeftSubtree,RightSubtree)
        :param : node ->"Node of a Tree" 
        """
        if node is None:
            return
        print(node.data,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)
    
    def postOrder(self,node:Node):
        """
        Method to traverse tree in postOrder (LeftSubtree,RightSubtree,Root)
        :param : node ->"Node of a Tree" 
        """
        if node is None:
            return "-1"
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data,end=" ")

    def inOrder(self,node:Node):
        """
        Method to traverse tree in inOrder (LeftSubtree,Root,RightSubtree)
        :param : node ->"Node of a Tree"         
        """
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data,end=" ")
        self.inOrder(node.right)
    
    def levelOrder(self,node):
        """
        Method to traverse tree in Level using Queue(First In, First Out)
        :param : node ->"Node of a Tree" 
        """
        if node is None:
            return
        queue:Node=[]
        queue.append(node)
        queue.append(None)
        while len(queue):
            currentNode=queue.pop(0)
            if currentNode is None:
                print()
                if len(queue)!=0:
                    queue.append(None)
                else:
                    break
            else:
                print(currentNode.data,end=" ")
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)

       


if __name__=="__main__":
    nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
    tree = BinaryTree()
    root = tree.buildTree(nodes)
    tree.preOrder(root)
    print()
    tree.inOrder(root)
    print()
    tree.postOrder(root)
    print("Level Order")
    tree.levelOrder(root)
    

    

