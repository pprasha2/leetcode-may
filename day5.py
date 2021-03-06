'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0]* 26
        for i in s:
            freq[ord(i) - 97] += 1
        for index,item in enumerate(s):
            if freq[ord(item) - 97] == 1:
                return index
        return -1

