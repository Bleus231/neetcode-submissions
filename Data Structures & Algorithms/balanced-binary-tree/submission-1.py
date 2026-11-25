# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_height_if_unbalanced(node):
            
            #Check if empty
            if not node:
                return 0

            #dive left
            left_height = get_height_if_unbalanced(node.left)
            if left_height == -1:
                return -1
            
            right_height = get_height_if_unbalanced(node.right)
            if right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return get_height_if_unbalanced(root) != -1
        