class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers for the search range
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Find the middle index
            median = (right - left) // 2 + left

            # Narrow the search range based on target comparison
            if target < nums[median]:
                right = median - 1  # Search left half
            elif target > nums[median]:
                left = median + 1  # Search right half
            else:
                return median  # Target found

        # Return -1 if target is not found
        return -1
