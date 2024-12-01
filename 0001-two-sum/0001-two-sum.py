class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We're going to loop through nums by (i, n).
        # Let's create a hashmap that can store {n: i}.
        hashmap = {}

        # the loop
        for i, n in enumerate(nums):
            # we get the diff of target minus n
            diff = target - n

            # here is where the magic happens
            if diff in hashmap:
                return [hashmap[diff], i]

            # here we populate the hashmap with {n: i}
            hashmap[n] = i