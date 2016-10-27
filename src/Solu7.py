#coding = utf-8


'''
Reverse Integer

Reverse digits of an Integer
Example1: x = -123, return 321

注意1000，0，和越界的情况，即大于计算机最大的整数
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        singal = 1
        if x < 0:
        	singal = -1
        a = str(abs(x))
        a = a [::-1]
        a = singal*int(a)
        import sys
        if a > 2**31-1 or a < -2**31:
        	return 0
        else:
        	return a


if __name__ == '__main__':
	x = 123
	print Solution().reverse(x)

	x = -123
	print Solution().reverse(x)

	x = 0
	print Solution().reverse(x)

	x = 1563847412
	print 2**32-1
	print Solution().reverse(x)
	
	x = str((2**32+1))
	x = -1*int(x[::-1] )
	print Solution().reverse(x)

