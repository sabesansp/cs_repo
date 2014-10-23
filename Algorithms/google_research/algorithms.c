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


	
// entry point of code execution
int main()
{
   write_billion("/Volumes/My Passport/data/billion.txt");
   return 0;
}

