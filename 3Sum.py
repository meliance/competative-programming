class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array to make the two-pointer approach efficient
        result = []

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  
                    left += 1
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result