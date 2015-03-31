from vertex import Vertex


class Graph : 


   def __init__(self):

      self.vertList = {}
      self.numVertices = 0


   def addVertex(self,
                 node_id) :

      new_vertex = Vertex(node_id)
      self.numVertices = self.numVertices + 1
      self.vertList[node_id] = new_vertex
      return new_vertex


   def getVertex(self,
                 n):

      if n in self.vertList :
         return self.vertList[n]
      else :
         return None


   def __contains__(self,
                    n):

      return n in self.vertList


   def addEdge(self,
               f,
               t,
               cost=0):

      src_vertex = self.vertList[f]
      if src_vertex is None :
         src_vertex = self.addVertex(f)
      dest_vertex = self.vertList[t]
      if dest_vertex is None :
         dest_vertex = self.addVertex(t)
      self.vertList[f].addNeighbor(self.vertList[t],
                                   cost)
      

   def getVertices(self) :

      return self.vertList.keys() 


   def __iter__(self):

      return iter(self.vertList.values())




if __name__ == '__main__':

   g = Graph()
   g.addVertex('1')
   g.addVertex('2')
   g.addVertex('3')
   g.addEdge('1','2',6807)
   g.addEdge('2','3',-8874)
   g.addEdge('3','1',-1055)
   for v in g.getVertices():
      print g.vertList[v]

