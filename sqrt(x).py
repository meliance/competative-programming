class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        result = 0
        while left <= right:
            mid = (right + left) // 2
            square = mid * mid
            if square <= x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result