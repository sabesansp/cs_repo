## How much time does it take to load a list of 10000 integers ? 
## [using an intel i3 processor(3.2Ghz) with 4GB RAM]


from random import randint


## Method to create a dataset of "num_int" integers
## and store them in a file

def create_dataset(num_int,file_path):

   # open a file in write mode
   
   f = open(file_path,'w')

   # write "num_int" random integers into file

   for i in range(1,num_int+1):

      s = randint(1,num_int)
      f.write(str(s))
      f.write("\n")

   f.close()






if __name__ == '__main__' :

   # "data.txt" file exists in the current working directory
   # created through create_dataset api

  
  
