class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     if nums[1] >= len(nums) - 2:
        #         return True
        # return False
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True