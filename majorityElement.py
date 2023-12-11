class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        majority_element = max(counter, key=counter.get)
        
        if counter[majority_element] > len(nums) // 2:
            return majority_element
            
        # count =0 
        # res = 0

        # for num in nums:
        #     if count == 0:
        #         res = num
        #     if num == res:
        #         count += 1
        #     else:
        #         count -= 1
        # return res