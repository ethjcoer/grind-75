# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # This function finds the first bad version in the range [1, n].
        # It uses binary search to achieve O(log n) time complexity.

        left, right = 1, n  # Initialize the search bounds.

        while left < right:
            # Calculate the middle point of the current range.
            # Adding left ensures no overflow when (left + right) is large.
            median = ((right - left) // 2) + left

            if isBadVersion(median):
                # If the median is bad, the first bad version is at or before median.
                right = median
            else:
                # If the median is not bad, the first bad version is after median.
                left = median + 1

        # When the loop ends, left == right, pointing to the first bad version.
        return left
