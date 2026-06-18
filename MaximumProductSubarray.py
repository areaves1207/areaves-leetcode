
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 1
        min_sum = 1

        max_ans = max(nums)

        for num in nums:
            if num == 0:
                max_sum = 1
                min_sum = 1
                continue
            prev_max = max_sum
            prev_min = min_sum

            max_sum = max(prev_max * num, prev_min * num, num)
            min_sum = min(prev_max * num, prev_min * num, num)
            
            max_ans = max(max_ans, max_sum)

        return max_ans

        
