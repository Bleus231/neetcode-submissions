class Solution {
    public int lengthOfLongestSubstring(String s) {
          HashSet<Character> hashSet = new HashSet<>();
        int maxSubstring =0;
        int start =0;
        int end = 0;


       while (end < s.length()){
           char c = s.charAt(end);
           if (!hashSet.contains(c)){
                hashSet.add(c);
                end++;
                if (end - start > maxSubstring){
                    maxSubstring = end - start;
                }
           } else {
               hashSet.remove(s.charAt(start));
               start++;
           }
       }
        return maxSubstring;
    }
}
