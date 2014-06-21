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
     

 	 
           

if __name__== '__main__' :
   #print_fibonacci(1.9) 
   #print_fibonacci_recurse(6.5)
   print fib(5)     
