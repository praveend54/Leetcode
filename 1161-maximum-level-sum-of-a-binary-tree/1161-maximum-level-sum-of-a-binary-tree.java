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
    public int maxLevelSum(TreeNode root) {
        int m=Integer.MIN_VALUE,index=1,j=1;
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            int n=q.size();
            int s=0;
            for(int i=0;i<n;i++){
                TreeNode d=q.poll();
                s+=d.val;
                if(d.left!=null){
                    q.add(d.left);
                }
                if(d.right!=null){
                    q.add(d.right);
                }
            }
            if(s>m){
                index=j;
                m=s;
            }
            j++;
        }
        return index;
    }
}