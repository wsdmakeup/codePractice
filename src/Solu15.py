#coding = utf-8

'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(nums2, target):
	   		result = []
	   		for idx,x in enumerate(nums2):
	   			if (target-x) in nums2[idx+1:]:
	   				result.append([x, target-x])
	   		return result
        nums.sort()
        result = []
        for idx, x in enumerate(nums):
        	target = 0 - x
        	t = twoSum(nums[idx+1:], target)
        	if len(t)>0:

        		for combo in t:
        			if combo:
        				combo.insert(0,x)
        				if combo not in result:
        					result.append(combo)

        return result



   	def twoSum(self, nums, target):
   		result = []
   		for idx,x in enumerate(nums):
   			if (target-x) in nums[idx+1:]:
   				result.append([x, target-x])
   		return result

if __name__ == '__main__':
	nums = [-1, 0, 1, 2, -1, -4]
	print Solution().threeSum(nums)