import java.util.*;
import java.io.*;
import java.math.*;

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


   // SP : compute the median index of three elements
   int computeMedianIndex(int[] a, int l, int r)
   {
      int m = (l+r)/2;
      // l=0, r=4, m=2
      // a[l]=5, a[r]=5, a[m]=2
      // median_index=2
      int median_index = m;
      // 2>5 => no
      if(a[m] > a[l])
      {
         if(a[m] > a[r]) 
         {
            median_index = (a[l] < a[r]) ? r : l;          
         } 
         else if(a[m] == a[r]) 
         {
            median_index = l;
         }  
      } 
      else if(a[m] == a[l])
      {
         if(a[m] > a[r]) 
            median_index = r;
      } 
      else
      {
         // 2<5 
         if(a[m] < a[r]) 
         { 
            if(a[l] != a[r]) 
               median_index = (a[l] > a[r]) ? r : l;
         }
      }
      return median_index;
   }  
       
  

   // SP : Choose pivot and partition the array
   int qsortPartition(int[] a, int l, int r)
   {
      // a = {5,4,6,3,2,9,1}
      // l = 0, r = 6
      // p = a[0] = 5
      // i = 1
      // choose the final element as the pivot
      // choose the median element of the three
      
      int p = a[l]; 
      int i = l + 1;
      //System.out.println("The value of i at init time : " + i);
      for(int j=l+1;j<=r;j++)
      {
         // 5>4 => swap(a,1,2) => {5,6,4,3,2,9,1}, i=2,j=3
         // 5>3 => swap(a,2,3) => {5,6,3,4,2,9,1}, i=3,j=4
         // 5>2 => swap(a,3,4) => {5,6,3,2,4,9,1}, i=4,j=5
         // 5<9 => {5,6,3,2,4,9,1},i=4,j=6
         // 5>1 => swap(a,4,6) => {5,6,3,2,1,9,4}, i=5,j=7
         if(p>a[j])
         {
            swap(a,i,j);
            i++;
         }
         //printArray(populateArrayList(a));
      }
      // swap(a,0,4) => {1,6,3,2,5}
      swap(a,l,i-1);
      //System.out.println("The value of i before return : " + i);
      return i-1;
   } 


   // P4 : Routine to perform quick sort on array a
   int qsort(int[] a,int l,int r)
   {
      if(l<r) 
      { 
         int median_index = computeMedianIndex(a,l,r);
         swap(a,l,median_index);
         int p = qsortPartition(a,l,r);
         //System.out.println("The value of l = "+l);
         //System.out.println("The value of r = "+r);
         //System.out.println("The value of p = "+p);
         return (r-l) + qsort(a,l,p-1) + qsort(a,p+1,r);
      }
      return 0;
   }   
    

   // 0 < alpha < 0.5
   // suppose alpha = 0.2
   // n=10
   // what is the probability that the size of the smaller subarray >= alpha times the size of the original array ?
   // probability of choosing a random element = 1/10 {1/n} 
   // size of smaller subarray >= 0.2*10 = 2
   // P(choosing pivot element such that size of smaller subarray>=2} = 1 - P(size<2) = 1- 1/n



   // SP : Read integers from a given file in the programming assignment
   List<Integer> readFile(String fileName)
      throws Exception
   {
      FileReader file = new FileReader(fileName);
      List<Integer> scores = new ArrayList<Integer>();
      Scanner sc = new Scanner(file);
      while(sc.hasNextInt())
      {
         scores.add(sc.nextInt());
      }
      return scores;
   } 


   //SP : Turn a list of integers into an array of ints
   int[] toIntArray(List<Integer> list)
   {
      int[] ret = new int[list.size()];
      int i=0;
      for(Integer e:list)
      {
         ret[i++] = e.intValue();
      } 
      return ret;
   }  


   // SP : Swap the elements in the character array
   public void swapCharArray(char[] a, int i, int j)
   {
      char temp = a[i];
      a[i] = a[j];
      a[j] = temp;
   }        

   // SP : Reverse an entire character array
   public void reverse(char[] a,
                       int start,
                       int end)
   {
      for( int i=start,j=end;
           i<j;
           i++,j--
         )
      {
         swapCharArray(a,i,j);
      }
   } 


   //SP : Print all elements in the character array
   public void printCharArray(char[] a)
   {
      for(int i=0;
          i<a.length;
          i++
         )
      {
         System.out.print(a[i]);
      }
      System.out.print("\n");
   }

   // P4: Reverse the words in a sentence
   public void reverseWordsInSentence(char[] a)
   {
      // reverse the entire array
      reverse(a,0,a.length-1);   

      // reverse the character array upto the space
      for(int i=0,start=i;
          i<a.length-1;
          i++
         ) 
      {
         if(a[i] == ' ' && 
            i>0 &&
            a[i-1] != ' '
           )
         {
            reverse(a,start,i-1);
            start = i+1;
         }
      } 
   } 
             
      
   // SP : Print the entire hash map                      
   public void displayHashMap(Map<Character,Integer> map)
   {
      // Iterate through the hash map and print the key and the value
      for(Map.Entry<Character,Integer> entry : 
          map.entrySet()
         )
      {
         System.out.println(entry.getKey() + 
                            " : " + 
                            entry.getValue());
      }
   }

   // P5 : Count the number of occurrences for characters in the array 'a'
   public Map<Character,Integer> 
          countOccurrences(char[] a)
   {
      // Create the hash map
      Map<Character,Integer> map = new HashMap<Character,Integer>();
      
      // Scan the array 
      for(int i=0;
          i<a.length;
          i++
         )
      {
         // ignore spaces
         if(a[i] == ' ') 
            continue;

         // if map contains the key, increment the count
         // else insert '1' as the value
         if(map.containsKey(a[i]))
         {
            Integer count = map.get(a[i]);
            map.put(a[i],count + 1);
         } 
         else 
         {
            map.put(a[i],1);
         }
      }
      
      // return map
      return map;
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
      //int a[] = {5,4,6,3,2,9,1};
      // The following code does not work
      //al.qsort(a,0,6);
      //al.swap(a,0,2);
      //al.printArray(al.populateArrayList(a));
      try{
         //List<Integer> input = al.readFile("QuickSort.txt");
         //al.printArray(input);
         //int a[] = al.toIntArray(input); 
         //int a[] = {1,4,2,3,5};
         //al.qsort(a,0,4,0);
         //System.out.println("first element = " + a[0]);
         //System.out.println("middle element = " + a[4999]);
         //System.out.println("last element = " + a[9999]);
         //System.out.println("median index = " + al.computeMedianIndex(new int[]{5,1,2,3,5},0,4)); 
         //System.out.println("number of comparisons = " + al.qsort(a,0,input.size()-1));
         char[] a = new char[]{'i',' ','a','m',' ','a',' ','y','o','g','i'}; 
         //al.reverseWordsInSentence(a);
         //al.printCharArray(a);
         al.displayHashMap(al.countOccurrences(a));
         
      } 
      catch(Exception e)
      {
         e.printStackTrace();
      }           
   }
}

