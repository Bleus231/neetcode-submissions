class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> stack = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            // Push closing bracket onto the stack for each opening bracket
            if (c == '[') {
                stack.add(']');
            } else if (c == '(') {
                stack.add(')');
            } else if (c == '{') {
                stack.add('}');
            } else {
                // If it's a closing bracket, check if it matches the last element
                if (stack.isEmpty() || stack.get(stack.size() - 1) != c) {
                    return false;
                }
                // Remove the last matched bracket
                stack.remove(stack.size() - 1);
            }
        }

        // If the stack is empty, all brackets were matched
        return stack.isEmpty();
    }
}
