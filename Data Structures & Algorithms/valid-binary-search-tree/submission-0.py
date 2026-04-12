# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def check(node, lowerB = -1001, upperB = 1001):
            if not node:
                return True

            if not (node.val > lowerB and node.val < upperB):
                return False

            return check(node.left,lowerB,node.val) and check(node.right,node.val,upperB)


        return check(root)


        