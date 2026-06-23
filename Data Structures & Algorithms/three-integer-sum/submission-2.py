class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()
        print(nums)

        

        for num in nums:
            left = nums.index(num) + 1
            right = len(nums) -1
            
            while left < right:
                
                tsum = num + nums[left] + nums[right]
                if tsum == 0:
                    solution = [num, nums[left], nums[right]]
                    if not (solution in solutions):
                        solutions.append(solution)
                        left += 1
                    else:
                        right -= 1
                        

                elif tsum < 0:
                    left += 1
                else:
                    right -= 1
        
        return solutions
        