class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # i, j=0, 0
        # for i in range(len(numbers)):
        #     for j in range(i + 1,len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]