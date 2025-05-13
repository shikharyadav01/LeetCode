class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        low = 0
        high = n -1
        ans = n

        while low <= high:
            mid = (low + high) // 2

            #maybe an answer 

            if nums[mid]>=target:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        
        