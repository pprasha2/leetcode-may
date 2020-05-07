'''
Cousins in Binary Tree
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3

Output: false
Note:
The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque()
        q.append(root)
        q.append(0)
        level = 0
        found = 0
        L = set()
        P = set()
        while len(q) > 1:
            current = q.popleft()
            if current == 0:
                level += 1
                q.append(current)
                continue
            if current.val == x or current.val == y:
                found += 1
                L.add(level)
                if found == 2:
                    return len(L) == 1 and len(P) == 2
            if current.left:
                if current.left.val == x or current.left.val == y:
                    P.add(current)
                q.append(current.left)
            if current.right:
                if current.right.val == x or current.right.val == y:
                    P.add(current)
                q.append(current.right)
