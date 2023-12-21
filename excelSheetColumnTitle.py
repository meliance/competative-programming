class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            reminder = columnNumber % 26
            result.append(chr(ord('A') + reminder))
            columnNumber //= 26
        return ''.join(result[::-1])