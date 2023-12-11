class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        charToWord, wordToChar = {}, {}

        if len(pattern) != len(words):
            return False
        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w or w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w   
            wordToChar[w] = c
        return True