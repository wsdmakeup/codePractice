#coding=utf-8

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
http://www.geeksforgeeks.org/median-of-two-sorted-arrays/
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
       	

if __name__ == '__main__':
	nums1 = [1,23,4345,234]
	nums2 = [2,34,123,123,32434]
	print Solution().findMedianSortedArrays(nums1, nums2)
