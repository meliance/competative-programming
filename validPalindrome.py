class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ''
        for i in s:
            if i.isalnum():
                if i.isalpha:
                    phrase += i.lower()
                else:
                    phrase += i
        return phrase == phrase[:: -1]