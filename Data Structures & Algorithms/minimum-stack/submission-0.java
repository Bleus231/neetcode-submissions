class MinStack {
 Stack<Integer> stack = new Stack<>();
    public MinStack() {
         this.stack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
    }
    
    public void pop() {
         stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
          Stack<Integer> tmp = new Stack<>();
        int mini = stack.peek();

        while (!stack.isEmpty()) {
            mini = Math.min(mini, stack.peek());
            tmp.push(stack.pop());
        }
        
        while (!tmp.isEmpty()) {
            stack.push(tmp.pop());
        }
        
        return mini;
    }
}
