class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> charFrequency = new HashMap<>();
            int left = 0;
            int right = 0;
            int maximumFrequency = 0;
            int result = 0;

            while (right < s.length()) {
                char c = s.charAt(right);
                charFrequency.put(c, charFrequency.getOrDefault(c, 0) + 1);

                // Update the maximum frequency seen so far
                maximumFrequency = Math.max(maximumFrequency, charFrequency.get(c));

                // Check if the current window is valid
                if ((right - left + 1) - maximumFrequency > k) {
                    char leftChar = s.charAt(left);
                    charFrequency.put(leftChar, charFrequency.get(leftChar) - 1);
                    left++; // Shrink the window
                }

                // Update the result (window size)
                result = Math.max(result, right - left + 1);

                right++; // Expand the window
            }

            return result;
    }
}
