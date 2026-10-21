class Solution {
    public int findMin(int[] nums) {
        int left = 0;
    int right = nums.length - 1; // Adjust `right` to point to the last index

    while (left < right) {
        int mid = (left + right) / 2;

        // Compare nums[mid] with nums[right]
        if (nums[mid] > nums[right]) {
            // Minimum is in the right half
            left = mid + 1;
        } else {
            // Minimum is in the left half or could be nums[mid]
            right = mid;
        }
    }

    // At the end of the loop, `left` will point to the minimum
    return nums[left];
    }
}



