class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set() # take an empty set and add elements of original nums
        n = len(nums)

        for i in range(0,n):
            my_set.add(nums[i])

        longest = 0

        for num in my_set:
            if num - 1 not in my_set:
                x = num 
                count = 1 
                while x + 1 in my_set:
                    count += 1 
                    x += 1 
                longest = max(longest , count)
        
        return longest 