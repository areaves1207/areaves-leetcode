

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        left_ptr = 0
        right_ptr = len(nums)-1
        ans = []

        for i in range(len(nums)):
            val = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left_ptr = i+1
            right_ptr = len(nums)-1
            

            while(left_ptr < right_ptr):
                l = nums[left_ptr]
                r = nums[right_ptr]

                if(l+r+val == 0):
                    a = [val, l, r]
                    ans.append(a)
                    left_ptr += 1
                    right_ptr -= 1
                    while(left_ptr < right_ptr and nums[left_ptr] == l):
                        left_ptr += 1
                    while(right_ptr >= left_ptr and nums[right_ptr] == r):
                        right_ptr -= 1
                else:
                    if(r + l < -val):
                        left_ptr += 1
                    else:
                        right_ptr -= 1

        return ans

