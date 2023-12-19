class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        current_product = 1
        output = [1] * n
        for i in range(n):
            output[i] *= current_product
            current_product *= nums[i]
        current_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= current_product
            current_product *= nums[i]

        return output