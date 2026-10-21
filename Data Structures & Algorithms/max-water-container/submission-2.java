class Solution {
    public int maxArea(int[] heights) {
          int l = 0;
        int r = heights.length-1;
        int result = 0;

        while (l < r){
            int indexDifference = r - l;
            int min = Math.min(heights[l],heights[r]);
            int currentMaxArea = min * indexDifference;
            // System.out.println("Current Max Area :" + currentMaxArea);
            if (currentMaxArea > result){
                result = currentMaxArea;
            }
            if (heights[l] > heights[r]){
                r--;
            } else {
                l++;
            }
        }

        return result;
    }
}
