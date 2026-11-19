class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        return 0 if len(nums) <= 3 else min(nums[-1] - nums[2],nums[-3] - nums[0],nums[-2] - nums[1])