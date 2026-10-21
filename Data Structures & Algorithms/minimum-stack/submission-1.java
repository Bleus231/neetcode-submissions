public class MinStack {

        public Stack<Integer> newStack;

        public MinStack (){
            newStack = new Stack<>();
        }

        public void push (int val){
            newStack.push(val);
        }

        public void pop(){
            newStack.pop();
        }

        public int top(){
            return newStack.peek();
        }

        public int getMin(){
            int min = newStack.get(0);

            for (int i =0; i < newStack.size(); i++){
                int current = newStack.get(i);


                if (current < min){
                    min = current;
                }
            }

            return min;
        }





}
