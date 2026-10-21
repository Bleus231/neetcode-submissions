class Solution {
    public boolean checkInclusion(String s1, String s2) {
         if (s1.length() > s2.length()) {
            return false; // s1 cannot be a permutation of any substring of s2
        }

        HashMap<Character, Integer> charCountS1 = new HashMap<>();
        HashMap<Character, Integer> windowCharCount = new HashMap<>();
        int windowSize = s1.length();

        int left = 0;
        int right = 0;

        for (int i = 0; i < s1.length(); i++) {
            char c = s1.charAt(i);
            charCountS1.put(c, charCountS1.getOrDefault(c, 0) + 1);
        }

        for (int i = 0; i < s2.length(); i++) {
            // Add the current character to the window
            char c = s2.charAt(i);
            windowCharCount.put(c, windowCharCount.getOrDefault(c, 0) + 1);

            // Remove the character left out of the window
            if (i >= windowSize) {
                char leftChar = s2.charAt(i - windowSize);
                if (windowCharCount.get(leftChar) == 1) {
                    windowCharCount.remove(leftChar);
                } else {
                    windowCharCount.put(leftChar, windowCharCount.get(leftChar) - 1);
                }
            }
            if (windowCharCount.equals(charCountS1)) {
                return true;
            }

        }
        return false;
    }
}
