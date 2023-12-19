class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0
        elif len(s.split()) == 1:
            return len(s)
        return len(s.split()[-1])