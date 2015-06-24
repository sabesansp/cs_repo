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
      
   

   // Display the matrix 
   public void displayMatrix(int[][] a, 
                             int r, 
                             int c)
   {
      for(int i=0;
          i<r;
          i++)
      {
         for(int j=0;
             j<c;
             j++)
         {
            System.out.print(a[i][j] + " ");
         }
         System.out.print("\n"); 
      }  
   } 


   // P6 : Display the edges of the matrix clockwise                    
   public void displayMatrixEdgeClockwise(int[][] a,
                                          int r,
                                          int c)
   {
      int i,j;
      for(i=0,j=0; j<(c-1); j++) System.out.print(a[i][j]+" ");
      for(;i<(r-1);i++) System.out.print(a[i][j]+ " ");
      for(;j>0;j--)System.out.print(a[i][j] + " ");
      for(;i>0;i--)System.out.print(a[i][j] + " ");
      System.out.print("\n");
   }


   // P7 : Copy one edge onto another edge in a nxn matrix at 90 degrees
   public void rotateMatrix(int[][] A,
                            int n) 
   {
      int[] t1 = copyColumnArray(A,n-1,n);
      int[] t2 = copyRowArray(A,n-1,n);
      int[] t3 = copyColumnArray(A,0,n);
      int i,j,k;
      // populate right edge
      for(i=0,j=n-1,k=n-1;
          k>=0;
          k--)
      {
         A[k][j] = A[i][k];
      }
      // populate the bottom edge
      for(i=n-1,k=0;
          k<n-1;
          k++)
      {
         A[i][k] = t1[n-2-k];
      }  
      // populate the left edge
      for(i=0,k=0;
          k<n-1;
          k++)
      {
       
         A[k][i] = t2[k];
      }
      printArray(populateArrayList(t3));
      // populate the top edge
      for(i=0,k=0;
          k<n-1;
          k++)
      {
         A[i][k] = t3[n-2-k];
      }         
   }   


   // SP : Copy contents of a specific column of a matrix into 
   //      an array and return the array
   public int[] copyColumnArray(int[][] A,
                          int j,
                          int n)
   {
      int[] t  = new int[n-1];
      for(int i=1;
          i<n;
          i++)
      {
         t[i-1] = A[i][j];
      }
      return t;
   }   
    
  
   // SP : Copy contents of a specific row of a matrix into 
   //      an array and return the array
   public int[] copyRowArray(int[][] A,
                          int j,
                          int n)
   {
      int[] t  = new int[n-1];
      for(int i=0;
          i<n-1;
          i++)
      {
         t[i] = A[j][i];
      }
      return t;
   }


   // SP : Build a sample graph for graph problems 
   public ArrayList<ArrayList<Integer>> buildGraph()
   {
      ArrayList<ArrayList<Integer>> graph = 
      new ArrayList<ArrayList<Integer>>();
      // first list
      ArrayList<Integer> l0 = new ArrayList<Integer>();
      l0.add(1);
      l0.add(3);
      graph.add(l0);
      // second list
      ArrayList<Integer> l1 = new ArrayList<Integer>();
      l1.add(4);
      graph.add(l1);
      // third list
      ArrayList<Integer> l2 = new ArrayList<Integer>();
      l2.add(4);
      l2.add(5);
      graph.add(l2);
      // fourth list
      ArrayList<Integer> l3 = new ArrayList<Integer>();
      l3.add(1);
      graph.add(l3);
      // fifth list
      ArrayList<Integer> l4 = new ArrayList<Integer>();
      l4.add(3);
      graph.add(l4);
      // sixth list
      ArrayList<Integer> l5 = new ArrayList<Integer>();
      l5.add(5);
      graph.add(l5);
      return graph;
   }   

   // SP: Print a graph
   public void printGraph(ArrayList<ArrayList<Integer>>
                          graph)
   {
      for(ArrayList<Integer> l : graph)
      {
         for(Integer i : l)
         {
            System.out.print(" " + i);
         }
         System.out.print("\n");
      }
   }     


   // SP : Check whether an element is found
   public boolean isElementFound(ArrayList<Integer> list,
                                 int n)
   {
      for(Integer i : list)
      {
         if(i==n)
         {
            return true;
         }
      }
      return false;
   } 


   public void callDfs()
   {

         Graph g = new Graph(new int[]{0,1,2,3,4,5}); 
         List<Graph.Node> nodeList = g.getNodes();
         // add an edge between 2->3 and 2->4
         List<Graph.Node> edgesList = new 
         ArrayList<Graph.Node>(); 
         edgesList.add(g.findNode(3));
         edgesList.add(g.findNode(4));
         Graph.Node currNode = g.findNode(2);
         currNode.addEdge(edgesList);
         // 0->1
         edgesList = new ArrayList<Graph.Node>();
         edgesList.add(g.findNode(1));
         currNode = g.findNode(0);
         currNode.addEdge(edgesList);
         // 1->2
         //edgesList = new ArrayList<Graph.Node>();
         //edgesList.add(g.findNode(2));
         //currNode = g.findNode(1);
         //currNode.addEdge(edgesList);
         // 3->0
         edgesList = new ArrayList<Graph.Node>();
         edgesList.add(g.findNode(0));
         currNode = g.findNode(3);
         currNode.addEdge(edgesList);
         // 4->5
         edgesList = new ArrayList<Graph.Node>();
         edgesList.add(g.findNode(5));
         currNode = g.findNode(4);
         currNode.addEdge(edgesList);
         // display graph
         g.displayGraph();
         // call isRoute
         List<Integer> l = new ArrayList<Integer>();
         g.dfs(l,0,4);
         printArray(l);

   } 



   // P : Print all permutations of a string represented as a character 
   // array
   public void permute(char[] A, 
                       int start, 
                       int end)
   {
      if(start == end)
      {
         // display all the characters 
         for(int j=0;j<=end;j++) 
            System.out.print(A[j]);
         System.out.print("\n");
      }
      else 
      {
         if(start < end)
         {
            for(int i=start;i<=end;i++)
            {
               swapCharArray(A,i,start);
               permute(A,start+1,end);
               swapCharArray(A,i,start);
            }
         }
      }
   }    



   // P : combination of indices of number "l"
   public void combineIndex(char[] A,
                            int l) 
   { 
      if(l>0) 
      {
         if(l == A.length)
         {
            printCharArray(A);
         } 
         else
         {
            for(int i=0;i<A.length;i++)
            {
               for(int j=i,k=1;k<=l;k++,j++)
               {
                  if(j==A.length) j=0;
                  System.out.print(A[j]);
               }
               System.out.print("\n");
            } 
         }
         combineIndex(A,l-1);
      }
   }
 


   // P : Count the number of occurrences of pattern "P" in "T"
   public int naiveStringMatch(char[] T,
                               char[] P)
   {
      int c = 0;
      for(int i=0,j=0,start=i;
          i < T.length;
          i++,j++)
      {
         // if 'j' reaches the end of the array, please
         // loop it from the start of 'P'
         if(j>P.length-1)
            j=0;
         if(T[i] == P[j])
         {
            if(j == P.length-1)
            {
               c++;
               j=0;
            }
         }
         else 
         {
            i = start+1;
            start = i;
            j=0;
         } 
      }
      return c; 
   } 
            

   // P : implement radix sort
   public void radixSort(int[] A)
   {

      // compute the max number of digits in A
      int d = maxDigits(A);

      for(int k=d;
          k>=1;
          k--)
      {
         // sort A according to "extractDigits" routine
         for(int i =0;
             i<A.length;
             i++)
         {
            for(int j=i+1;
                j<A.length-1;
                j++)
            {
               int d1 = extractDigits(A[i],k);
               int d2 = extractDigits(A[j],k);
               System.out.print(d1 + " " + d2 + "\n");
               if(d1>d2)
               {
                  swap(A,i,j);
                  dispArray(A);
               }
            }
         }
      } 
   }  
          

   // P : display the entire integer array
   public void dispArray(int[] A)
   {
      for(int a : A) {System.out.print(a + " ");}
      System.out.print("\n");
   } 


   // P : Count the number of digits in x
   public int countDigits(int x)
   {
   
      x = Math.abs(x); 
      int c=0;
      if(x==0)
      {
         c=1;
      } 
      else
      {
         while(x>0)
         {
            x=x/10;
            //System.out.println("The abs value of x = " + x);   
            c++;
         }
      }
      return c;
   } 

   // P: extract the digits in the specified place
   public int extractDigits(int x,
                            int y)
   {
   
      int n = countDigits(x);
      int[] dArray = new int[n];
      int k=n-1;
      while(x != 0 &&
            k>=0)
      {
         dArray[k] = x%10;
         x = x/10;
         k--;
      }
      // take care of test cases like y = {0,-1,>n etc...}
      return dArray[y-1];
   } 


   // P : Count the maximum number of digits in an array
   public int maxDigits(int[] A)
   {
      int max = 0;
      for(int a : A)
      {  
         // count the number of digits
         int d = countDigits(a);      

         if(d>max) max = d;
      }
      return max;
   } 
 

   // P : Max-heapify a tree
   public void maxHeapify(int[] A,
                          int i,
                          int heapSize)
   {
      int largest=i;
      if(i>=0 && i<A.length)
      {
         int left = 2*i+1;
         int right = 2*i+2;
         if(left < A.length &&
            left <= heapSize)
         {
            if(A[left]>A[largest])
               largest = left;
         } 
         if(right < A.length &&
            right <= heapSize)
         {
            if(A[right]>A[largest])
               largest = right;
         }
         if(largest != i)
         {
            swap(A,i,largest);
            System.out.println("Max-heapify i : " + i);
            dispArray(A); 
            maxHeapify(A,largest,heapSize);
         }
      }
   }    


   // P : Build a max heap given the heap size
   public void buildMaxHeap(int[] A,
                            int heapSize)
   {
      if(heapSize>=0 &&
         heapSize<A.length)
      {
         int p = (heapSize + 1)/2;
         for(int i=p;
             i>=0;
             i--)
         {
            maxHeapify(A,i,heapSize);
         }
      }
   }
 

   // P : sort an array of elements using heap sort
   public void heapSort(int[] A)
   {
      for(int i=A.length-1;
          i>=1;
          i--)
      {
         buildMaxHeap(A,i);
         System.out.println("Max heap : ");
         dispArray(A);
         swap(A,0,i);
         System.out.println("After swap : ");
         dispArray(A);
      }
   }


   // P : compute the maximum sub array sum
   public int computeMaxSubArraySum(int[] A)
   {
      int sum=A[0], maxSum=sum, start=0, end=0;
      // loop through array
      for(int i=1;
          i<A.length;
          i++)
      {
         if(A[i]>sum && 
            A[i]>maxSum &&
            sum+A[i] < A[i])
         {
            start=i;
            sum=A[i];
         }
         else
            sum+=A[i];
         if(sum>maxSum)
         {
            maxSum=sum;
            end=i;
         }
      }
      System.out.println("Start = " + start + 
                         "\t End  = "+ end);
      return maxSum;
   }

   
   public String concatenateStr(String src,
                                String dest)
   {
      String[] srcList = src.split(" ");
      String[] destList = dest.split(" ");
      if(srcList != null && srcList.length > 0 &&
         destList != null && destList.length > 1 && 
         srcList[0].equals(destList[1]))
      {
         return dest+" "+src;
      } 
      else 
      if(destList != null && destList.length>0 &&
         srcList != null && srcList.length>1 &&
         destList[0].equals(srcList[1]))
      {
         return src+" "+dest;
      }
      else
      {
         return null;
      } 
   }


   public String getRoute(List<String> l)
   {
      while(l.size()>1)
      {
         for(int i=0;
             i<l.size()-1;
             i++)
         {
            for(int j=i+1;
                j<l.size();j++)
            {
               String str = concatenateStr(l.get(i),
                                           l.get(j));
               if(str != null)
               {
                  l.set(i,str);
                  l.remove(j);
                  j--;
               }
            }
         }
      }
      return l.get(0);
   }
    
               
       


   public void readInputString()
   {
      try{
         BufferedReader br = 
               new BufferedReader(
                      new InputStreamReader(System.in));
         List<String> strList = new ArrayList<String>();
         String input = null;
         do{
         
            // Enter null to terminate the prompt for list of pairs
            System.out.print("Enter the list of pairs: ");
            input = br.readLine();
            System.out.print("\n");
            if(!input.equals("null"))
               strList.add(input);                   
     
         }while(input != null && 
                !input.equals("null")); 
         String route = getRoute(strList);
         strList = new ArrayList<String>();
         String[] graphArray = route.split(" ");
         for(int i=0;i<graphArray.length;i+=2)
         {
            strList.add(graphArray[i]+" "+graphArray[i+1]);
         } 
         // Display the final array list
         for(String s : strList)
         {
            System.out.println(s);
         }
      } catch(IOException e){
         e.printStackTrace();
      }
   }


   public int[] mergeArrays(int[] A, int[] B, int[] C) {

      // A = <0,2,4,6>
      // B = <-1,7,9,25,98>
      // C = <100,215>
      // i=0, j=0 0>-1, copy B[j] into O[index] 
   
      int i,j,k;

      int[] O = new int[A.length + B.length];
      int[] output = new int[O.length + C.length];
      int index = 0;

      // Iterate through the A and B array

      for( i=0,j=0; i<A.length && j<B.length;) {

         if(A[i] < B[j]) {O[index++] = A[i++];} 

         else {O[index++] = B[j++];}

      }

      if(i < A.length) {while(i<A.length) {O[index++] = A[i++];}}
      if(j < B.length) {while(j<B.length) {O[index++] = B[j++];}}

      // Array O = sorted merge output of A & B

      int m;
      int n=0; 
      for(m=0,k=0;k<C.length && m<O.length;) {

         // Iterate through O array and C array
 
         if(O[m] < C[k]) { output[n++] = O[m++]; }
         else { output[n++] = C[k++]; }

      }

      if(m<O.length) { while(m<O.length) { output[n++] = O[m++];}}
      if(k<C.length) { while(k<C.length) { output[n++] = C[k++];}}
      
      return output;
      
     

   }

   public List<String> readStringFromIn() 
      throws Exception {

      BufferedReader br = new BufferedReader(
                          new InputStreamReader(
                          System.in));
      List<String> strList = new ArrayList<String>();
      String line = null;
      System.out.print("Enter the (src:dest) : ");
      line = br.readLine();
      while(!line.equals("")) {
         System.out.println(line);
         strList.add(line);
         System.out.print("\n");
         System.out.print("Enter the (src:dest) : ");
         
         line = br.readLine();
      }
      return strList;
   }       
   


   public void getRoute() 
      throws Exception {

      // Read the string from keyboard

      List<String> strList = readStringFromIn();

      // Collection of hashmaps

      Map<String,Integer> exSrcMap = new HashMap<String,Integer>();

      Map<String,Integer> exDestMap = new HashMap<String,Integer>();

      Map<String,Integer> srcDestMap = new HashMap<String,Integer>();

      // Loop through the list of strings

      for(String s : strList) {

         // split the string based on ":"

         String[] parts = s.split(":");
     
         //
      }    

   }


   public void rotateArray(int[] A, int k) {

      for(int i=1; i<=k; ++i) {
         int temp1 = A[0];
         int temp2 = A[0];
         for(int j=1; j<A.length; ++j) {
            temp2 = A[j];
            A[j] = temp1;
            temp1 = temp2;
         }
         A[0] = temp1;
      }
      printArray(populateArrayList(A));
   }

  

   // code starts executing from here
   public static void main(String[] args)
   {
      Algorithms al = new Algorithms();
      try{
         int a[] = {5,1,0,2,4,6};
         al.rotateArray(a,2);
         //al.getRoute();          
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
         //char[] a = new char[]{'i',' ','a','m',' ','a',' ','y','o','g','i'}; 
         //al.reverseWordsInSentence(a);
         //al.printCharArray(a);
         //al.displayHashMap(al.countOccurrences(a));
         //int[][] a = new int[5][5];
         //a[0] = new int[]{2,3,7,9,11};
         //a[1] = new int[]{0,1,2,0,5};
         //a[2] = new int[]{6,2,1,5,6};
         //a[3] = new int[]{4,3,1,0,2};
         //a[4] = new int[]{1,1,3,5,6}; 
         //al.displayMatrixEdgeClockwise(a,3,3); 
         //System.out.println("input :\n");           
         //al.displayMatrix(a,5,5);
         //al.rotateMatrix(a,5);
         //al.displayMatrix(a,5,5); 
         //System.out.println("output :\n");           
         //al.displayMatrix(a,5,5);
         //int[] temp = al.copyRowArray(a,4,5);
         //al.printArray(al.populateArrayList(temp)); 
         //ArrayList<ArrayList<Integer>> graph = al.buildGraph(); 
         //al.printGraph(graph); 
         //System.out.println("Is there a route (0->5) ?" +  
                            //al.isRoute(graph,0,5));
         //char[] A = new char[]{'a','b','c','d'};
         //al.permute(A,0,1);
         //al.combineIndex(A,4);
         //LList<Integer> head = new LList<Integer>();
         // data insertion
         //head.insertData(5);
         //head.insertData(6);
         //head.insertData(7);
         // data deletion
         //head.deleteData(5); 
         //char[] T = new char[]{'a','a','a','a','a'};
         //char[] P = new char[]{'a'};
         //System.out.println("Count of number of occurrences : " + 
                            //al.naiveStringMatch(T,P));
         
         //int x = 845670909;
         //int y = 8;
         //System.out.println("The number of digits in " 
                            //+  x  + " : " + 
                            //al.countDigits(x));
         //System.out.println("The digit extracted " + y +
                            //" : " + al.extractDigits(x,y));
         // this code does not work, need to debug 
         //int[] a = new int[]{6,8,0,2,4,21,2,21,874};
         //System.out.println("Original array : ");
         //al.dispArray(a);
         //al.heapSort(a);
         //System.out.println("Sorted array : ");
         //al.dispArray(a);
         //al.dispArray(a);
         //int[] a = new int[]{1,-2,3,-10,-4,7,5};
         //int sum = al.computeMaxSubArraySum(a);
         //System.out.println("Max sum = " + sum);
         //al.readInputString();         
         //al.dispArray(al.mergeArrays(new int[]{0,2,4,6},
                        //new int[]{-1,7,9,25,98},
                        //new int[]{100,215}));
 
      } 
      catch(Exception e)
      {
         e.printStackTrace();
      }           
   }
}

