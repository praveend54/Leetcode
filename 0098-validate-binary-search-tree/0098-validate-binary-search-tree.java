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
    public static boolean BST(TreeNode root,long mi,long ma){
            if(root==null) return true;
            if(root.val<=mi || root.val>=ma) return false;
            return BST(root.left,mi,root.val)&&BST(root.right,root.val,ma);
        }
    public boolean isValidBST(TreeNode root) {
        return BST(root,Long.MIN_VALUE,Long.MAX_VALUE);
    }
}