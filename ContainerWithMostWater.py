class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        lptr=0
        rptr=len(height)-1

        def area(lptr, rptr):
            return min(height[lptr], height[rptr]) * (rptr-lptr)

        max_area = area(lptr, rptr)


        while lptr != rptr:
            # print(max_area)
            if height[lptr] > height[rptr]:
                # print("move right pointer")
                rptr -= 1
            else:
                # print("move left pointer")
                lptr +=1
            if area(lptr, rptr) > max_area:
                max_area = area(lptr, rptr)
        return max_area

        
