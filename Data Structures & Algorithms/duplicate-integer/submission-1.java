class Solution {
    public boolean hasDuplicate(int[] nums) {
    int current = 0;
        ArrayList<Integer> ints2 = new ArrayList<>();
        
        for(int i =0; i < nums.length;i++){
            current = nums[i];
            
            if(ints2.contains(current)){
                return true;
            } else{
                ints2.add(current);
            }
            
            
        }
        return false;
    }
}
