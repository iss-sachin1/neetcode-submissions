class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rList = []

        main_product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                main_product *= num
            else:
                zero_count += 1
        
        if zero_count == 0:
            for num in nums:
                rList.append(int(main_product / num))
        elif zero_count == 1:
            for num in nums:
                if num != 0:
                    rList.append(0)
                else: 
                    rList.append(int(main_product))
        else:
            return [0] * len(nums)
        
        return rList

        
        

        