#!/usr/bin/python

import re

def sum(a,b) :

   c = a + b
   return c

def find_function(func_name,file_name) :


   try :
   
      fp = open(file_name)

   except IOError : 

      raise IOError

   line = fp.readline()
   lineno = 1
   answer = None
   # Iterate through all the lines in the file

   while(line!= '') :
      cre = re.compile(r'def\s+%s\s*[(]' % re.escape(func_name))
      if cre.match(line) :
         answer = lineno
         break 
      line = fp.readline()
      lineno = lineno + 1

   fp.close()
   return answer

if __name__ == '__main__':
   # expected = 15
   print sum(5,10)

   # expected = 12
   print find_function('create_dataset','p1.py')
