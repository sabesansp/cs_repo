import java.util.*;

public class Algorithms
{

   //SP : populate an array list of integers from an existing array
   ArrayList<Integer> populateArrayList(int[] a)
   {  
      ArrayList<Integer> arrayList = new ArrayList<Integer>();
      for(int i=0;i<a.length;i++)
      {
         arrayList.add(a[i]);
      }
      return arrayList;
   }



   //SP : return the maximum of two numbers
   int max(int a, int b)
   {
   
      return a>b ? a:b;
   
   } 


   //SP : find the maximum element in a list of integers
   int findMax(List<Integer> a)
   {
      int max = 0;
      if(a != null && a.size()>=1)
      {

         for(int i=0;i<a.size();i++)
         {
            if(a.get(i)>max)
               max = a.get(i);
         }
      }
      return max;
   }


   //SP : Check if index exists in the array list
   boolean indexExists(ArrayList<Integer> a,
                       int index)
   {
      return index>=0 && index<a.size();
   } 
                 



   // P2 : Method to compute the length of the longest increasing subsequence
   // input : a = [7,2,3,-1] l=[ ], i=3
   // f(a,l,i) = max(l(i-1), 1 + max() 
   void computeLengthOfLongestIncreasingSubsequence(ArrayList<Integer> a,
                                                   ArrayList<Integer> l, 
                                                   int i) 
   {
      if(i==0)
      {
         //set the value of l[i] to 1
         if(a != null && a.size()>=1)
         {
            l.set(0,1); 
         } 
      } 
      else if(i>0)
      {
         // example : how would you compute l[1]
         // compute all indices less than i such that
         // a(i)>a(j)
         if(l.get(i-1) == 0) 
            //recurse
            computeLengthOfLongestIncreasingSubsequence(a,l,i-1);
         
         List<Integer> indices = calculateMinIndices(a,i);
         printArray(indices);
         System.out.println("indices size = " +  indices.size());
         // call_1 : i=5 
         List<Integer> elements = new ArrayList<Integer>();
         for(int k : indices)
         {
            elements.add(l.get(k));
         }
         printArray(elements);
         System.out.println("find max = " + findMax(elements));
         int element = max(l.get(i-1),1 + findMax(elements));
         System.out.println("element = "+element);
         l.set(i,element);
         
      }
   }

  
   // SP :Method to print the contents of an array entirely
   void printArray(List<Integer> a)
   {
      for(int i=0;i<a.size();i++)
         System.out.print(a.get(i)+"\t");
      System.out.print("\n");
   }

   // SP : Method to print the contents of an array upto a certain point
   void printArray(List<Integer> a,
                   int point)
   {
   
       for(int i=0;i<=point;i++)
          System.out.print(a.get(i)+"\t");
       System.out.print("\n");
   }

   // P1 : Return a list of array indices that are less than a number
   //      at a specific index
   List<Integer> calculateMinIndices(List<Integer> a,
                                     int i)
   {
      
      List<Integer> o = new ArrayList<Integer>(); 
      // example : a = [5 -1 3 8 6 4] ; i = 3
      // output = o = [0 1 2] 
      // j = 0...i-1 => check if a[j] < a[i]
      // if preceding condition true => add element to 'o'
      for(int j=0;j<i;j++)
      {
      
         if(a.get(i) > a.get(j))
         {
            o.add(j);
         }
      } 
      return o;       
   }

   // P3 : Compute the common ancestor of two nodes in a binary tree 
   int commonAncestor(int[] a,int n1, int n2)
   {
      if(n1==n2)
         return n1;
      else if(n1>n2)
         return commonAncestor(a,(n1-1)/2,n2);
      else
         return commonAncestor(a,n1,(n2-1)/2);
   }


   // SP : swap two values at indices i and j in the array a
   void swap(int[] a,int i, int j)
   {
      int t = a[i];
      a[i] = a[j];
      a[j] = t;
   } 

  

   // SP : Choose pivot and partition the array
   int qsortPartition(int[] a, int l, int r)
   {
      int p = a[l]; 
      int i = l + 1;
      for(int j=i+1;j<=r;j++)
      {
         if(p>a[j])
         {
            swap(a,i,j);
            i++;
         }
      }
      swap(a,l,i-1);
      return i-1;
   } 


   // P4 : Routine to perform quick sort on array a
   void qsort(int[] a,int l,int r)
   {
   
      if(l<r) 
      {
         int p = qsortPartition(a,l,r);
         System.out.println("pivot position = "+p);
         //qsort(a,l,p-1);
         //qsort(a,p+1,r);
      }
   }   
    

  
   // code starts executing from here
   public static void main(String[] args)
   {
      Algorithms al = new Algorithms();
      // P1 : calculate minimum indices
      //ArrayList<Integer> array = al.populateArrayList(new int[]{5,-1,3,8,6,4});
      //al.printArray(al.calculateMinIndices(array,4));
      //ArrayList<Integer> ls = al.populateArrayList(new int[]{0,0,0,0,0,0});
      //al.computeLengthOfLongestIncreasingSubsequence(array,ls,5);
      //al.printArray(ls,5);
      // P3 : Common ancestor in a binary tree
      //int a[] = {1,2,3,4,5,6,7};
      //int index = al.commonAncestor(a,3,4);
      //System.out.println("The common ancestor = " +  a[index]);
      int a[] = {5,4,6,3,2,9,1};
      // The following code does not work
      al.qsort(a,0,6);
      al.printArray(al.populateArrayList(a));      
   }
}
