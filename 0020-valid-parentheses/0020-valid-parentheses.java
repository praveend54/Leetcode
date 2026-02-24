class Solution {
    public boolean isValid(String s) {
        Stack<Character> st=new Stack<>();
        for(char ch:s.toCharArray()){
            if(st.empty()) st.push(ch);
            else if(ch=='(' || ch=='[' || ch=='{') st.push(ch);
            else{
                char c=st.peek();
                if(ch==']' && c=='[') st.pop();
                else if(ch==')' && c=='(') st.pop();
                else if(ch=='}' && c=='{') st.pop();
                else return false;
            }
        }
        if(st.empty()) return true;
        return false;
        
    }
}