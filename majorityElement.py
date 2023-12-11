class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        majority_element = max(counter, key=counter.get)
        
        if counter[majority_element] > len(nums) // 2:
            return majority_element