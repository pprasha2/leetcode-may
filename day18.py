'''
Permutation in String
Solution
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        counterP = Counter(s1)
        counterS = Counter(s2[0:m])
        if counterP == counterS:
            return True
        n = len(s2)
        print(counterP,counterS)
        for i in range(m,n):
            if s2[i] in counterS.keys():
                counterS[s2[i]] += 1
            else:
                counterS[s2[i]] = 1
            if counterS[s2[i-m]] > 0:
                counterS[s2[i-m]] -= 1
            if counterS[s2[i-m]] == 0:
                counterS.pop(s2[i-m])
            if counterP == counterS:
                return True
        return False
