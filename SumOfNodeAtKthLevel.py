"""
Program to find Sum of Nodes in a binary Tree
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
    
    def KthlevelOrder(self,node,k):
        if node is None:
            return 
        queue=[]
        s=0
        lvl=1
        queue.append(node)
        queue.append(None)
        while len(queue) and k>=1:
            currentNode=queue.pop(0)
            if  currentNode is not None:
                if currentNode.left is not None:
                        queue.append(currentNode.left)
                if currentNode.right is not None:
                        queue.append(currentNode.right)
                if k==1:
                    s+=currentNode.data
                
            else:
                print()
                if len(queue)!=0:
                    queue.append(None)
                    k-=1
                else:
                    break
        return s

    
    def sumOfNodes(self,node):
        if node is None:
            return 0
        leftSum = self.sumOfNodes(node.left)
        rightSum = self.sumOfNodes(node.right)
        return leftSum+rightSum+node.data
     

if __name__ == "__main__":
    nodes = [1,2,4,-1,-1,5,-1,-1,3,6,-1,-1,7,-1,-1]
    tree = BinaryTree()
    root=tree.buildTree(nodes)
    print("Sum of Node at 1st level:",tree.KthlevelOrder(root,1))
