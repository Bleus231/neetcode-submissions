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
   
            public static List<Integer> listsPerLevel (TreeNode root, List<List<Integer>> lists, int currentLevel){
            List<Integer> list;

            if (root == null){
                return null;
            }

    
    

            if (lists.size() == currentLevel){
                list = new ArrayList<>();
                list.add(root.val);
                 lists.add(list);
            } else {
               list = lists.get(currentLevel);
               list.add(root.val);
            }

            listsPerLevel(root.left,lists,currentLevel + 1);
            listsPerLevel(root.right,lists,currentLevel + 1);




            return list;
    
    
    
    
        }


    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> lists = new ArrayList<>();
        int currentLevel = 0;


        if (root == null){
            return lists;
        }



        listsPerLevel(root,lists,currentLevel);
        



        return lists;
    }



    
}
