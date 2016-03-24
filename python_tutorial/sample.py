# This is a sample python file which can be used
# to teach programming to beginners in python


from multiprocessing import Process
import sys
import traceback
import urllib2
import requests
import re


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
      
      

# Task 9 : Split a string based on '-'
def split(nos_version):

   list = nos_version.split('-')
   if list[2] == 'danube' :
      list[2] = list[2] + '-' + list[3] + '-' + list[4]
      del list[3]
      del list[3]
      print list
   

# Task 10 : understand the lambda function
def lambda_func():

   if filter(lambda x: x is None, [2, 3]):
      print "T10 : None lambda function result"
   else:
      print "T10 : valid lambda function result"     


# Task 11 : Get all executable names in the cores
def save_nos_build_links(cores_map):
  
   executables_list = ['name1'] 
   # Assume core_map had "name : <value>" 
   for name, core_map in cores_map.items():
      for n in core_map.keys():
         if n not in executables_list:
            executables_list.append(n)
 
   # print the executables list here
   print "T11 : ", executables_list


# Task 12 : Form the complete url from base url
def form_url(branch, commit, build_type):

   base_url = 'http://earth.corp.nutanix.com/builds/nos-builds/'
   url = base_url + branch + '/' + commit + '/' + build_type
   return url   


# Task 13 : Split the release version based on '-'
def split_version(nos_version):

   clist = nos_version.split('-')
   b_type = clist[1]
   print "T13 : build type = ",b_type
   size = len(clist)
   commit = clist[size-1]
   print "T13 : commit = ",commit
   if 'danube' in nos_version:
      branch = clist[2]
      for i in range(3,size-1):
         branch = branch + '-' + clist[i]
   else:
      branch = clist[2]
   print "T13 : branch = ",branch       


# Task 17 : Write contents of url to a file
def print_link_contents(url):

   tar_url_list = []
   dbg_url_list = []
   exec_name_list = ['stargate','curator']
   urlpath = urllib2.urlopen(url+'/tar')
   response = urlpath.read()
   str_list = response.split('HREF=')
   file = None
   for str in str_list:
      file_list = re.findall(r'(nutanix_installer.+\.tar\.gz)\">',str)
      if file_list:
         file = file_list[0]
         break
   # "file" contains the actual link
   new_url = url + '/tar/' + file
   if new_url not in tar_url_list:
      tar_url_list.append(new_url)
   
   # Proceed in a similar fashion for the debug symbols list
   try :
      dbg_url = url + '/debug_symbols'
      urlpath = urllib2.urlopen(dbg_url)
      response = urlpath.read()
      for exec_name in exec_name_list:
         newurl = dbg_url+ '/'
         regex = re.escape(exec_name)+".dbg.gz"
         s = re.findall(regex, response)
         if s :
            newurl = newurl+ s[0]
            if newurl not in dbg_url_list:
               dbg_url_list.append(newurl)
         else :
            print "No valid link found for executable name %s" % exec_name

   except urllib2.HTTPError as e:
      print "no debug_symbols directory found in the builds directory"        
         

   # Write to file
   with open('nos_build_links.txt','w') as fh:
      if tar_url_list:
         fh.write("tar link : \n")
         for u in tar_url_list:
            fh.write(u + "\n")
         fh.write("\n\n")
      if dbg_url_list:
         fh.write("debug symbols link : \n")
         for k in dbg_url_list:
            fh.write(k + "\n")
   fh.close()


if __name__ == '__main__':



   print_link_contents('http://earth.corp.nutanix.com/builds/nos-builds/danube-4.5.3-stable/04e3f85e9d43e0b7147d383552fc07e1f3bf5b41/release') 

   # Call form_url with relevant parameters
   url = form_url('master', '000d79ddd02d0e2f93cb3f38ee991bce0c396276', 'opt')

   # Call split_version
   split_version('el6-opt-danube-4.5.3-stable-af72c6727333445115e2ec844d4cb246ffe6a010')   

   # Call url formed above and list all the files in that path
   r = requests.get(url)
   #print "T14 : ",r.content  

   # create core_map here
   cores_map = {}
   core_map = {}
   core_map['name1'] = 'sabesan'
   core_map['name2'] = 'jag'
   cores_map['exec_1'] = core_map
   save_nos_build_links(cores_map)


   # Call lambda function
   lambda_func()

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

   # Split a string based on '-'
   split('el6-opt-danube-4.5.3-stable-af72c6727333445115e2ec844d4cb246ffe6a010')
 
