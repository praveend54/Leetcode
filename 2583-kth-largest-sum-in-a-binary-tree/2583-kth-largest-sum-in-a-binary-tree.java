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
    public long kthLargestLevelSum(TreeNode root, int k) {
        List<Long> l=new ArrayList<>();
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            int n=q.size();
            long s=0;
            for(int i=0;i<n;i++){
                TreeNode d=q.poll();
                s+=d.val;
                if(d.left!=null) q.add(d.left);
                if(d.right!=null) q.add(d.right);
            }
            l.add(s);
        }
        Collections.sort(l);
        if(k>l.size()) return -1;
        return l.get(l.size()-k);
    }
}