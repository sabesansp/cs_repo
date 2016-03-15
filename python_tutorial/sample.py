# This is a sample python file which can be used
# to teach programming to beginners in python

# Task1 : Adjust vim editor to make sure that each line does not exceed 90 characters,test

def main():

   print "Inside main function: make sure that this line extends 90 character limit"


# Task 2: Add a method to test validity of an ipv4 address
def is_valid_ipv4_addr(ip):

   octets = ip.split(".")
   if len(octets) != 4 :
      return False
   return all(0 <= int(octet) <= 255 for octet in octets)

if __name__ == '__main__':
   main()

   # Expected value = true
   print is_valid_ipv4_addr('10.4.66.239')

   # Expected value = false
   print is_valid_ipv4_addr('10.456.34.255')


