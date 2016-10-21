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
       	def findKth(l1, l2, k):
            if len(l1) == 0:
                return l2[k-1]
            if len(l2) == 0:
                return l1[k-1]
            if k == 1:
                return min(l1[k-1], l2[k-1])
            k1 = k/2
            k2 = k/2
            if k %2 ==0:
                pass
            else:
                #k是奇数,l1,l2内的索引需要是k/2+1-1, k/2-1
                k1 = k/2+1
                k2 = k/2

            if k1 > len(l1):
                #l1的太短了,但是l2足够长，在l1和l2[k/2:]内找k/2的数
                return findKth(l1, l2[k2:], k1)
            elif k2 > len(l2):
                return findKth(l1[k1:], l2, k2)
            elif l1[k1-1] == l2[k2-1]:
                return l1[k1-1]
            elif l1[k1-1] > l2[k2-1]:
                #l2内部的小于k/2-1的数据都可以丢弃的,在l2[k/2]和l1中
                #找k/2个最小的数
                return findKth(l1, l2[k2:], k1)
                pass
            else:
                #l1内部的小于k/2-1的数据都可以丢弃的,在l1[k/2]和l2中
                #找k/2个最小的数
                return findKth(l1[k1:], l2, k2)

        n = len(nums1)
        m = len(nums2)
        if (n+m) %2 ==0:
            #要找2个数
            return (findKth(nums1, nums2, (n+m+1)/2)+findKth(nums1, nums2, (n+m+1)/2+1))*1.0/2
            pass
        else:
            return findKth(nums1, nums2, (n+m+1)/2)
            


if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [1,3,4,5]
    print Solution().findMedianSortedArrays(nums1, nums2)
    a = (nums1+nums2)
    a.sort()
    print a

    nums1 = []
    nums2 = [2,3,4,5]
    print Solution().findMedianSortedArrays(nums1, nums2)
    a = (nums1+nums2)
    a.sort()
    print a

    nums1 = [1, 3]
    nums2 = [2]
    print Solution().findMedianSortedArrays(nums1, nums2)
    a = (nums1+nums2)
    a.sort()
    print a

    nums1 = [1, 2]
    nums2 = [3,4]
    print Solution().findMedianSortedArrays(nums1, nums2)
    a = (nums1+nums2)
    a.sort()
    print a

    nums1 = [2,3,4]
    nums2 = [1]
    print Solution().findMedianSortedArrays(nums1, nums2)
    a = (nums1+nums2)
    a.sort()
    print a
