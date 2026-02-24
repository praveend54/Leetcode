class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n=nums.length;
        int res[]=new int[n];
        Stack<Integer> st=new Stack<>();
        for(int i=2*n-1;i>=0;i--){
            int c=nums[i%n];
            while(!st.empty() && st.peek()<=c) st.pop();
            if(i<n){
                res[i]=st.empty()?-1:st.peek();
            }
            st.push(c);
        }
        return res;
    }
}