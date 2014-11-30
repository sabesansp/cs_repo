public class LList<T>
{

   public T data;
   public LList<T> next;


   public T getData()
   {
      return data;
   } 

   public void setData(T data)
   {
      this.data = data;
   } 

   public void setNext(LList<T> node)
   {
      this.next = node;
   }



   // P : Constructor for the linked list
   public LList()
   {
      this.data = null;
      this.next = null;
   }  


   // constructor for the linked list with "data"
   public LList(T data)
   {
      this.data = data;
      this.next = null;
   } 


   // P : Insert data into the linked list
   public void insertData(T data) 
   {

      // Instantiate a new node
      LList<T> l = new LList<T>(data);      


      // Get the next node from the head
      LList<T> node = this.next;

      // the list is empty, insert the first node
      if(node == null) 
      {
         this.next = l;
      } 

      // else, the list contains some nodes, loop
      // until we find the last one

      else 
      {
         // loop until the node is null
         while(node.next != null)
            node = node.next; 
   
         // node now points to the last 
         // node in the linked list

         node.next = l;
      }

   }


   // Delete a node in the linked list that 
   // contains "data"
   public void deleteData(T data) 
   {
      // Set the previous and current nodes
      LList<T> prev = this;
      LList<T> curr = prev.next;
     
       
      // Loop through the list
      while(curr != null)
      {
         if(curr.data == data)
         {
            prev.next = curr.next;
            break;
         } 
         else
         {
            prev = prev.next;
            curr = curr.next;
         }
      }
      printList();
   }     
                

   // Print the contents of the linked list
   public void printList()
   {
      System.out.println("The contents of linked list : ");
      System.out.print("-> ");
      LList<T> node = this.next;
      while(node != null)
      {
         System.out.print(node.getData() + " -> ");
         node = node.next;
      }
      System.out.print("null\n"); 
   }   
  


}
