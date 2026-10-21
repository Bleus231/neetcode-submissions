# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def height(node):

            if not node:
                return -1

            left_diameter = height(node.left)
            right_diameter = height(node.right)

            self.diameter = max(self.diameter, left_diameter + right_diameter + 2)

            return max(left_diameter, right_diameter) + 1

        height(root)
        return self.diameter




        