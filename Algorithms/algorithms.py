#!/usr/bin/python

import types

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


if __name__== '__main__' :
   #print_fibonacci(1.9) 
   #print_fibonacci_recurse(6.5)
   #l = [-1] * 10
   #print fibo(l,0)
   #list_num = [8, 2, 4, 9, 3, 6] 
   #list_num = insertion_sort(list_num)  
   #print list_num 
