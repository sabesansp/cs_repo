#You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers
#and return it as a linked list.

#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8

import pdb


class ListNode(object):

  def __init__(self, x):
    self.val = x
    self.next = None

  def printVal(self):
    p = self
    while p:
      print "%d -> " % p.val,
      p = p.next
    print "None"

class Solution(object):

  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :type l3: ListNode
    """

    carry = 0
    head = None
    res = None
    while l1 and l2:
      sum = l1.val + l2.val + carry
      carry = sum / 10
      if sum>9:
        sum = sum % 10
      if not head:
        res = ListNode(sum)
        head = res
      else:
        curr = res
        res = ListNode(sum)
        curr.next = res
      l1 = l1.next
      l2 = l2.next
    while l1:
      sum = l1.val + carry
      carry = sum / 10
      if sum>9:
        sum = sum % 10
      if not head:
        res = ListNode(sum)
        head = res
      else:
        curr = res
        res = ListNode(sum)
        curr.next = res
      l1 = l1.next
    while l2:
      sum = l2.val + carry
      carry = sum / 10
      if sum>9:
        sum = sum % 10
      if not head:
        res = ListNode(sum)
        head = res
      else:
        curr = res
        res = ListNode(sum)
        curr.next = res
      l2 = l2.next
    if carry>0:
      print "inside carry GT 0"
      n = ListNode(carry)
      res.next = n
    return head

if __name__ == '__main__':
 
  s = Solution()
  o = ListNode(2)
  o1 = ListNode(5)
  o1.next = o
  l2 = ListNode(5)
  h = s.addTwoNumbers(o1, l2)    
  h.printVal()







