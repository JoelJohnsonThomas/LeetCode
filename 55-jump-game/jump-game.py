class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < x:
                x += 1
            else:
                x = 1
        return x == 1