class Solution {
    public int[] twoSum(int[] numbers, int target) {
           int l = 0;
        int r = numbers.length - 1;
        int [] results = new int[2];

        while (l < r){
            int first = numbers[l];
            int last = numbers[r];

            if (first + last == target){

                return new int[] {l + 1,r + 1};
            }
            if (first + last > target){
                r--;
            } else {
                l++;
            }



        }



        return results;
    }
}
