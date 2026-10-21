class Solution {
        public int search(int[] nums, int target) {
    int low = 0;
        int high = nums.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2; // Prevents overflow
            
            if (nums[mid] == target) {
                return mid; // Found target, return its index
            } else if (nums[mid] < target) {
                low = mid + 1; // Search in the right half
            } else {
                high = mid - 1; // Search in the left half
            }
        }
        return -1; // Target not found
        }
}
