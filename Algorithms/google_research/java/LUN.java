import java.io.*;
import java.util.*;


public class LUN
{

   
   public void readFile(String path)
      throws IOException
   {
      File file = new File(path);
      BufferedReader br = new BufferedReader(
                             new FileReader(file));
      String line = null;
      List<Integer> intList = new ArrayList<Integer>();
      while((line = br.readLine()) != null)
      {
         String[] strArray = line.split(" ");
         for(String s : strArray)
         {
            intList.add(Integer.parseInt(s));      
         } 
         for(Integer i : intList)
         {
            System.out.print(i + " ");
         }
         System.out.print("\n");
      }
   }



   public static void main(String[] args)
   {
      LUN lun = new LUN();
      try
      {
         // read the file from prog arg
         lun.readFile(args[0]);
      }
      catch(IOException e)
      {
         e.printStackTrace();
      }
   }

}
