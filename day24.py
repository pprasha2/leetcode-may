'''
Construct Binary Search Tree from Preorder Traversal
Solution
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preBst(self,preorder,l,r,index):
        if l == r:
            return TreeNode(preorder[index])
        if l > r:
            return None
        print(preorder[index])
        node = TreeNode(preorder[index])
        pos = self.inorder.index(preorder[index])
        node.left = self.preBst(preorder,l,pos-1,index+1)
        node.right = self.preBst(preorder,pos+1,r,index+pos-l+1)
        return node
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.inorder = sorted(preorder)
        self.index = 0
        return self.preBst(preorder,0,len(preorder)-1,0)
