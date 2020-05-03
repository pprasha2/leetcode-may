'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        ransomNote_dict = {}

        for i in magazine:
            if i in magazine_dict.keys():
                magazine_dict[i] = magazine_dict[i] + 1
            else:
                magazine_dict[i] = 1
        for i in ransomNote:
            if i in ransomNote_dict.keys():
                ransomNote_dict[i] = ransomNote_dict[i] + 1
            else:
                ransomNote_dict[i] = 1
        #print(magazine_dict)
        #print(ransomNote_dict)
        for k,v in ransomNote_dict.items():
            if ransomNote_dict[k] > magazine_dict.get(k,0):
                return False
        return True

