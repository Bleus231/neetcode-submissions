class Solution {
    public boolean isValid(String s) {
            Stack<Character> order = new Stack<>();

        if (s.length() < 2){
            return false;
        }

        for (int i=0; i < s.length(); i++){
            char c = s.charAt(i);


            if (c == '{'){
                order.add('}');
            } else if (c == '['){
                order.add(']');
            } else if (c == '('){
                order.add(')');
            } else {
                if (order.isEmpty() || order.peek() != c){
                    return false;
                } else {
                    order.pop();
                }
            } 

        }

        return order.isEmpty();
    }
}
