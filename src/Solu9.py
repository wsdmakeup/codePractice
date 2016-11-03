# -*- coding:utf-8 -*-

'''
Determine whether an integer is a palindrome. Do this without extra space.
'''

'''
不可以使用转换str的方法。
将自然对比转换为每次对比最左边和最右边，然后掐头去尾，就是数字除以100，
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        a = x
        c = a 
        n = 0
        flag = True 
        while(c>0):
        	n += 1
        	c = c/10
        print n
        for idx in range(n):
        	if idx > n -1 -idx:
        		break
        	else:
        		n1 = (a % (10**(idx+1)))/(10**idx)
        		
        		n2 = (a / (10**(n-idx-1)))%10
        		print n1,n2
        		if n1!=n2:
        			flag = False 
        return flag

    def anotherTry(self, x):
    	if x < 0:
    		return False
    	d = 1
    	while x/d >= 10:
    		d = d*10
    	while(x !=0):
    		l = x / d
    		r = x % 10
    		if l != r:
    			return False
    		x = x % d
    		x = x /10
    		d = d /100
    	return True

if __name__ == '__main__':
	x = 123
	print Solution().anotherTry(x)

	x = 12321
	print Solution().anotherTry(x)

	x = 123321
	print Solution().anotherTry(x)

	x = -2147447412
	print Solution().anotherTry(x)

	x = 0
	print Solution().anotherTry(x)