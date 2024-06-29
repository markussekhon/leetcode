class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """


        if not height:
            return 0

        waterTotal, leftMax, rightMax = 0, 0, 0

        leftPointer, rightPointer = 0, len(height) - 1

        while leftPointer < rightPointer:

            if height[leftPointer] < height[rightPointer]:

                if height[leftPointer] < leftMax:
                    waterTotal = leftMax - height[leftPointer]
                else:
                    leftMax = height[leftPointer]

                leftPointer += 1

            else:

                if height[rightPointer] < rightMax:
                    waterTotal = rightMax - height[rightPointer]
                else:
                    rightMax = height[rightPointer]

                rightPointer +=1

        return waterTotal
