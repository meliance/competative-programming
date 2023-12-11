# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
#         magazine = list(magazine)

#         for i in ransomNote:
#             if i in magazine:
#                 magazine.remove(i)
#             else:
#                 return False
#         return True
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)

        for char, count in ransom_counts.items():
            if count > magazine_counts[char]:
                return False

        return True