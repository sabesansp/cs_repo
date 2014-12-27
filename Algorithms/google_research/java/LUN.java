import java.io.*;
import java.util.*;


public class LUN
{


   /*
    * This method gets a list of integers and 
    * prints the lowest unique number to console
    */
   public String getWinner(List<Integer> list)
      throws Exception
   {
      if(list == null || 
         list.isEmpty())
      {
         throw new Exception("Empty_List");
      }
      if(list.size()>20)
      {
         throw new Exception("Max_Players_Exceeded_20");
      }
      Integer min = list.get(0);
      Integer winner = 1;
      for(int i=1;
          i<list.size();
          i++
         )
      {
         Integer num = list.get(i);
         if(num<min)
         {
            min = num;;            
            winner = i+1;
         }
         else
         {
            if(num==min)
            {
               winner = 0;
            }
         }
      }
      return String.valueOf(winner);
   }
   
   public void readFile(String path)
      throws Exception
   {
      File file = new File(path);
      String output = new String("output.txt");
      File outputFile = new File(output);
      if(file.createNewFile())
      {
         System.out.println("Created the output file : " + outputFile);
      }
      BufferedReader br = new BufferedReader(
                             new FileReader(file));
      
      PrintWriter out = new PrintWriter(new BufferedWriter(
                        new FileWriter(outputFile)));
      String line = null;
      List<Integer> intList = null;
      while((line = br.readLine()) != null)
      {
         intList = new ArrayList<Integer>();
         String[] strArray = line.split(" ");
         for(String s : strArray)
         {
            intList.add(Integer.parseInt(s));      
         } 
         String winner = getWinner(intList);
         out.println(winner);
      }
      out.close();
      br.close();
      br = new BufferedReader(new 
           FileReader(outputFile));
      System.out.println("The output from "+
                         outputFile + " : ");
      while((line = br.readLine()) != null)
      {
         System.out.println(line);
      }
      br.close();
   }



   public static void main(String[] args)
   {
      LUN lun = new LUN();
      try
      {
         // read the file from prog arg
         lun.readFile(args[0]);
      }
      catch(Exception e)
      {
         e.printStackTrace();
      }
   }

}
