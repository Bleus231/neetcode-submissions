class Solution {
    public int maxArea(int[] heights) {
    int l = 0;
     int r = heights.length-1;
     int maxArea =0;
     while (l < r){
         int min = Math.min(heights[l],heights[r]);
         int difference = r - l;
        int maxArea2 = min * difference;
         if (maxArea2 > maxArea ){
             maxArea = maxArea2;
         }
         if (heights[l] < heights[r]){
             l++;
         } else {
             r--;
         }


     }
    return maxArea;
    }
}
