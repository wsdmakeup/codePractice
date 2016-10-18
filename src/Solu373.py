#coding = utf-8

'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
'''


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        def myCompare(a, b):
            return nums1[a[0]]+nums2[a[1]] - nums1[b[0]]-nums2[b[1]]

        states = [ [0,0] ]
        allCombo = []
        size = min(k, len(nums1)*len(nums2))
        while len(allCombo) < size:
            states.sort( cmp = myCompare)
            minKey = states[0]
            allCombo.append([nums1[minKey[0]], nums2[minKey[1]]])
            key = states.pop(0)
            if key[0]+1 < len(nums1):
                newKey = [key[0]+1, key[1]]
                if newKey not in states:
                    states.append(newKey)
            if key[1]+1 < len(nums2):
                newKey = [key[0], key[1]+1]
                if newKey not in states:
                    states.append(newKey)
        return allCombo
