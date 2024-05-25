# Kth smallest elment
class Solution:
    def collectInOrderTraversal(self,root,arr):
        if root==None:
            return
        self.collectInOrderTraversal(root.left,arr)
        arr.append(root.val)
        self.collectInOrderTraversal(root.right,arr)
    def kthSmallest(self, root: optional[TreeNode], k: int) -> int:
        arr=[]
        self.collectInOrderTraversal(root,arr)
        n=len(arr)
        return arr[k-1]