class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if not height:
            return 0
        
        water_total = 0
        left_index = 0
        right_index = len(height) - 1
        left_max = 0
        right_max = 0

        while left_index < right_index:

            if height[left_index] < height[right_index]:
                if height[left_index] >= left_max:
                    left_max = height[left_index]
                else:
                    water_total += left_max - height[left_index]
                
                left_index += 1

            else:
                if height[right_index] >= right_max:
                    right_max = height[right_index]
                else:
                    water_total += right_max - height[right_index]
                
                right_index -= 1

        return water_total

