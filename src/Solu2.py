#coding = utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1 = l1
        c2 = l2
        l = None
        head = None
        numSum = 0
        while (c1!= None or c2 != None):
        	if c1 :
        		numSum += c1.val
        		c1 = c1.next
        	if c2 :
        		numSum += c2.val
        		c2 = c2.next
        	if l == None:
        		l = ListNode(numSum % 10)
        		head = l
        	else:
        		l.next = ListNode(numSum % 10)
        		l = l.next
        	numSum /= 10
        if numSum == 1:
        	l.next = ListNode(numSum % 10)
        result = []
        while head != None:
        	result.append(head.val)
        	head = head.next
        return result

if __name__ == '__main__':
	l1 = ListNode(2)
	l1.next = ListNode(4)
	l1.next.next = ListNode(3)
	l2 = ListNode(5)
	l2.next = ListNode(6)
	l2.next.next = ListNode(4)
	print Solution().addTwoNumbers(l1,l2)

