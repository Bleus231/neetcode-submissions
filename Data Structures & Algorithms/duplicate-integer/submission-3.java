class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> duplicationCheck = new ArrayList<>();

        for (int i=0; i < nums.length;i++ ){
            int current = nums[i];

            if (!duplicationCheck.contains(current)){
                duplicationCheck.add(current);
            } else {
                return true;
            }

        }

        return false;
    }
}
