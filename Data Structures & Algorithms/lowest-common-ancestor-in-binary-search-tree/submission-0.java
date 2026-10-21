/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {


    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        //checking for null cases
        if (root == null || p == null || q == null) {
            return null;
        }

        //Checks if LCA is in left subtree
        if (Math.max(p.val, q.val) < root.val) {
            return lowestCommonAncestor(root.left, p, q);

        //Check to see if LCA is in right subtree    
        } else if (Math.min(p.val, q.val) > root.val) {
            return lowestCommonAncestor(root.right, p, q);

        //Will be here if not found in either left or right    
        } else {
            return root;
        }
    }
}
