class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> order = new Stack<>();
        int result = 0;



        for (int i =0; i < tokens.length;i++){
            String c = tokens[i];


            if (!c.equals("+") && !c.equals("-") && !c.equals("*") && !c.equals("/")) {
                order.push(Integer.parseInt(c));
            } else {
                int first = order.pop();
                int second = order.pop();

                if (c.equals("+")){
                    result = first + second;
                    order.push(result);
                } else  if (c.equals("-")){
                    result = second - first;
                    order.push(result);
                } else  if (c.equals("*")){
                    result = first * second;
                    order.push(result);
                }  if (c.equals("/")){
                    result = second/first;
                    order.push(result);
                }
            }
        }




        return order.pop();
    }
}
