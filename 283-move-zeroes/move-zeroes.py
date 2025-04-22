class Solution(object):
    def moveZeroes(self, nums):
        nonzeros = 0
        i = 0 
        n = len(nums)
        while i < n :
            if nums [i]!= 0:
                nums[i],nums[nonzeros] = nums[nonzeros], nums[i]
                nonzeros += 1
            i += 1
        