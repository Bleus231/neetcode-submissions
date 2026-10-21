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
    //This helper method will take in root and list to
    //recursivelly go through every node and add value to list
    //This method uses L -> N -> R traversal order.
    public static void nodeValue (TreeNode root, ArrayList<Integer> list){
        if (root == null){
            return;
        }
        nodeValue(root.left,list);
        list.add(root.val);
        nodeValue(root.right,list);

    }




    public int kthSmallest(TreeNode root, int k) {
        if (root == null){
            return 0;
        }

        ArrayList<Integer> list = new ArrayList<>();
        nodeValue(root,list);


        Collections.sort(list);


        return list.get(k - 1);
    }
}
