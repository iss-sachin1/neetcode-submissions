class Solution:
    def maxArea(self, heights: List[int]) -> int:

        volume = 0
        left = 0
        right = len(heights) - 1

        while left <= right:
            if left == right:
                right = len(heights) - 1
                left += 1
            height = 0
            width = right - left
            


            if heights[left] > heights[right]:
                height = heights[right]
            else:
                height = heights[left]
            
            if height * width > volume:
                volume = height * width

            right -= 1
        return volume
            
            
            
            

        