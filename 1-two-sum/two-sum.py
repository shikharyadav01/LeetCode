class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = {}
        for i in range(0,n):
            remaning = target - nums[i]
            if remaning in hash_map:
                return [hash_map[remaning],i]
            else:
                hash_map[nums[i]] = i 

        