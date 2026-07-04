class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)
        rob1, rob2 = nums[0], max(nums[0],nums[1])

        for i in range(2, n):
            rob1, rob2 = rob2, max(nums[i] + rob1, rob2)
        return max(rob1, rob2)