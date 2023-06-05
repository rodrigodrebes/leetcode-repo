class Solution(object):
    def averageValue(self, nums):
        numbers =[]
        for num in nums:
            if num % 2 == 0 and num % 3 == 0: 
                numbers.append(num)
        
        if len(numbers) == 0:
            return 0

        return int( math.floor(sum(numbers) / len(numbers)) )