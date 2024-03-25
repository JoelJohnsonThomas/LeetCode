class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr=[]
        if len(nums)==1:
            return arr
        
        left=0
        right=1
        while left<len(nums)-1:
            if nums[left]==nums[right]:
                arr.append(nums[left])
            left+=1
            right+=1
        return arr