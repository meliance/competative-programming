class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        arr = {}
        
        for i, j in enumerate(nums):
            if j in arr and i - arr[j] <= k:
                return True
            arr[j] = i
        return False