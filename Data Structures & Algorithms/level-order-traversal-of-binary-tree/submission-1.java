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
   
                  //Helper method to add all nodes on each level

        public static List<Integer> listsPerLevel (TreeNode root, List<List<Integer>> lists, int currentLevel){
            List<Integer> list;
            
            //If current root is null return null
            if (root == null){
                return null;
            }
            
            //If condition below is met it means no list has been created yet
            if (lists.size() == currentLevel){
                list = new ArrayList<>();
                list.add(root.val);
                 lists.add(list);
                 //Otherwise current node is added to the existing list
            } else {
               list = lists.get(currentLevel);
               list.add(root.val);
            }
            
            
            //Recurse through children 
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
