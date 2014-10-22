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

# SP3 : Compute the number of digits in a number
def num_digits(x) :

   if x==0:
      return 1
   c=0
   # ex : 330 => number of digits = 3
   # 330 % 10 = 0
   # 330 / 10 = 33
   # 33 % 10 = 3
   # 33 / 10 = 3
   while x!=0 :
      c+=1
      x/=10
   print "number of digits = ",c
   return c      

# P16 : Compute integer multiplication of n digits recursively 
def int_mult(x,y):

   # iter_1: nx=3,ny=3,x=330,y=225,n=3,p=2,a=33,b=0,c=22,d=5
   # iter_2: nx=2,ny=2,x=33,y=22,a=3,b=3,c=2,d=2,n=2
   # iter_3: x=3,y=2, ret(6)
   # iter_2: 100*6 + 10*(6+6) + 6
   #         ret(600 + 120 + 6) = ret(726) 
   # iter_4: x=3,y=2, ret(6)
   # iter_5: =iter_4
   # iter_6: =iter_4
   # iter_1: 1000*mult(33,22) + 10*(mult(33,5)+mult(0,22)) + mult(0,5)
   #         726000 
   nx = num_digits(x)
   ny = num_digits(y) 
   n = nx if nx>ny else ny
   if n==1:
      return x*y

   if is_odd(n) :
      p = n/2 + 1
   else :
      p = n/2 
   (a,b) = split_num(x,p,n)
   (c,d) = split_num(y,p,n)
   if is_odd(n) :
      return compute_power(10,p)*int_mult(a,c) + compute_power(10,n/2)*(int_mult(a,d) + int_mult(b,c)) + int_mult(b,d)
   else :
      return compute_power(10,n)*int_mult(a,c) + compute_power(10,n/2)*(int_mult(a,d) + int_mult(b,c)) + int_mult(b,d)

# P17 : Implement a three-way merge on sorted lists in ascending order
def merge_three(l1,l2,l3):

   return merge(merge(l1,l2),l3)        


# SP : Calculate the median in a sorted array "a"
def median(a,n):
   if is_odd(n):
      return a[n/2],n/2
   else :
      return a[n/2 - 1],n/2-1 
            

# SP : test pythonic behavior when list references are passed in incremental form
#      '+' is actually treated as a concatenation operator
def test_list(a):
   print a


# SP : Return the maximum of two numbers
def max(a,b):
   if a>b:
      return a
   else :
      return b


# SP : Return the minimum of two numbers
def min(a,b):
   if a<b:
      return a
   else :
      return b


# P18 : Implement an algorithm that outputs the item whose key is the 
#       lower median in the union of 's' and 't'.
# t(n) => 84m
# idea => http://www.geeksforgeeks.org/median-of-two-sorted-arrays/
def union_median(s,t,n):
   print "s = ",s
   print "t = ",t
   # call_1 : 
   #   s=[3,6,7,9]; t=[-1,1,2,8]; 
   #   s_start = 0; s_end = n-1
   #   t_start = 0; t_end = n-1
   #          
   (m1,m1_index) = median(s,n)
   (m2,m2_index) = median(t,n) 
   if n==0:
      return
   if n==1:
      return min(s[0],t[0]) 
   if n==2:
      return max(s[0],t[0])
   # call_1 : m1 = 6 ; m2 = 1
   if m1==m2 :
      return m1 
   if m1>m2:
      if is_odd(n):
         return union_median(s[:m1_index+1],t[m2_index:],n/2+1)
      else :
         return union_median(s[:m1_index+1],t[m2_index:],n/2)            
   else :
      if is_odd(n):
         return union_median(s[m1_index:],t[:m2_index+1],n/2+1)
      else :
         return union_median(s[m1_index:],t[:m2_index+1],n/2)   
      
# P19 : Implement a 2-way merge of numbers sorted in ascending order
#       list l1 = l[start] -> l[mid] || list l2 = l[mid+1] -> l[end]
#       and count the number of inversions 

def count_inversions(l1,l2) : 
   i = 0
   j = 0
   k = 0
   c =0
   l = [None] * (len(l1) + len(l2))
   print "left list in count_inversions : ",l1
   print "right list in count_inversions : ",l2
   while i<len(l1) and j<len(l2)  :
      if l1[i] < l2[j] :
         l[k] = l1[i] 
         i = i + 1
      else :
         l[k] = l2[j]
         j = j + 1
         c = c + (len(l1) - i) 
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
   print "merged_list in count_inversions = ",l
   print "count in count_inversions = ",c
   return l,c


# P20 : Implement the merge sort function for computing inversions
# T(n) => 106m 
def sort_count(l) :
  
   # call_1 : l = [5,4,3,2,1] 
   #          n = 5
   # call_2 : l = [5,4]
   #          n = 2
   # call_3 : l = [5],n = 2,left=[5],x=0,  
   # call_4 : l = [4,3,2,1], n = 4,           
   n = len(l)
   if n<=1 :
      return l,0 
   
   
   (left,x) = sort_count(l[ :n/2]) 
   print "left = ", left
   print "x = ",x
   (right,y) = sort_count(l[n/2:])
   print "right = ",right
   print "y = ",y 
   (merged,z) = count_inversions(left,right)
   print "merged = ",merged
   print "z = ",z 
   return merged,x+y+z 


# SP : Function returns the absolute value of a number
def abs(a):

   if a < 0 :
      return -a
   else :
      return a
   
# SP : compute the euclidean distance in 1 dimension
def compute_linear_distance(a,b):
   
   return abs(a - b) 


# P21 : Implement a function that takes a list and 
# outputs the minimum distance value between the numbers  
def min_dist(input_list):

   # Example : [3,4,6,9,11,45,87,99,101] 
   # n = 9 
  
   # if input list was none, -1 should be returned 
   if input_list==None :
      return -1

   merged_list = merge_sort(input_list) 

   # compute the length of the input list
   n = len(merged_list)
   
   # i : counter to keep track of the array
   i = 0
   min_delta = merged_list[0]
   output_list = [0,min_delta]

   while i<n-1 :
      delta = compute_linear_distance(merged_list[i],
                                      merged_list[i+1])   
      if delta<min_delta :
         min_delta = delta
         output_list= [merged_list[i],merged_list[i+1]]

      i = i + 1
      
   return output_list      

 
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
   #print int_mult(33,5) 
   #print num_digits(32984)i
   #print merge_three([2,3,4],[21,67,90],[35,45,55,76,95])
   #a = [34, 67, 89, 91]
   #test_list(a[2:2:2])
   #print union_median([3,6,7,9],[-1,1,2,8],4) ## Works for even numbers in the list
   #print union_median([5,10,34,65,78],[2,3,4,6,9],5) ## Works for odd numbers in the list as well
   #(l,c) = sort_count([6,5,4,3,2,1]) # this code does not work
   #print c
   #print abs(8)
   print min_dist([6,4,3,18,9,45,25]) # runs in O(nlogn) time
   
