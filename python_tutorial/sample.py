# This is a sample python file which can be used
# to teach programming to beginners in python


from multiprocessing import Process
import sys
import traceback


# Task1 : Adjust vim editor to make sure that each line does not exceed 90 characters,test
def main():

   print "Inside main function: make sure that this line extends 90 character limit"


# Task 2: Add a method to test validity of an ipv4 address
def is_valid_ipv4_addr(ip):

   octets = ip.split(".")
   if len(octets) != 4 :
      return False
   return all(0 <= int(octet) <= 255 for octet in octets)


# Task 3: Write a method and spawn this method as a process
def run_as_process(name):
   try:
      vm = None
      # Inject an error here to check 
      # what happens to the process when this is run
      if vm.is_valid():
         print "vm is valid"
      print "Inside function run_as_process : %s" %(name)
   except:
      print "Unexpected error : ", sys.exc_info()
      return False
   return True


# Task 4: catch the exception above and return true or false based on the outcome
def call_process():

   print "Calling run_as_process\n",run_as_process('process:sabesan')


# Task 5: write a function with kwargs and call function from main
def func_kwargs(**kwargs):
   for key,value in kwargs.iteritems():
      print "%s = %s" % (key,value)


# Task 6: write a while loop and throw an exception inside that
def func_while_exception():
   try:
      while True:
         vm = None
         if vm.is_valid():
            print "vm is valid"
   except:
      print "Inside except block, caught exception"


# Task 7 : Print with an extra pair of braces
def print_braces():
   name = 'sabesan'
   print "My name is : %s" %((name))

# Task 8 : Induce an IndexError and catch the same
def check_IndexError():
   try:
      l = []
      print 0/0
   except IndexError as indexerror:
      print "Failed exception : %s" % indexerror
   except Exception as exc:
      #print "exception : %s" % exc
      print "traceback : %s" % traceback.format_exc()
      
      


if __name__ == '__main__':
   main()

   # Expected value = true
   print is_valid_ipv4_addr('10.4.66.239')

   # Expected value = false
   print is_valid_ipv4_addr('10.456.34.255')


   # Run the previous function as a process
   p = Process(target=call_process, args=()) 
   p.start()
   p.join() # this blocks until process terminates

   # Call function with kwarg
   kwargs = {'name' : 'sabesan', 'age' : '33'}
   func_kwargs(**kwargs) 

   # Call func_while_exception, check the exception message is printed
   func_while_exception()
 
   # Induce a syntax error here :
   if 1==1:
      print "True"

   # Test print_braces
   print_braces()

   # Call check_IndexError
   check_IndexError()
