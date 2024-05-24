class Box:
    def __init__(self,data):
         self.data=data
         self.left=None
         self.right=None
#In order traversal
def printInOrderTraversal(root):
    if root==None:
        return
    printInOrderTraversal(root.left)
    print(root.data,end=" ")
    printInOrderTraversal(root.right)
#Pre order traversal
def printPreOrderTraversal(root):
    if root==None:
        return
    print(root.data)
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right,end=" ")
#post order traversal
def printPostOrderTraversal(root):
    if root==None:
        return
    printPostOrderTraversal(root.left)
    printPostOrderTraversal(root.right)
    print(root.data,end=" ")
#level order traversal ----> https://pastebin.com/mXprcNB0
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
 
#object creation is happening here # 20 100 -40 50 90 10 30 
obj1=Box(10)
obj2=Box(20)
obj3=Box(30)
obj4=Box(40)
obj5=Box(50)
obj6=Box(60)
obj7=Box(70)
obj8=Box(90)
obj9=Box(100)
obj10=Box(-40)
#establishing links among those nodes
obj1.left=obj2
obj1.right=obj3
obj2.right=obj4
obj2.right=obj5
obj4.right=obj6
obj6.left=obj7
obj5.right=obj8
obj5.left=obj9
obj9.right=obj10