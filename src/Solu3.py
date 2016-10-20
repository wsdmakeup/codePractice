#coding = utf-8

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxStr = ''
        curStr = ''
        maxLen = 0
        for x in s:
        	if x in curStr:
        		curStr = curStr[curStr.find(x)+1:] + x
        	else:
        		curStr += x
        		if len(curStr) > maxLen:
        			maxLen = len(curStr)
        			maxStr = curStr
        		else:
        			continue
        return maxLen


if __name__ == '__main__':
	s = 'pwwkew'
	print Solution().lengthOfLongestSubstring(s)
