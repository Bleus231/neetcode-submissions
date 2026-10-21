class Solution {
    public int[] twoSum(int[] nums, int target) {
      int current = 0;
        int next =0;
        int sum1 = 0;
        int sum2 =0;
        for (int i=0; i < nums.length;i++){
             current = nums[i];
            for (int j =1; j<nums.length; j++){
                next = nums[j];
                if (current + next == target && i != j){
                    sum1 = i;
                    sum2 = j;
                }
            }
        }

        int min = Math.min(sum1,sum2);
        int max = Math.max(sum1,sum2);

        int[] answer = {min,max};

        return answer;
    }
}
