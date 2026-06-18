class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) -1

        while left < right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid

            print(nums[left], mid, nums[right])

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid            

        print(left, nums[left])

        if nums[left] == target:
            return left
        return -1
        
