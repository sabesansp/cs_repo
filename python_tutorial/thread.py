import thread


def func(threadName):

   print "%s" %(threadName)


def main():

   try:

      thread.start_new_thread(func("t1"))
      thread.start_new_thread(func("t2"))

   except:

      print "Unable to start thread"



if __name__ == '__main__':
   main()
