class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            complement = target - nums[i]
            if complement in hashmap:
                return[hashmap[complement], i]
            else:
                hashmap[n] = i 