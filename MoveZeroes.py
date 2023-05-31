from typing import List

class Solution:
    def moveZeroes(self, nums:List[int]) ->None:
        previous_index = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                hold = nums[previous_index]
                nums[previous_index] = nums[i]
                nums[i] = hold
                previous_index+=1

s = Solution()
nums = [0, 10, 0, 3, 12]
s.moveZeroes(nums)
print(nums)