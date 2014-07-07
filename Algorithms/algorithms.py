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
   while j<len(list_num) :
      i = 0
      while i<=j-1 :
         if list_num[j] < list_num[i] :
            tmp = list_num[i] 
            list_num[i] = list_num[j]
            list_num[j] = tmp
         i = i + 1
      j = j + 1
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
   print_address()  
