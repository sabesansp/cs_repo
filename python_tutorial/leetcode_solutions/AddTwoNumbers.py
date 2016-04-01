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
    :type head: ListNode
    """
    
    # Initialize all the required variables
    l = None
    l3 = None
    carry = 0
    
    while l1 or l2:
      p1 = l1.val if l1 else 0
      p2 = l2.val if l2 else 0
      sum = carry + p1 + p2
      carry = sum / 10
      sum = sum % 10 if sum > 9 else sum
      prev = l
      l = ListNode(sum)
      if not l3:
        l3 = l
      else:
        prev.next = l
      if l1:
        l1 = l1.next
      if l2:
        l2 = l2.next       
    return l3
        
                
        
        
            
         

if __name__ == '__main__':
 
  s = Solution()
  o = ListNode(2)
  o1 = ListNode(5)
  o1.next = o
  l2 = ListNode(5)
  h = s.addTwoNumbers(o1, l2)    
  h.printVal()






