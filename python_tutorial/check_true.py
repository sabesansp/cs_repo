def isTrue(x):

   if x==0:
      return True
   else:
      return False


def main():

   if not isTrue(10):
      print "Unable to get a valid ipv4 address\
            yes"
   else:
      print "10 is false"

if __name__ == "__main__":
   main()
