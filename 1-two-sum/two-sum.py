class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            curr= nums[i]
            needed = target - curr
            
            if needed in seen:
                return [seen[needed], i] 
            seen[curr]= i 

        return None
