'''
Contiguous Array
Solution
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        count = {}
        cumulative = [0] * n
        if nums[0] == 1:
            cumulative[0] = nums[0]
        else:
            cumulative[0] = -1
        for i in range(1,n):
            if nums[i] == 0:
                cumulative[i] = cumulative[i-1] - 1
            else:
                cumulative[i] = cumulative[i-1] + 1
        maxlen = 0
        print(cumulative)
        current = 0
        for i in range(n):
            if cumulative[i] == 0:
                current = i + 1
            elif cumulative[i] in count.keys():
                current = i - count[cumulative[i]]
            else:
                count[cumulative[i]] = i
            if maxlen < current:
                maxlen = current
        return maxlen
