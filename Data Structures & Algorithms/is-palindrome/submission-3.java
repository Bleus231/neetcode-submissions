class Solution {
    public boolean isPalindrome(String s) {
          StringBuilder original = new StringBuilder();

        for (int i=0; i < s.length(); i++){
            char c = s.charAt(i);

            if (Character.isAlphabetic(c) || Character.isDigit(c)){
                c = Character.toLowerCase(c);
                original.append(c);
            }

        }

        StringBuilder reverse = new StringBuilder(original);
        reverse.reverse();
        System.out.print("the Original is " + original);
        System.out.print("The reversed is " + reverse);

        if (original.toString().equals(reverse.toString())){
            return true;
        }



        return false;
    }
}
