#!/usr/bin/python

import types
from ctypes import c_int,addressof
import sys


# P1 : Print 'n' numbers in the fibonacci sequence using iteration
 # n = 5 => sequence = [0,1,1,2,3]
  # E1 : l = 0, r = 1,i = 3
  # E2 : s = l + r  
  # E3 : print s
  # E4 : l = r, r = s, i++
  # E5 : (E2) if i<=5, else E6
  # E6 : STOP


def print_fibonacci(n) : 
   if n <= 0 or type(n) != types.IntType :
      print("Error: n cannot be negative or zero and should be an integer")
   else :
      i = 0
      l = 0
      r = 1
      while i < n :
         if i >= 2 :
            s = l + r
            print s
            l = r
            r = s
         else : 
            print i
         i = i + 1

# P2 : Print 'n' numbers in the fibonacci sequence using recursion
 # n = 6 => sequence = [0,1,1,2,3,5]
  # E1 : variables => n=6, l=0, r=1
  # E2 : 'n < 0' or 'type(n)' is not integer => print error message
  # E3 : 'n == 0' return (base case) 
  # E4 : 'n <= 2' => print n
  # E5 : 'n > 2' => print s = l+r, go to step E1 with n=5 (n-1), l=r,r=s       
 
def print_fibonacci_recurse(n,l,r) :
   if n<0 or type(n) != types.IntType :
      print 'Error: n cannot be negative and should be an integer'
      return
   if n==0 :
      return
   if n<=2 :
      print n-1
      print_fibonacci_recurse(n-1,l,r)
   if n>2 :
      s = l + r 
      print s
      print_fibonacci_recurse(n-1,r,s) 


# P3 : Print the nth number in the fibonacci sequence using recursion
 # n = 6 => output = 5
  # fib(n) = fib(n-1) + fib(n-2)
  # fib(1) = 0
  # fib(0) = returns from the function
  # fib(-1) = undefined (Error message) 
  # fib(-2) = undefined (Error message) 
  # fib(1.1) = undefined (Error message) 
  # fib(-1.5) = undefined (Error message) 
  # fib(2) = fib(1) + fib(0) = 0 

def fib(n) : 
   if n<0 or type(n) != types.IntType :
      print 'Error: n cannot be negative and should be an integer'
      return -1
   if n==0 : 
      return
   if n<=2 :
      return n-1
   else :
      return fib(n-1) + fib(n-2)
     

# P4 : Reduce redundant operations in the computation in P3
 # problem => l(4) = 5th number in the fibonacci sequence
 # l(4) = l(3) + l(2) 
 # l(3) = l(2) + l(1) 
 # l(2) = l(1) + l(0)
 # l(1) = 1
 # l(0) = 1
 # l = [-1 -1 -1 -1 -1]
 # fibo(l,4) = fibo(l,3) + fibo(l,2) 
 # fibo(l,3) = fibo(l,2) + fibo(l,1) 
 # fibo(l,2) = fibo(l,1) + fibo(l,0) 
 # fibo(l,1) = l[1] = 1
 # fibo(l,0) = l[0] = 0
 # fibo(l,2) = 1 + 0 = 1	  

def fibo(l,start) : 
   if start<2 : 
      l[start] = start
   else :
      l[start] = l[start-1] + l[start-2]
      print l
      print 'start =',start
      if start==len(l)-1 :
         return l[start]         
   if start<len(l)-1 :
      return fibo(l,start+1)


# P5 : Implement a swap function 

def swap(a,b) : 
   return b,a

# P6 : Implement insertion sort for a list of numbers

def insertion_sort(list_num) :
   j = 1
   # j moves from 1 to n-1 where n = length of list 'list_num'
   while j<len(list_num) :
      # Set i to 0 each time this loop starts
      i = 0
      # i moves from 0 to j-1
      while i<=j-1 :
         # i < j => we need to make list_num[i] <= list_num[j]
         if list_num[j] < list_num[i] :
            # swap the numbers if the condition list_num[i] <= list_num[j] is not maintained
            tmp = list_num[i] 
            list_num[i] = list_num[j]
            list_num[j] = tmp
         # increment i for the inner loop
         i = i + 1
      # increment j for the outer loop
      j = j + 1
   # return the list
   return list_num  


# P7 : Implement a 2-way merge of numbers sorted in ascending order
#      list l1 = l[start] -> l[mid] || list l2 = l[mid+1] -> l[end] 

def merge(l1,l2) : 
   i = 0
   j = 0
   k = 0
   l = [None] * (len(l1) + len(l2))  
   while i<len(l1) and j<len(l2)  :
      if l1[i] < l2[j] :
         l[k] = l1[i] 
         i = i + 1
      else :
         l[k] = l2[j]
         j = j + 1 
      k = k + 1
   # If the left list was not exhausted
   if i<len(l1) :
      while i<len(l1) :
         l[k] = l1[i] 
         i = i + 1
         k = k + 1

   # If the right list was not exhausted
   if j<len(l2) :
      while j<len(l2) :
         l[k] = l2[j]
         j = j + 1
         k = k + 1
   return l


# P8 : Implement the merge sort function using "merge" function
# Picture a 4-element list = [4,2,9,1] 
# n = 4, l = [4,2,9,1], left = merge_sort([4.2])
# n = 2, l = [4,2], left = merge_sort([4]) 
# n = 1, l = [4], returned
# n = 2, l = [4,2], right = merge_sort([2]) 
# n = 1, l = [2], returned
# n = 2, l = [4,2] , left = [4], right = [2] 
# merge => [2,4] returned
# n = 4, l = [4,2,9,1], left = [2,4], right = merge_sort([9,1]) 
# n = 2, l = [9,1], left = merge_sort([9]) 
# n = 1, l = [9], returned
# n = 2, l = [9,1], left = [9], right = merge_sort([1]) 
# n = 1, l = [1], returned
# n = 2, l = [9,1], left = [9], right = [1]
# merge => [1,9] returned
# n = 4, l = [4,2,9,1], left = [2,4], right = [1,9]
# merge => [1,2,4,9] 
 
def merge_sort(l) :
  
   n = len(l)
   if n<=1 :
      return l 
   left = merge_sort(l[:n/2]) 
   right = merge_sort(l[n/2:])
   return merge(left,right)  
   


# P9 : Build a sample graph datastructure 

def build_graph():

   graph = {'A' : ['B','D'],
            'B' : ['C'],
            'C' : ['F','E'],
            'D' : ['E'],
            'E' : ['F'],
           }
   return graph


# P10 : Check if there exists a path between two nodes in a graph

def is_path_exists(graph,start_node,end_node):

   # check if start_node is a key in the graph
   if graph.has_key(start_node) :
      l = graph[start_node]
      if end_node in l :
         return True
      else :
         for node in l :
            return is_path_exists(graph,node,end_node)
   return False



# P11 : Print the address of the stored variable
def print_address() :

   a = 5;
   print "address of a  = ",hex(addressof(c_int(a)))
 
   # Expected value would be 24 bytes, reason being
   # every python object contains atleast a refcount
   # and a reference to the object's type in addition
   # to other storage on a 64-bit machine, that takes 
   # upto 16 bytes	
   # typedef struct	 {
   #   PyObject_HEAD
   #   long ob_ival;
   # }PyIntObject;
   # 
   # struct _intblock {
   #  struct _intblock *next;
   #  PyIntObject objects[N_INTOBJECTS];
   # };
   # typedef struct _intblock PyIntBlock;

   print "size of 'a' using getsizeof function= ",sys.getsizeof(a)
   print "size of 'a' using bit length = ",a.bit_length() 
   

#P12 : Print the bytes in the passed variable
def show_bytes(input):

   print "Entire input in bytes = ",hex(input)
   while input!=0 and input!=-1 :
      print "input = ",input
      print "byte = ",hex(input&0xFF)
      input = input >> 8



#P13 : Find a peak if it exists in an array of numbers
def find_peak(a):

   # Example : [5,4,2,1,7,9]
   # Set the left and right ends of the list
   l = 0 # points to 5
   r = len(a)-1 # points to 9

   while l<=r:

      # Compute the mid-point of the list
      m = (l + r)/2 # mid = 1
 
      # If m=0, check a[m]>a[m+1] 
      if m==0 :
         if a[m]>=a[m+1] :
            # condition => a[m] is a peak, output the same
            return a[m]
      else :
         if m==len(a)-1 :
            if a[m]>=a[m-1] :
               # condition => a[m] is a peak, output the same
               return a[m]
         else :
            # cond => 0 < m < len(a)-1
            if a[m]>=a[m-1] and a[m]>=a[m+1] :
               # condition => a[m] is a peak
               return a[m]
            else :
               # cond => a[m] was not the peak
               if a[m]<a[m-1] :
                  r=m-1
               else :
                  if a[m]<a[m+1] :
                     l=m+1    
      
   return None


# P14 : Implement a binary search algorithm for finding a number in the list of numbers
#       Return position if found, -1 otherwise
def binary_search(a,n):

   # Example: a = [3,9,27,100,150,200]
   # n = 9 | 0 
   # Assumption: Input list is sorted already
   # Fix l to be left end of array ; r to be right end of array
   l = 0 # a[l] = 3
   r = len(a)-1 # a[r] = 200

   while l<=r:
      
      # Compute the mid-point of the list
      m = (l+r)/2

      # If a[m] > n => r = m - 1
      if a[m] > n :
         r = m - 1
      else :
         # If a[m] < n => l = m + 1
         if a[m] < n:
            l = m + 1
         else:
            # a[m] will be the element that is being searched for
            # return the position m
            return m
   
   # if there was no return statement executed
   # within the while loop, it means that 
   # the number was not found, return -1

   return -1 
         
# P15 : Compute the pth power of n
def compute_power(n,p):
  
   # initialize variables here
   i = 1
   power = 1

   # run the while loop from 1 to p
   while i<=p:
      power *= n
      i += 1
   
   return power
   
# SP1 : Check whether a number is even or odd 
def is_odd(n):

   return n%2 != 0

# SP2 : Split a number into two parts, 
#       a => first 'p' digits
#       b => rest of the digits together
def split_num(n,p,t) :

   # n=5567, p=2, expected_output = (55, 67)
   # n=330, p=2, expected_output = (33,0)
   # t=3 (total number of digits) 
   #   
   d = compute_power(10,t-p)
   print "p = ",p
   print "d = ",d
   print "n = ",n
   print "t = ",t
   a = n/d
   b = n%d
   print "a = ",a
   print "b = ",b
   return (a,b) 



# P16 : Compute integer multiplication of n digits recursively 
def int_mult(x,y,n):

   if n==1:
      return x*y

   # x = 330 , y = 225, n = 3
   # compute a,b,c,d
   # a = 33, b = 0, c = 22, d = 5
   # when n is odd, p = (n/2 + 1) digits in the number
   if is_odd(n) :
      p = n/2 + 1
   else :
      p = n/2 

   # Compute a,b,c,d 
   (a,b) = split_num(x,p,n)
   (c,d) = split_num(y,p,n)
  
   # Complete return statement
   # there is a bug hidden for odd values of 'n' => figure out the bug
   return compute_power(10,n)*int_mult(a,c,p) + compute_power(10,n/2)*(int_mult(a,d,p) + int_mult(b,c,p)) + int_mult(b,d,p)
      
if __name__== '__main__' :
   #print_fibonacci(1.9) 
   #print_fibonacci_recurse(6.5)
   #l = [-1] * 10
   #print fibo(l,0)
   #list_num = [8, 2, 4, 9, 3, 6] 
   #list_num = insertion_sort(list_num)  
   #print list_num
   #print merge_sort([2, 5, 9, 253,-25,0,7,32,89])
   #print build_graph()  
   #print is_path_exists(build_graph(),'C','D')
   #print_address()
   #show_bytes(-214734894)
   #print find_peak([5,4,2,1,7,9,10,8,4,0])   
   #print binary_search([-3,-4,1,2,6,250],250)
   #print binary_search([0,1],0)
   #print binary_search([2,3,4],5) 
   #print compute_power(10,2)
   print int_mult(3000,2000,4) 
   
