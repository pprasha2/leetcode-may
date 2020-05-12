'''
Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10


Note: Your solution should run in O(log n) time and O(1) space.
'''
class Solution:
    def search(self,arr,l,r):
        if l == r:
            return arr[l]
        mid = l + (r - l) // 2
        if mid % 2 == 0 and mid < r:
            if arr[mid] == arr[mid+1]:
                return self.search(arr,mid+1,r)
            else:
                return self.search(arr,l,mid)
        else:
            if mid > 0 and arr[mid] == arr[mid-1]:
                return self.search(arr,mid+1,r)
            else:
                return self.search(arr,l,mid)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return self.search(nums,0,len(nums)-1)


