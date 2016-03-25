# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers
# and return it as a linked list.


# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


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
    
    # Initialize all the required variables
    l3 = None
    res = None
    carry = 0
    s = 0
        
    # Iterate through lists l1 and l2 only if l1 and 
    # l2 have elements to be iterated in conjunction
    # with each other
    while l1 and l2:
      s = l1.val + l2.val + carry
      carry = s / 10
      if s > 9:
        s = s % 10
      curr = res
      res = ListNode(s)
      if not l3:
        l3 = res
      else:
        curr.next = res
      l1 = l1.next
      l2 = l2.next
        
    # Iterate through list l1
    while l1:
      s = l1.val + carry
      carry = s / 10
      if s > 9:
        s = s % 10
      curr = res
      res = ListNode(s)
      if not l3:
        l3 = res
      else:
        curr.next = res
      l1 = l1.next
    
    # Iterate through list l2
    while l2:
      s = l2.val + carry
      carry = s / 10
      if s > 9:
        s = s % 10
      curr = res
      res = ListNode(s)
      if not l3:
        l3 = res
      else:
        curr.next = res
      l2 = l2.next
     
    # Only if carry is greater than 
    # zero we need to consider adding an 
    # extra node in the linked list
    if carry > 0:
      n = ListNode(carry)
      res.next = n 
       
    return l3
        
                
        
        
            
         

if __name__ == '__main__':
 
  s = Solution()
  o = ListNode(2)
  o1 = ListNode(5)
  o1.next = o
  l2 = ListNode(5)
  h = s.addTwoNumbers(o1, l2)    
  h.printVal()






