// All libraries to be included here 
# include<stdio.h>
# include<stdlib.h>



// P1 : Write a billion (10^9) numbers into a file
// This operation took approximately 5 mins
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


// SP : returns the maximum element in "a" which is less than "s"
// make sure that "a" is in a sorted order
int compute_max_element_less_than_element(int s, int* a, int l,int r,int n)
{
   // compute mid-point 'm'
   int m = (l+r)/2;
   
   if(a[m]<=s)
   {
      if(m==(n-1) || a[m+1]>s) 
         return a[m];
      if(m<(n-1))
      {
         if(a[m+1]<=s)
         {
            return compute_max_element_less_than_element(s,a,m+1,r,n);
         }
      }
   } else 
   {
      if(m>0)
      {
         return compute_max_element_less_than_element(s,a,l,m+1,n);
      }
   }   
}      



// P2 : dynamic programming problem
int compute_min(int s,int* a, int n)
{
   if(s == 0) 
      return 0;
   else 
      return 1 + compute_min(s - compute_max_element_less_than_element(s,a,0,n-1,n),a,n);

}
	
// entry point of code execution
int main()
{
   //write_billion("/Volumes/My Passport/data/billion.txt");
   int a[] = {5,9,10,11,13,15};
   printf("%d",compute_max_element_less_than_element(12,a,0,5,6));
   return 0;
}

