// All libraries to be included here 
# include<stdio.h>
# include<stdlib.h>



// P1 : Write a billion (10^9) numbers into a file
void write_billion(char *file_name)
{
   FILE* fp;
   
   fp = fopen(file_name,"w");
   // execute the for loop a billion times
   for(int i=1;i<=1000000000;i++) 
   {
      fprintf(fp,"%d\n",i);
   }
   fclose(fp);
}


// SP : returns the maximum element in "cost" which is less than "sum"
// make sure that "cost" is in a sorted order
int compute_max_element_less_than_element(int sum, int* cost, int n)
{
   // perform a binary search here
   // design issue : how do you know where to stop in the set of elements
   // that cost points to 
   int i = 0, left = 0, right = n-1;
   
}      



// P2 : dynamic programming problem
int compute_min_number_of_coins(int sum,int* cost, int n)
{
   if(sum == 0) 
      return 0;
   else 
      return 1 + compute_min(

}
	
// entry point of code execution
int main()
{
   write_billion("/Volumes/My Passport/data/billion.txt");
   return 0;
}

