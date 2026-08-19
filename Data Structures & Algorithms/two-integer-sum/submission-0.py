class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i, num in enumerate(nums):
            c = i
            while c+1 < l:
                c+=1
                if (num + nums[c] == target):
                    return [i, c]