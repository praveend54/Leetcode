class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> st=new Stack<>();
        int res[]=new int[temperatures.length];
        for(int j=0;j<temperatures.length;j++) res[j]=0;
        int i=temperatures.length-1;
        while(i>=0){
            if(st.empty()) st.push(i--);
            else if(temperatures[i]>=temperatures[st.peek()]) st.pop();
            else{
                res[i]=st.peek()-i;
                st.push(i--);
            }
        }
        return res;
    }
}