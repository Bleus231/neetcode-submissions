class Solution {
    public int search(int[] nums, int target) {
            int l = 0;
        int r = nums.length - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            // Check if mid is the target
            if (nums[mid] == target) {
                return mid;
            }

            // Determine which half is sorted
            if (nums[l] <= nums[mid]) {
                // Left half is sorted
                if (nums[l] <= target && target < nums[mid]) {
                    r = mid - 1; // Target is in the sorted left half
                } else {
                    l = mid + 1; // Target is in the right half
                }
            } else {
                // Right half is sorted
                if (nums[mid] < target && target <= nums[r]) {
                    l = mid + 1; // Target is in the sorted right half
                } else {
                    r = mid - 1; // Target is in the left half
                }
            }
        }

        // If the target is not found
        return -1;
    }
}
