class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset[:])
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)
            
            # Do not include nums[i] (Backtrack)
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
