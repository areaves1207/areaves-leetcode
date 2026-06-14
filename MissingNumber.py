class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1 and nums[0] == 1):
            return 0
        if(len(nums) == 1 and nums[0] == 0):
            return 1

        n = len(nums)+1
        m = (n*(n-1))/2
        a = 0
        for num in nums:
            a += num

        return m - a

        
