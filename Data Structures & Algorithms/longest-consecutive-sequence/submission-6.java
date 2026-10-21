class Solution {
    public int longestConsecutive(int[] nums) {
         int largestCounter = 1;
        int counter = 1;
        Arrays.sort(nums);

        if (nums.length == 0){
            return 0;
        }
        
        for (int i=0; i < nums.length-1;i++){
            int current = nums[i];
            int next = nums[i+1];
            int difference = next - current;

            if (difference == 1 ){
                counter++;
                if (counter > largestCounter){
                    largestCounter = counter;
                }
            } else if (difference == 0){

            }else {
                counter = 1;
            }
            
        }
        return largestCounter;
    }
}
