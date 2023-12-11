class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        number = x

        while x > 0:
            reminder = x % 10
            reverse = reverse * 10 + reminder
            x = x // 10

        return number == reverse