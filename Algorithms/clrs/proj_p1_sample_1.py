#!/usr/bin/python

def sum(a,b) :

   c = a + b
   return c

def find_function(func_name,file_name) :


   try :
   
      fp = open(file_name)

   except IOError : 

      return None

   line = fp.readline()
   print "line = ",line
   fp.close()

if __name__ == '__main__':
   print sum(5,10)
   find_function('find_function','p1.py')
