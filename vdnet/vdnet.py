import optparse
import sys


def test_pydict(dict) :

   if hasattr(dict,'id') :
      print "id is the attribute in dict\n"
   else :
      print "id is not an attribute in dict"




if __name__ == "__main__":
   print "Inside main \n"
   #dict = {'id' : '1','s' : '0'}
   #test_pydict(dict)
   args = sys.argv[1:]
   usage = "usage: %prog [options]"
   parser = optparse.OptionParser(usage=usage)
   parser.add_option("--config",dest="config",action="store",type="string",help="json_config")
   (cmdOptions,args) = parser.parse_args(args)
   print "cmdOptions.config : ",cmdOptions.config
   
