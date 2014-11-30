import java.util.*;



public class Graph
{
   
   
   public enum State{
      Unvisited, Visited, Visiting;
   }

 
   class Node
   {
      private int label;
      private Graph.State state;
      private List<Node> destNodes = 
      new ArrayList<Node>();;


 
      public Node(int label)
      {
         this.label = label;
         this.state = Graph.State.Unvisited;
      }

      public List<Node> getAdjacentNodes()
      {
         return this.destNodes;
      } 

      public void addEdge(List<Node> destNodes)
      {
         this.destNodes = destNodes;
      } 

      public Graph.State getState()
      {
         return this.state;
      } 

      public int getLabel()
      {
         return this.label;
      }

      public void setLabel(int label)
      {
         this.label = label;
      }

      public void setState(Graph.State s)
      {
         this.state =  s;
      } 

      
         
   }  


   private List<Node> nodes = null;
  

   // Constructor takes in an array of labels
   public Graph(int[] labels)
   {
      nodes = new ArrayList<Node>();
      for(int label : labels)
      {
         Node n = new Node(label);
         nodes.add(n);
      } 
   }

   // find the node using the label
   public Node findNode(int label)
   {
      for(Node n : this.nodes)
      {
         if(n.getLabel() == label)
            return n;
      }
      return null;
   }  


   // display all the nodes in the graph with the edges
   public void displayGraph()
   {
      // display all nodes in the graph
      for(Node n : this.nodes)
      {
         System.out.print(n.getLabel() + " : ");
         for(Node a : n.getAdjacentNodes())
         {
            System.out.print(a.getLabel() + " ");
         }
         System.out.print("\n");
      }
   }

   // Get all the nodes in the graph
   public List<Node> getNodes()
   {
      return this.nodes;
   }


   // Include all the nodes reachable from src
   // including "src" 
   public void dfs(List<Integer> l,
                   int src,
                   int dest)
   {
      // Find the node
      Node srcNode = findNode(src);

      // Set state as visited
      srcNode.setState(State.Visited);

      // add src to the list   
      l.add(src);

      // loop for all adjacent nodes
      for(Node n : srcNode.getAdjacentNodes())
      {
         if(n.getState() != State.Visited)
            dfs(l,n.getLabel(),dest);
      }    
   
   }

   // check whether there is a route between "src" and 
   // "dest"
   public boolean isRoute(int src,
                          int dest)
   {
      // Find the node corresponding to src
      Node srcNode = findNode(src); 

      // Maintain a stack
      LinkedList<Node> stack = new LinkedList<Node>();

      // Add the source node to the stack
      stack.add(srcNode);

      // Start a loop
      while(!stack.isEmpty())
      {
         // pop node from stack
         Node node = stack.removeFirst();

         node.setState(State.Visiting);
 
         // Start a loop for exploring all the adjacent nodes
         for(Node n : node.getAdjacentNodes())
         {

            if(n.getState() != State.Visited)
            {
     
               if(n.getLabel() == dest)
               {

                  n.setState(State.Visited);
                  return true;
               } 
               else
               {
                  n.setState(State.Visiting);
                  stack.add(n);
               } 
            }      
         }
         node.setState(State.Visited);
       }
       // return false since the entire data structure is exhausted  
       return false;
   } 


}





  
         
