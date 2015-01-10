
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;


public class Main {

	
	
	class StringCount {

		
		private String str;
		private Integer count;
		private Integer beauty;
		
		
		// getters
		public Integer getCount(){
			return this.count;
		}
		
		public Integer getBeauty(){
			return this.beauty;
		}
		
		public String getStr(){
			return this.str;
		}
		
		
		// setters
		public void setStr(String str){
			this.str = str;
		}
		
		public void setCount(Integer count){
			this.count = count;
		}

		public void setBeauty(Integer beauty){
			this.beauty = beauty;
		}
	
	}
	
	
	public boolean isCharacterLetter(Character c)
	   throws Exception{
		
		// condn : c = null ? => yes =>
		// Null_Character
		
		if(c == null){
			throw new 
			Exception("Null_Character");
		}
		
		// compute the code for the character
		
		int code = (int)c.charValue();
		if((code >= 65 && code <= 90) ||
		   (code >= 97 && code <= 122)){
			return true;
		} else {
			return false;
		}
	}
	
	public boolean findString(List<StringCount> list, String str)
			throws IllegalArgumentException {

		// Check validity of input parameters

		if (list == null || str == null) {
			throw new IllegalArgumentException("Invalid input");
		}

		// compute the lowercase of string

		str = str.toLowerCase();

		// search list for string

		for (StringCount obj : list) {

			String val = obj.getStr();
			if (val.equals(str)) {
				return true;
			}
		}
		return false;
	}

	public void insertString(List<StringCount> list, String str)
			throws IllegalArgumentException {

		// check validity of parameters in method

		if (list == null || str == null) {
			throw new IllegalArgumentException("Invalid input");
		}

		// insert str in list if str is not found

		str = str.toLowerCase();

		if (!findString(list, str)) {

			StringCount strCount = new StringCount();
			strCount.setStr(str);
			strCount.setCount(1);
			list.add(strCount);
		} else {

			for (StringCount obj : list) {
				String val = obj.getStr();
				if (val.equals(str)) {
					int c = obj.getCount();
					c = c + 1;
					obj.setCount(c);
					break;
				}
			}
		}
	}

	public void display(List<StringCount> list) {
		for (StringCount l : list) {
			System.out.print("String = " + l.getStr() + " ");
			System.out.print("Count = " + l.getCount());
			System.out.print("\n");
		}
	}
	
	public int computeMaxBeauty(List<StringCount> list)
	   throws Exception{
		
		int maxBeauty = 0;
		
		if(list == null){
			throw new 
			Exception("Null_Character_Count_List");
		}
		
		// Iterate through the list
		
		for(int i=0,v=26;
		    i<list.size();
		    i++,v--){
			
			maxBeauty = maxBeauty +
					    (v * list.get(i).getCount());
		}
		
		return maxBeauty;
	}
	
	
	public static void main(String[] 
			                args){
		
		// instantiate object here
		
		Main m = new Main();
		String line = null;
		BufferedReader br = null;
		List<StringCount> strCountList = null;
		try {
			
			// Get the input from file
			
			File f = new File(args[0]);
			
			br = new BufferedReader(
		         new FileReader(f));
			
			// Run a while loop for all lines
			// in the file
			
			while((line = br.readLine()) != null){
				
				// Test case 1 : If the line contains 
				// any character whose ascii code is 
				// between 65-90 or 97-122, only 
				// consider those characters, discard
				// the rest
				
				strCountList = new 
				   ArrayList<StringCount>();
				
				for(int i=0;
				    i<line.length();
				    i++){
					
					// Look at each character in string
					
					char c = line.charAt(i);
					
					// check for validity 
					
					if(m.isCharacterLetter(c)){
						
						// convert to string
						
						String s = String.valueOf(c);
						
						// insert s into strCountList
						
						m.insertString(strCountList,
								       s);
					
					}
				}
				
				// Sort the list of CharacterCount objects
				
				Collections.sort(strCountList, 
				         new Comparator<StringCount>(){
			                  public int compare(StringCount o1,
			                		             StringCount o2){
			                	  return o2.getCount().
			                			 compareTo(
			                		     o1.getCount());
			                  }
		                 }
		        );
				
				
				// compute max beauty
				
				int maxBeauty = 
						m.computeMaxBeauty(strCountList);
				
				System.out.println(maxBeauty);	
				
				
			}
			
			
		} catch(Exception e){
			e.printStackTrace();
		} finally{
			try{
				
				// Close the buffered reader
				
				br.close();
				
			} catch(IOException e){
				e.printStackTrace();
			}
		}
		
		
		
	}
	
}

