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
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        Queue<TreeNode> q=new LinkedList<>();
        List<List<Integer>> a=new ArrayList<>();
        if(root==null) return a;
        q.add(root);
        while(!q.isEmpty()){
            int n=q.size();
            ArrayList<Integer> l=new ArrayList<>();
            for(int i=0;i<n;i++){
                TreeNode d=q.poll();
                l.add(d.val);
                if(d.left!=null) q.add(d.left);
                if(d.right!=null) q.add(d.right);
            }
            a.add(l);
        }
        return a;
    }
}