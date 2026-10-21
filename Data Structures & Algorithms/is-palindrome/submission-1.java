class Solution {
    public boolean isPalindrome(String s) {
         StringBuilder palindrome = new StringBuilder();


        if (s.isEmpty()){
            return true;
        }

        for (int i = 0; i < s.length(); i++){

            char c =  Character.toLowerCase(s.charAt(i));
            if (Character.isLetter(c) || Character.isDigit(c)){
                palindrome.append(c);

            }
        }




        StringBuilder reversed = new StringBuilder(palindrome);
        reversed.reverse();
       


        return reversed.toString().contentEquals(palindrome);
    }
}
