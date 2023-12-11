class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroCounts=0
        while n > 0:
            n//=5
            zeroCounts += n
        return zeroCounts