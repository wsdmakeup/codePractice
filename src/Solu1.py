#coding = utf-8

'''
1. Two Sum   QuestionEditorial Solution  My Submissions
Total Accepted: 327359
Total Submissions: 1182428
Difficulty: Easy
Contributors: Admin
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
#next level Solution15

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = nums[:]
        l.sort()
        result = []
        start = 0
        end = len(nums) -1
        while start < end:
        	if l[start] + l[end] < target:
        		start += 1
        	elif l[start] + l[end] > target:
        		end -= 1
        	else:
        		index1 = nums.index(l[start])
        		nums.reverse()
        		index2 = len(nums) -nums.index(l[end]) -1
        		result = [index1, index2]
        		break
        return result

if __name__ == '__main__':
	nums = [-1,-2,-3,-4,-5]
	target = -8
	print Solution().twoSum(nums,target)
