#implementing trees
class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#inorder traversal
def printInorderTraversal(root):
    if root == None:
        return
    printInorderTraversal(root.left)
    print(root.data, end=" ")
    printInorderTraversal(root.right)
#postorder traversal    
def printPostorderTraversal(root):
    if root == None:
        return
    printPostorderTraversal(root.left)
    printPostorderTraversal(root.right)
    print(root.data, end=" ")
#preorder traversal    
def printPreorderTraversal(root):
    if root == None:
        return
    print(root.data, end=" ")
    printPostorderTraversal(root.left)
    printPostorderTraversal(root.right)
    
#level order traversal 
def levelOrderTraversal(root):
    if root == None:
        return 
    result = []
    Q = [root]
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            # step - 1
            currNode = Q.pop(0)
            # step - 2
            subResult.append(currNode.data)
            # step - 3
            if currNode.left != None:
                Q.append(currNode.left)
            # step - 4
            if currNode.right != None:
                Q.append(currNode.right)
        result.append(subResult)
    print(result)
 
               
#creating tree nodes        
n1=Tree(-105)
n2=Tree(1)
n3=Tree(28)
n4=Tree(27)
n5=Tree(82)
n6=Tree(-15)
n7=Tree(-18)
n8=Tree(22)
n1.left=n2
n2.right=n3
n3.left=n4
n1.right=n5
n5.left=n6
n6.left=n7
n6.right=n8 
'''printInorderTraversal(n1)
print()
printPostorderTraversal(n1)
print()
printPreorderTraversal(n1)      
print()    
'''    
levelOrderTraversal(n1) 
