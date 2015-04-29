def test_pydict(dict) :

   if hasattr(dict,'id') :
      print "id is the attribute in dict\n"
   else :
      print "id is not an attribute in dict"




if __name__ == "__main__":
   print "Inside main \n"
   dict = {'id' : '1','s' : '0'}
   test_pydict(dict)
