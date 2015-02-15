## How much time does it take to load a list of 10000 integers ? 
## [using an intel i3 processor(3.2Ghz) with 4GB RAM]


from random import randint
from time import time


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



## Display the list of integers

def display(int_list) :

   for i in range(0,len(int_list)) :

      print int_list[i]



## Load the dataset from the "file_path"

def load_dataset(file_path) :

   # open the file in read mode

   f = open(file_path,'r')

   # read lines from file
 
   lines = f.read().splitlines()

   int_list = []

   # Iterate through lines 

   for line in lines :

      int_list.append(int(line))


   f.close()

   return int_list


## Method to measure the time elapsed
## for a certain function 'f'

def measure_time(func,data) :

   start_time = time()
   func(data)
   stop_time = time()  
   elapsed_time = stop_time - start_time
   return elapsed_time



## Method to perform insertion sort 
## on an array of integers

def insertion_sort(int_list) :

   for j in range(1,len(int_list)):
      key = int_list[j]
      i = j-1
      while (i>=0 and key<int_list[i]) :
         int_list[i+1] = int_list[i]
         i = i-1  
      int_list[i+1] = key



def addBinaryDigits(A,B) :

   sum = 0
   carry = 0
   if(len(A) != len(B)):
      raise invalid_input
   k=len(A) -1
   C = [0] * (k+2)
   while k>=0 :
      sum = A[k] + B[k] + carry
      if(sum == 2) :
         sum = 0
         carry = 1
      if(sum == 3) :
         sum = 1
         carry = 1
      C[k+1] = sum 
      k = k-1
   C[0] = carry
   return C


      
      

## Actual entry point of the program

if __name__ == '__main__' :

   # "data.txt" file exists in the current working directory
   # created through create_dataset api

   #int_list = load_dataset('data.txt')

   #t_insertion_sort = measure_time(insertion_sort,int_list)
  
   #display(int_list)

   #print "time_insertion_sort = ",t_insertion_sort

   A = [1,1,1,0,1,0,1,1,1]
    
   B = [1,1,0,1,0,1,1,0,1]

   C = addBinaryDigits(A,B)
 
   display(C)
